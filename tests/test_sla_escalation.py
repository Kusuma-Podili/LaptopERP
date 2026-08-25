from django.test import TestCase
from decimal import Decimal
from django.utils import timezone
from core.models import User
from inventory.models import Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec, DisplaySpec, GpuSpec, LaptopModel, LaptopUnit
from repairs.models import WorkshopJobCard
from repairs.services.sla_escalator import RepairSLAEngine


class SLAEscalationTestCase(TestCase):
    def setUp(self):
        self.tech = User.objects.create_user(username='sla_tech', email='sla@erp.local', password='pwd')
        self.brand = Brand.objects.create(name='Dell', code='DELL')
        self.cat = LaptopCategory.objects.create(name='Business', slug='biz')
        self.cpu = ProcessorSpec.objects.create(brand='INTEL', model_name='i7')
        self.ram = RamSpec.objects.create(ram_type='DDR5', capacity_gb=16)
        self.storage = StorageSpec.objects.create(storage_type='NVME_SSD', capacity_gb=512)
        self.display = DisplaySpec.objects.create(size_inches=Decimal('14.0'), resolution='1920x1080')
        self.gpu = GpuSpec.objects.create(brand='INTEL', model_name='Iris')
        self.model = LaptopModel.objects.create(brand=self.brand, category=self.cat, model_name='Lat 7440', model_number='L7440', processor=self.cpu, ram=self.ram, storage=self.storage, display=self.display, gpu=self.gpu)
        self.unit = LaptopUnit.objects.create(laptop_model=self.model, serial_number='SN-SLA-001', status='IN_WORKSHOP')

    def test_sla_audit_engine(self):
        job = WorkshopJobCard.objects.create(job_number='JOB-SLA-101', unit=self.unit, priority='NORMAL', assigned_technician=self.tech)
        escalated = RepairSLAEngine.audit_sla_breaches()
        self.assertIsInstance(escalated, list)
