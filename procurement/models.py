"""
Procurement Domain Models:
Suppliers, Purchase Orders, Goods Receipt Notes (GRN), and Inward Quality Check (IQC).
"""

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedUUIDModel, User
from inventory.models import LaptopModel, LaptopUnit, ComponentItem


class Supplier(TimeStampedUUIDModel):
    """Vendor / Hardware supplier master table."""
    code = models.CharField(max_length=32, unique=True)
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=128, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    tax_id = models.CharField(max_length=64, blank=True)
    payment_terms_days = models.PositiveSmallIntegerField(default=30)
    rating_score = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, default='United States')

    def __str__(self):
        return f"{self.company_name} ({self.code})"


class PurchaseOrder(TimeStampedUUIDModel):
    """Enterprise Purchase Order workflow."""
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('SUBMITTED', 'Submitted for Approval'),
        ('APPROVED', 'Approved & Sent to Vendor'),
        ('PARTIALLY_RECEIVED', 'Partially Received'),
        ('COMPLETED', 'Fully Received & Closed'),
        ('CANCELLED', 'Cancelled'),
    )
    po_number = models.CharField(max_length=64, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='purchase_orders')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='DRAFT')
    order_date = models.DateField()
    expected_delivery_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_pos')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_pos')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"PO {self.po_number} - {self.supplier.company_name} (${self.total_amount})"


class PurchaseOrderItem(TimeStampedUUIDModel):
    """Line item in Purchase Order."""
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    laptop_model = models.ForeignKey(LaptopModel, on_delete=models.PROTECT, null=True, blank=True)
    component = models.ForeignKey(ComponentItem, on_delete=models.PROTECT, null=True, blank=True)
    quantity_ordered = models.PositiveIntegerField(default=1)
    quantity_received = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity_ordered * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        item_name = self.laptop_model.model_name if self.laptop_model else self.component.name
        return f"{self.quantity_ordered}x {item_name} @ ${self.unit_price}"


class GoodsReceiptNote(TimeStampedUUIDModel):
    """Inward Goods Receiving Note (GRN) on warehouse dock."""
    grn_number = models.CharField(max_length=64, unique=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.PROTECT, related_name='receipt_notes')
    receiving_date = models.DateTimeField(auto_now_add=True)
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    carrier_tracking_number = models.CharField(max_length=128, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"GRN {self.grn_number} (PO: {self.purchase_order.po_number})"


class InwardQualityCheck(TimeStampedUUIDModel):
    """Quality inspection check for newly arrived batch or serial units."""
    RESULT_CHOICES = (
        ('PASSED', 'Passed IQC - Accept to Stock'),
        ('REJECTED', 'Failed IQC - Reject to Supplier'),
        ('CONDITIONAL', 'Conditional Pass (Grade B/C)'),
    )
    grn = models.ForeignKey(GoodsReceiptNote, on_delete=models.CASCADE, related_name='qc_inspections')
    inspector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    result = models.CharField(max_length=32, choices=RESULT_CHOICES, default='PASSED')
    units_inspected = models.PositiveIntegerField(default=1)
    units_passed = models.PositiveIntegerField(default=1)
    units_rejected = models.PositiveIntegerField(default=0)
    rejection_reason = models.TextField(blank=True)

    def __str__(self):
        return f"IQC for {self.grn.grn_number}: {self.result}"
