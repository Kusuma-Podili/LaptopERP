"""
Warehouse Logistics & Multi-Location Bin Allocation Models.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedUUIDModel, Branch, User
from inventory.models import LaptopUnit, ComponentItem


class Warehouse(TimeStampedUUIDModel):
    """Physical warehouse facility."""
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='warehouses')
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=255)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_warehouses')
    address = models.TextField(blank=True)
    total_capacity_units = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Zone(TimeStampedUUIDModel):
    """Warehouse internal zone (e.g. Inward Dock, Storage A, Workshop QA, Outward Staging)."""
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='zones')
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    zone_type = models.CharField(max_length=32, choices=(
        ('INWARD', 'Inward Receiving Dock'),
        ('STORAGE', 'General Storage'),
        ('QC', 'Quality Control Holding'),
        ('WORKSHOP', 'Repair Workshop Buffer'),
        ('DISPATCH', 'Outward Dispatch Staging'),
        ('SCRAP', 'Scrap & Quarantine'),
    ), default='STORAGE')

    class Meta:
        unique_together = ('warehouse', 'code')

    def __str__(self):
        return f"{self.warehouse.code} - Zone {self.name}"


class Bin(TimeStampedUUIDModel):
    """Exact bin location (Aisle-Rack-Shelf-Bin)."""
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='bins')
    bin_code = models.CharField(max_length=64, unique=True, help_text=_("e.g. A01-R02-S03-B04"))
    max_units = models.PositiveIntegerField(default=20)
    current_occupancy = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Bin {self.bin_code} [{self.zone.warehouse.code}]"


class StockTransferOrder(TimeStampedUUIDModel):
    """Inter-warehouse or inter-zone inventory transfer order."""
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('APPROVED', 'Approved for Transfer'),
        ('IN_TRANSIT', 'In Transit'),
        ('RECEIVED', 'Received at Destination'),
        ('CANCELLED', 'Cancelled'),
    )
    transfer_number = models.CharField(max_length=64, unique=True)
    source_warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name='transfers_out')
    destination_warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, related_name='transfers_in')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='DRAFT')
    initiated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='initiated_transfers')
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_transfers')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Transfer {self.transfer_number} ({self.source_warehouse.code} -> {self.destination_warehouse.code})"


class StockTransferItem(TimeStampedUUIDModel):
    """Specific serialized laptop unit attached to transfer order."""
    transfer_order = models.ForeignKey(StockTransferOrder, on_delete=models.CASCADE, related_name='items')
    unit = models.ForeignKey(LaptopUnit, on_delete=models.PROTECT, related_name='transfers')
    is_received = models.BooleanField(default=False)

    def __str__(self):
        return f"Transfer Item: SN {self.unit.serial_number} on {self.transfer_order.transfer_number}"


class CycleCount(TimeStampedUUIDModel):
    """Periodic inventory audit / cycle counting batch."""
    count_number = models.CharField(max_length=64, unique=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    auditor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=32, choices=(('PENDING', 'In Progress'), ('COMPLETED', 'Completed'), ('RECONCILED', 'Reconciled')), default='PENDING')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Cycle Count {self.count_number} - {self.warehouse.name}"
