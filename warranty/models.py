"""
Warranty Registrations, RMA Claims, and Customer Support Tickets.
"""

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedUUIDModel, User
from inventory.models import LaptopUnit
from sales.models import Customer


class WarrantyPolicy(TimeStampedUUIDModel):
    """Standard warranty coverage policy."""
    name = models.CharField(max_length=128)
    duration_months = models.PositiveSmallIntegerField(default=12)
    terms_and_conditions = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.duration_months} Months)"


class ProductWarrantyRegistration(TimeStampedUUIDModel):
    """Warranty bound to individual serialized laptop unit and client."""
    unit = models.OneToOneField(LaptopUnit, on_delete=models.CASCADE, related_name='warranty_record')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='warranties')
    policy = models.ForeignKey(WarrantyPolicy, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Warranty: SN {self.unit.serial_number} for {self.customer.name} (Valid till {self.end_date})"


class RMATicket(TimeStampedUUIDModel):
    """Return Merchandise Authorization (RMA) ticket."""
    STATUS_CHOICES = (
        ('SUBMITTED', 'RMA Request Submitted'),
        ('APPROVED', 'RMA Approved - Awaiting Return'),
        ('RECEIVED', 'Unit Received at RMA Hub'),
        ('INSPECTION', 'Under RMA Inspection'),
        ('REPLACEMENT_DISPATCHED', 'Replacement Dispatched'),
        ('CREDIT_ISSUED', 'Credit Note Issued'),
        ('REJECTED', 'RMA Rejected (Out of Warranty / Abuse)'),
        ('CLOSED', 'RMA Closed'),
    )
    rma_number = models.CharField(max_length=64, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='rma_claims')
    unit = models.ForeignKey(LaptopUnit, on_delete=models.PROTECT, related_name='rma_tickets')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='SUBMITTED')
    reason_for_return = models.TextField()
    inspection_notes = models.TextField(blank=True)
    action_taken = models.TextField(blank=True)

    def __str__(self):
        return f"RMA #{self.rma_number} - SN: {self.unit.serial_number} ({self.get_status_display()})"
