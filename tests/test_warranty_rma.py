from django.test import TestCase
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta
from warranty.models import WarrantyPolicy, ProductWarrantyRegistration, RMATicket
from warranty.services.rma import WarrantyValidationService
from inventory.models import Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec, DisplaySpec, GpuSpec, LaptopModel, LaptopUnit
from sales.models import Customer


class WarrantyRMATestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(customer_number='C-99', name='VIP Client', email='vip@client.com', phone='555')
        self.brand = Brand.objects.create(name='Lenovo', code='LEN')
        self.cat = LaptopCategory.objects.create(name='Business', slug='biz')
        self.cpu = ProcessorSpec.objects.create(brand='INTEL', model_name='i7')
        self.ram = RamSpec.objects.create(ram_type='DDR4', capacity_gb=16)
        self.storage = StorageSpec.objects.create(storage_type='NVME_SSD', capacity_gb=512)
        self.display = DisplaySpec.objects.create(size_inches=Decimal('14.0'), resolution='1920x1080')
        self.gpu = GpuSpec.objects.create(brand='INTEL', model_name='Iris')

        self.model = LaptopModel.objects.create(
            brand=self.brand, category=self.cat, model_name='ThinkPad X1 Carbon', model_number='TP-X1-C9',
            processor=self.cpu, ram=self.ram, storage=self.storage, display=self.display, gpu=self.gpu
        )
        self.unit = LaptopUnit.objects.create(laptop_model=self.model, serial_number='SN-X1-8877')
        self.policy = WarrantyPolicy.objects.create(name='1-Year Standard ProSupport', duration_months=12, terms_and_conditions='Terms')

    def test_warranty_validation_active_and_expired(self):
        today = timezone.now().date()
        reg = ProductWarrantyRegistration.objects.create(
            unit=self.unit,
            customer=self.customer,
            policy=self.policy,
            start_date=today - timedelta(days=30),
            end_date=today + timedelta(days=335),
            is_active=True
        )
        self.assertTrue(WarrantyValidationService.is_unit_under_warranty(self.unit))

        reg.end_date = today - timedelta(days=1)
        reg.save()
        self.assertFalse(WarrantyValidationService.is_unit_under_warranty(self.unit))
