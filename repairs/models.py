"""
Workshop Diagnostics, Job Cards, and Refurbishing Engineering Models.
"""

import uuid
from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedUUIDModel, User
from inventory.models import LaptopUnit, ComponentItem


class DiagnosticChecklistMaster(TimeStampedUUIDModel):
    """Standard QA & diagnostic testing points for laptops."""
    CATEGORY_CHOICES = (
        ('POWER_BATTERY', 'Power, Charging & Battery Health'),
        ('DISPLAY_GPU', 'Screen Panel, Touch, Backlight & GPU'),
        ('CPU_RAM_STORAGE', 'Processor Stress, RAM Test & Storage SMART'),
        ('PORTS_CONNECTIVITY', 'Wi-Fi, Bluetooth, USB, HDMI & Audio'),
        ('INPUT_DEVICES', 'Keyboard, Trackpad & Fingerprint Sensor'),
        ('THERMAL_ACOUSTIC', 'Fan Operation, Heat Dissipation & Noise'),
        ('COSMETIC_BODY', 'Hinges, Chassis Scratches & Casing Integrity'),
    )
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    test_code = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=255)
    instructions = models.TextField(blank=True)
    is_mandatory = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"


class WorkshopJobCard(TimeStampedUUIDModel):
    """Repair & Refurbishing Work Order / Job Card."""
    STATUS_CHOICES = (
        ('QUEUED', 'Queued for Diagnostics'),
        ('IN_DIAGNOSTICS', 'Under Diagnostics'),
        ('WAITING_PARTS', 'Waiting for Spare Parts'),
        ('REPAIR_IN_PROGRESS', 'Repair / Upgrade in Progress'),
        ('QA_TESTING', 'Post-Repair Quality Assurance'),
        ('COMPLETED', 'Repaired & Refurbished (Ready)'),
        ('BEYOND_ECONOMIC_REPAIR', 'BER - Scrapped for Parts'),
    )
    PRIORITY_CHOICES = (
        ('LOW', 'Low Priority'),
        ('NORMAL', 'Standard Priority'),
        ('HIGH', 'High Priority'),
        ('URGENT', 'Urgent / RMA Priority'),
    )
    job_number = models.CharField(max_length=64, unique=True)
    unit = models.ForeignKey(LaptopUnit, on_delete=models.PROTECT, related_name='job_cards')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='QUEUED')
    priority = models.CharField(max_length=16, choices=PRIORITY_CHOICES, default='NORMAL')
    assigned_technician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_jobs')
    customer_reported_issue = models.TextField(blank=True)
    diagnostic_summary = models.TextField(blank=True)
    estimated_labor_hours = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    actual_labor_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    total_parts_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_labor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_repair_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Job #{self.job_number} - SN: {self.unit.serial_number} ({self.get_status_display()})"


class DiagnosticResult(TimeStampedUUIDModel):
    """Specific checklist test result on a job card."""
    job_card = models.ForeignKey(WorkshopJobCard, on_delete=models.CASCADE, related_name='test_results')
    test_item = models.ForeignKey(DiagnosticChecklistMaster, on_delete=models.PROTECT)
    passed = models.BooleanField(default=True)
    measured_value = models.CharField(max_length=128, blank=True, help_text=_("e.g. Battery 88%, CPU Temp 62C, Read 3200MB/s"))
    remarks = models.TextField(blank=True)

    def __str__(self):
        status = "PASSED" if self.passed else "FAILED"
        return f"{self.job_card.job_number} - {self.test_item.test_code}: {status}"


class JobCardPartRequisition(TimeStampedUUIDModel):
    """Spare parts issued from inventory and consumed in repair."""
    job_card = models.ForeignKey(WorkshopJobCard, on_delete=models.CASCADE, related_name='parts_used')
    component = models.ForeignKey(ComponentItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_cost_at_repair = models.DecimalField(max_digits=10, decimal_places=2)
    is_fitted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity}x {self.component.name} for Job #{self.job_card.job_number}"


class RepairLaborLog(TimeStampedUUIDModel):
    """Technician time tracking entries."""
    job_card = models.ForeignKey(WorkshopJobCard, on_delete=models.CASCADE, related_name='labor_logs')
    technician = models.ForeignKey(User, on_delete=models.PROTECT)
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2)
    work_performed = models.TextField()

    def __str__(self):
        return f"{self.technician.username}: {self.hours_spent}h on Job #{self.job_card.job_number}"
