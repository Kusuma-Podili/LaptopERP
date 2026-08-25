"""
Inventory & Serial Lifecycle Models.
Includes Hardware Specification Master Tables, Serial Number Tracking, Condition Grading, and Compatibility.
"""

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from core.models import TimeStampedUUIDModel, User


class Brand(TimeStampedUUIDModel):
    """Laptop and component manufacturers (e.g. Dell, HP, Lenovo, Apple, Asus, Acer, etc.)."""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=32, unique=True)
    country_of_origin = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)
    support_phone = models.CharField(max_length=32, blank=True)
    support_email = models.EmailField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class LaptopCategory(TimeStampedUUIDModel):
    """Form-factor / Market category (Business, Ultrabook, Gaming, Workstation, 2-in-1, Budget)."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Laptop Categories'

    def __str__(self):
        return self.name


class ProcessorSpec(TimeStampedUUIDModel):
    """CPU specifications master table."""
    brand = models.CharField(max_length=64, choices=(('INTEL', 'Intel'), ('AMD', 'AMD'), ('APPLE', 'Apple Silicon'), ('QUALCOMM', 'Qualcomm Snapdragon')))
    model_name = models.CharField(max_length=128, help_text=_("e.g. Core i7-13700H, Ryzen 7 7840U, M3 Pro"))
    generation = models.CharField(max_length=64, blank=True)
    cores = models.PositiveSmallIntegerField(default=4)
    threads = models.PositiveSmallIntegerField(default=8)
    base_clock_ghz = models.DecimalField(max_digits=4, decimal_places=2, default=2.40)
    boost_clock_ghz = models.DecimalField(max_digits=4, decimal_places=2, default=4.80)
    cache_mb = models.PositiveSmallIntegerField(default=12)

    def __str__(self):
        return f"{self.brand} {self.model_name}"


class RamSpec(TimeStampedUUIDModel):
    """RAM specification master table."""
    ram_type = models.CharField(max_length=32, choices=(('DDR3', 'DDR3'), ('DDR4', 'DDR4'), ('DDR5', 'DDR5'), ('LPDDR4X', 'LPDDR4X'), ('LPDDR5', 'LPDDR5'), ('UNIFIED', 'Apple Unified Memory')))
    capacity_gb = models.PositiveIntegerField(help_text=_("Capacity in Gigabytes (e.g. 8, 16, 32, 64)"))
    speed_mhz = models.PositiveIntegerField(default=3200)
    is_expandable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.capacity_gb}GB {self.ram_type} @ {self.speed_mhz}MHz"


class StorageSpec(TimeStampedUUIDModel):
    """Storage drives master table."""
    storage_type = models.CharField(max_length=32, choices=(('NVME_SSD', 'M.2 NVMe PCIe SSD'), ('SATA_SSD', '2.5" SATA SSD'), ('HDD', 'Mechanical HDD'), ('EMMC', 'eMMC Embedded')))
    capacity_gb = models.PositiveIntegerField(help_text=_("Capacity in GB (e.g. 256, 512, 1024, 2048)"))
    form_factor = models.CharField(max_length=32, default='M.2 2280')

    def __str__(self):
        cap_str = f"{self.capacity_gb // 1024}TB" if self.capacity_gb >= 1024 else f"{self.capacity_gb}GB"
        return f"{cap_str} {self.get_storage_type_display()}"


class DisplaySpec(TimeStampedUUIDModel):
    """Screen panel specifications."""
    size_inches = models.DecimalField(max_digits=4, decimal_places=1, help_text=_("e.g. 13.3, 14.0, 15.6, 16.0, 17.3"))
    resolution = models.CharField(max_length=64, help_text=_("e.g. 1920x1080 (FHD), 2560x1440 (QHD), 3840x2160 (4K)"))
    panel_type = models.CharField(max_length=32, choices=(('IPS', 'IPS LCD'), ('OLED', 'OLED'), ('VA', 'VA'), ('TN', 'TN LCD')), default='IPS')
    refresh_rate_hz = models.PositiveSmallIntegerField(default=60)
    is_touchscreen = models.BooleanField(default=False)

    def __str__(self):
        touch = " Touch" if self.is_touchscreen else ""
        return f"{self.size_inches}" {self.resolution} {self.panel_type}{touch} ({self.refresh_rate_hz}Hz)"


class GpuSpec(TimeStampedUUIDModel):
    """Graphics Processor specifications."""
    brand = models.CharField(max_length=64, choices=(('NVIDIA', 'NVIDIA GeForce / RTX'), ('AMD', 'AMD Radeon'), ('INTEL', 'Intel Arc / Iris Xe'), ('APPLE', 'Apple GPU')))
    model_name = models.CharField(max_length=128)
    vram_gb = models.PositiveSmallIntegerField(default=0, help_text=_("0 for Integrated Graphics"))
    is_dedicated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model_name} ({self.vram_gb}GB VRAM)" if self.is_dedicated else f"{self.brand} {self.model_name} (Integrated)"


class LaptopModel(TimeStampedUUIDModel):
    """Master Laptop Model catalog definition."""
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='models')
    category = models.ForeignKey(LaptopCategory, on_delete=models.PROTECT, related_name='laptops')
    model_name = models.CharField(max_length=255, help_text=_("e.g. ThinkPad T14 Gen 4, Latitude 7420, MacBook Pro 14"))
    model_number = models.CharField(max_length=128, unique=True, help_text=_("Manufacturer part/model SKU"))
    processor = models.ForeignKey(ProcessorSpec, on_delete=models.PROTECT)
    ram = models.ForeignKey(RamSpec, on_delete=models.PROTECT)
    storage = models.ForeignKey(StorageSpec, on_delete=models.PROTECT)
    display = models.ForeignKey(DisplaySpec, on_delete=models.PROTECT)
    gpu = models.ForeignKey(GpuSpec, on_delete=models.PROTECT)
    operating_system = models.CharField(max_length=64, default='Windows 11 Pro')
    msrp_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    standard_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    minimum_stock_threshold = models.PositiveIntegerField(default=5)
    image = models.ImageField(upload_to='laptops/', null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['brand', 'model_name']

    def __str__(self):
        return f"{self.brand.name} {self.model_name} ({self.model_number})"

    @property
    def current_in_stock_count(self):
        return self.units.filter(status='IN_STOCK').count()


class LaptopUnit(TimeStampedUUIDModel):
    """Individual physical laptop instance identified by unique Serial Number."""
    STATUS_CHOICES = (
        ('INWARD_RECEIVED', 'Inward Received (Pending QC)'),
        ('IN_QC', 'Under Inward Quality Check'),
        ('QC_FAILED', 'Failed QC Inspection'),
        ('IN_STOCK', 'Available in Stock'),
        ('RESERVED', 'Reserved for Sales Order'),
        ('IN_WORKSHOP', 'In Repair / Refurbishing Workshop'),
        ('DIAGNOSTICS_COMPLETED', 'Diagnostics Completed'),
        ('READY_FOR_DISPATCH', 'Ready for Dispatch'),
        ('SHIPPED', 'Shipped to Customer'),
        ('RMA_RETURNED', 'Returned via RMA'),
        ('SCRAPPED', 'Scrapped / Salvaged for Parts'),
    )

    GRADE_CHOICES = (
        ('NEW', 'Brand New (Sealed)'),
        ('OPEN_BOX', 'Open Box (Like New)'),
        ('GRADE_A_PLUS', 'Grade A+ (Flawless Refurbished)'),
        ('GRADE_A', 'Grade A (Minor cosmetic signs)'),
        ('GRADE_B', 'Grade B (Noticeable cosmetic scratches)'),
        ('GRADE_C', 'Grade C (Dents / Heavy wear)'),
        ('SCRAP', 'Grade Scrap (Non-functional)'),
    )

    laptop_model = models.ForeignKey(LaptopModel, on_delete=models.PROTECT, related_name='units')
    serial_number = models.CharField(max_length=128, unique=True, db_index=True)
    barcode = models.CharField(max_length=128, unique=True, db_index=True, blank=True)
    imei_or_asset_tag = models.CharField(max_length=128, blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='INWARD_RECEIVED', db_index=True)
    condition_grade = models.CharField(max_length=32, choices=GRADE_CHOICES, default='GRADE_A')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    battery_health_percentage = models.PositiveSmallIntegerField(default=100)
    battery_cycle_count = models.PositiveIntegerField(default=0)
    current_location = models.CharField(max_length=255, default='Inward Dock', help_text=_("Warehouse Bin or Department location"))
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.laptop_model.model_name} [SN: {self.serial_number}] ({self.get_status_display()})"

    def save(self, *args, **kwargs):
        if not self.barcode:
            self.barcode = f"BC-{self.serial_number}"
        super().save(*args, **kwargs)


class SerialLifecycleHistory(TimeStampedUUIDModel):
    """Complete lifecycle traceability for every serialized laptop."""
    unit = models.ForeignKey(LaptopUnit, on_delete=models.CASCADE, related_name='history_logs')
    previous_status = models.CharField(max_length=32, blank=True)
    new_status = models.CharField(max_length=32)
    location = models.CharField(max_length=255, blank=True)
    action_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    reference_document = models.CharField(max_length=128, blank=True, help_text=_("PO #, Job Card #, Invoice #, or RMA #"))
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"SN: {self.unit.serial_number} -> {self.new_status} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class ComponentItem(TimeStampedUUIDModel):
    """Spare components (RAM sticks, SSDs, Screens, Batteries, Keyboards, Motherboards)."""
    COMPONENT_TYPES = (
        ('RAM', 'Memory Module (RAM)'),
        ('STORAGE', 'Storage Drive (SSD/HDD)'),
        ('SCREEN', 'Display Panel'),
        ('BATTERY', 'Laptop Battery'),
        ('KEYBOARD', 'Keyboard Assembly'),
        ('MOTHERBOARD', 'System Board / Motherboard'),
        ('CHARGER', 'AC Power Adapter'),
        ('FAN', 'Cooling Fan / Heatsink'),
    )
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    component_type = models.CharField(max_length=32, choices=COMPONENT_TYPES)
    part_number = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=255)
    specification_summary = models.TextField(blank=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity_on_hand = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"[{self.get_component_type_display()}] {self.name} ({self.part_number}) - Stock: {self.quantity_on_hand}"


class ComponentCompatibility(TimeStampedUUIDModel):
    """Cross-reference compatibility between Laptop Models and Spare Components."""
    laptop_model = models.ForeignKey(LaptopModel, on_delete=models.CASCADE, related_name='compatibilities')
    component = models.ForeignKey(ComponentItem, on_delete=models.CASCADE, related_name='compatible_models')
    is_oem = models.BooleanField(default=True, help_text=_("Original Equipment Manufacturer component"))
    installation_notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('laptop_model', 'component')

    def __str__(self):
        return f"{self.laptop_model.model_name} <-> {self.component.name}"
