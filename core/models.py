"""
Core Domain Models for LaptopERP.
Includes Custom User, Enterprise Roles, Multi-Branch/Department, Audit Logs, and System Configurations.
"""

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class TimeStampedUUIDModel(models.Model):
    """Abstract base model providing UUID primary key and timestamp tracking."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, help_text=_("Designates whether this record is active."))

    class Meta:
        abstract = True
        ordering = ['-created_at']


class CompanyProfile(TimeStampedUUIDModel):
    """Master Company details for multi-tenant and single-enterprise setups."""
    name = models.CharField(max_length=255, unique=True)
    legal_name = models.CharField(max_length=255, blank=True)
    tax_identifier = models.CharField(max_length=64, blank=True, help_text=_("VAT / GST / Tax ID"))
    registration_number = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=True)
    website = models.URLField(blank=True)
    currency_code = models.CharField(max_length=3, default='USD')
    currency_symbol = models.CharField(max_length=8, default='$')
    logo = models.ImageField(upload_to='company/', null=True, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state_province = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=100, default='United States')
    financial_year_start_month = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = _('Company Profile')
        verbose_name_plural = _('Company Profiles')

    def __str__(self):
        return self.name


class Branch(TimeStampedUUIDModel):
    """Physical enterprise locations / operational branches."""
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='branches')
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    is_headquarters = models.BooleanField(default=False)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='United States')

    class Meta:
        verbose_name = _('Branch')
        verbose_name_plural = _('Branches')

    def __str__(self):
        return f"{self.name} ({self.code})"


class Department(TimeStampedUUIDModel):
    """Organizational business departments."""
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='departments', null=True, blank=True)
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return self.name


class Role(TimeStampedUUIDModel):
    """Fine-grained Role-Based Access Control (RBAC) definitions."""
    ROLE_CHOICES = (
        ('ADMIN', 'Super Administrator'),
        ('EXECUTIVE', 'Executive Management'),
        ('WAREHOUSE_MGR', 'Warehouse Manager'),
        ('INVENTORY_CLERK', 'Inventory Clerk'),
        ('TECHNICIAN_SENIOR', 'Senior Diagnostic Technician'),
        ('TECHNICIAN_JUNIOR', 'Junior Repair Technician'),
        ('PROCUREMENT_OFFICER', 'Procurement Officer'),
        ('SALES_EXEC', 'Sales Executive'),
        ('SALES_MGR', 'Sales Manager'),
        ('WARRANTY_REP', 'Warranty / RMA Representative'),
        ('AUDITOR', 'Compliance & Quality Auditor'),
    )
    code = models.CharField(max_length=64, choices=ROLE_CHOICES, unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    can_manage_users = models.BooleanField(default=False)
    can_manage_inventory = models.BooleanField(default=False)
    can_manage_warehouse = models.BooleanField(default=False)
    can_manage_procurement = models.BooleanField(default=False)
    can_perform_repairs = models.BooleanField(default=False)
    can_manage_sales = models.BooleanField(default=False)
    can_approve_invoices = models.BooleanField(default=False)
    can_process_rma = models.BooleanField(default=False)
    can_view_analytics = models.BooleanField(default=False)
    can_view_audit_logs = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Enterprise Role')
        verbose_name_plural = _('Enterprise Roles')

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    """Custom manager for Enterprise User model supporting email-based identification."""
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set.'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser, TimeStampedUUIDModel):
    """Enterprise User extending Django AbstractUser with RBAC, Employee Profile, and Security Flags."""
    email = models.EmailField(_('email address'), unique=True)
    employee_id = models.CharField(max_length=32, unique=True, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff')
    phone_number = models.CharField(max_length=32, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_technician = models.BooleanField(default=False)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    failed_login_attempts = models.PositiveIntegerField(default=0)
    account_locked_until = models.DateTimeField(null=True, blank=True)
    last_password_change = models.DateTimeField(default=timezone.now)
    require_password_change = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['username']

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.role.name if self.role else 'No Role'})"

    def has_role_permission(self, perm_field):
        if self.is_superuser:
            return True
        if not self.role:
            return False
        return getattr(self.role, perm_field, False)


class UserProfile(TimeStampedUUIDModel):
    """Detailed personal and operational metadata for ERP personnel."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_joining = models.DateField(null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=128, blank=True)
    emergency_contact_phone = models.CharField(max_length=32, blank=True)
    bio = models.TextField(blank=True)
    preferred_theme = models.CharField(max_length=32, default='light', choices=(('light', 'Light Mode'), ('dark', 'Dark Mode'), ('auto', 'System Default')))
    email_notifications_enabled = models.BooleanField(default=True)
    sms_notifications_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile of {self.user.username}"


class AuditLog(TimeStampedUUIDModel):
    """Immutable audit trail recording every significant CRUD and security event."""
    ACTION_CHOICES = (
        ('CREATE', 'Record Created'),
        ('UPDATE', 'Record Updated'),
        ('DELETE', 'Record Deleted'),
        ('LOGIN', 'User Login'),
        ('LOGOUT', 'User Logout'),
        ('STATUS_CHANGE', 'Workflow Status Change'),
        ('EXPORT', 'Data Exported'),
        ('SECURITY', 'Security Alert / Violation'),
        ('STOCK_ADJUSTMENT', 'Stock Adjustment'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs')
    action = models.CharField(max_length=32, choices=ACTION_CHOICES)
    module = models.CharField(max_length=64, db_index=True)
    entity_name = models.CharField(max_length=128)
    entity_id = models.CharField(max_length=128, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    details = models.TextField(blank=True, help_text=_("JSON-formatted or descriptive diff of the change."))
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        verbose_name = _('Audit Log')
        verbose_name_plural = _('Audit Logs')
        ordering = ['-timestamp']

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.user} - {self.action} on {self.module} ({self.entity_name})"


class SystemSetting(TimeStampedUUIDModel):
    """Dynamic key-value configuration registry for ERP features."""
    DATA_TYPE_CHOICES = (
        ('STRING', 'String'),
        ('INTEGER', 'Integer'),
        ('FLOAT', 'Float / Decimal'),
        ('BOOLEAN', 'Boolean'),
        ('JSON', 'JSON Object'),
    )
    key = models.CharField(max_length=128, unique=True)
    value = models.TextField()
    data_type = models.CharField(max_length=16, choices=DATA_TYPE_CHOICES, default='STRING')
    category = models.CharField(max_length=64, default='GENERAL')
    description = models.TextField(blank=True)
    is_editable = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('System Setting')
        verbose_name_plural = _('System Settings')
        ordering = ['category', 'key']

    def __str__(self):
        return f"{self.key} = {self.value}"

    def get_casted_value(self):
        if self.data_type == 'BOOLEAN':
            return self.value.lower() in ('true', '1', 'yes')
        elif self.data_type == 'INTEGER':
            return int(self.value)
        elif self.data_type == 'FLOAT':
            return float(self.value)
        return self.value


class Notification(TimeStampedUUIDModel):
    """In-app notifications for ERP alerts, stock warnings, and workflow approvals."""
    SEVERITY_CHOICES = (
        ('INFO', 'Information'),
        ('SUCCESS', 'Success'),
        ('WARNING', 'Warning'),
        ('DANGER', 'Critical / Alert'),
    )
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    severity = models.CharField(max_length=16, choices=SEVERITY_CHOICES, default='INFO')
    link_url = models.CharField(max_length=255, blank=True)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')
        ordering = ['-created_at']

    def __str__(self):
        return f"To {self.recipient.username}: {self.title}"

    def mark_as_read(self):
        self.is_read = True
        self.read_at = timezone.now()
        self.save(update_fields=['is_read', 'read_at'])


class SystemAlert(TimeStampedUUIDModel):
    """Global system banner alerts for maintenance and critical warnings."""
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    valid_from = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
