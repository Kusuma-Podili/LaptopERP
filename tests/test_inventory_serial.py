from django.test import TestCase
from decimal import Decimal
from core.models import User
from inventory.models import (
    Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec,
    DisplaySpec, GpuSpec, LaptopModel, LaptopUnit
)
from inventory.services.serial import SerialLifecycleService


class SerialLifecycleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', email='tester@erp.local', password='pwd')
        self.brand = Brand.objects.create(name='Dell', code='DELL')
        self.cat = LaptopCategory.objects.create(name='Business', slug='business')
        self.cpu = ProcessorSpec.objects.create(brand='INTEL', model_name='i7-13700H')
        self.ram = RamSpec.objects.create(ram_type='DDR5', capacity_gb=16)
        self.storage = StorageSpec.objects.create(storage_type='NVME_SSD', capacity_gb=512)
        self.display = DisplaySpec.objects.create(size_inches=Decimal('14.0'), resolution='1920x1080')
        self.gpu = GpuSpec.objects.create(brand='INTEL', model_name='Iris Xe')

        self.model = LaptopModel.objects.create(
            brand=self.brand,
            category=self.cat,
            model_name='Latitude 5440',
            model_number='LAT-5440-01',
            processor=self.cpu,
            ram=self.ram,
            storage=self.storage,
            display=self.display,
            gpu=self.gpu,
            msrp_price=Decimal('1100.00'),
            standard_cost=Decimal('700.00')
        )

        self.unit = LaptopUnit.objects.create(
            laptop_model=self.model,
            serial_number='SN-DELL-9001',
            purchase_price=Decimal('700.00'),
            status='INWARD_RECEIVED'
        )

    def test_serial_status_transition(self):
        self.assertEqual(self.unit.status, 'INWARD_RECEIVED')
        SerialLifecycleService.transition_status(
            self.unit,
            'IN_STOCK',
            user=self.user,
            location='Aisle 1 - Bin B02',
            ref_doc='GRN-101',
            notes='Passed Inward Inspection'
        )
        self.unit.refresh_from_db()
        self.assertEqual(self.unit.status, 'IN_STOCK')
        self.assertEqual(self.unit.current_location, 'Aisle 1 - Bin B02')
        self.assertEqual(self.unit.history_logs.count(), 1)
        self.assertEqual(self.unit.history_logs.first().new_status, 'IN_STOCK')
