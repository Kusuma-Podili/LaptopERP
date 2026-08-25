"""
Sales Orders, CRM, Invoicing, Tax Engine, and Receipts Models.
"""

import uuid
from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedUUIDModel, User
from inventory.models import LaptopModel, LaptopUnit


class Customer(TimeStampedUUIDModel):
    """B2B & B2C Customer directory."""
    CUSTOMER_TYPES = (
        ('B2B_ENTERPRISE', 'Corporate Enterprise Client'),
        ('B2B_RESELLER', 'Wholesale Reseller'),
        ('B2C_RETAIL', 'Retail Consumer'),
        ('INSTITUTION', 'Educational / Govt Institution'),
    )
    customer_number = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=255)
    customer_type = models.CharField(max_length=32, choices=CUSTOMER_TYPES, default='B2B_ENTERPRISE')
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    tax_id = models.CharField(max_length=64, blank=True, help_text=_("Tax / GST / VAT Registration"))
    credit_limit = models.DecimalField(max_digits=12, decimal_places=2, default=50000.00)
    outstanding_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, default='United States')

    def __str__(self):
        return f"{self.name} [{self.customer_number}]"


class TaxRule(TimeStampedUUIDModel):
    """Tax configuration rules (GST / VAT / Sales Tax)."""
    name = models.CharField(max_length=128)
    rate_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=18.00)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.rate_percentage}%)"


class SalesOrder(TimeStampedUUIDModel):
    """Sales Order lifecycle."""
    STATUS_CHOICES = (
        ('DRAFT', 'Draft Quote'),
        ('CONFIRMED', 'Confirmed Order'),
        ('ALLOCATED', 'Units Allocated'),
        ('DELIVERED', 'Delivered'),
        ('INVOICED', 'Fully Invoiced'),
        ('CANCELLED', 'Cancelled'),
    )
    order_number = models.CharField(max_length=64, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
    sales_rep = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sales_orders')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='DRAFT')
    order_date = models.DateField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order #{self.order_number} - {self.customer.name} (${self.total_amount})"


class SalesOrderItem(TimeStampedUUIDModel):
    """Line item on sales order."""
    order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='items')
    laptop_model = models.ForeignKey(LaptopModel, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        discount = (self.discount_percentage / Decimal('100.00')) * self.unit_price
        price_after_disc = self.unit_price - discount
        self.line_total = self.quantity * price_after_disc
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity}x {self.laptop_model.model_name} @ ${self.unit_price}"


class Invoice(TimeStampedUUIDModel):
    """Financial Tax Invoice."""
    PAYMENT_STATUS_CHOICES = (
        ('UNPAID', 'Unpaid'),
        ('PARTIAL', 'Partially Paid'),
        ('PAID', 'Paid in Full'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    )
    invoice_number = models.CharField(max_length=64, unique=True)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.PROTECT, related_name='invoices')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='invoices')
    issue_date = models.DateField()
    due_date = models.DateField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    payment_status = models.CharField(max_length=32, choices=PAYMENT_STATUS_CHOICES, default='UNPAID')

    def __str__(self):
        return f"Invoice #{self.invoice_number} - {self.customer.name} (${self.total_amount})"


class PaymentRecord(TimeStampedUUIDModel):
    """Customer payment transaction receipts."""
    PAYMENT_METHODS = (
        ('BANK_WIRE', 'Bank Wire / ACH'),
        ('CREDIT_CARD', 'Credit / Debit Card'),
        ('CHECK', 'Corporate Check'),
        ('CASH', 'Cash'),
        ('ONLINE', 'Online Payment Gateway'),
    )
    receipt_number = models.CharField(max_length=64, unique=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=32, choices=PAYMENT_METHODS, default='BANK_WIRE')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField()
    transaction_reference = models.CharField(max_length=128, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Payment #{self.receipt_number} (${self.amount}) for {self.invoice.invoice_number}"
