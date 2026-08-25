from django.test import TestCase
from decimal import Decimal
from core.models import User
from inventory.models import Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec, DisplaySpec, GpuSpec, LaptopModel, LaptopUnit, ComponentItem
from repairs.models import WorkshopJobCard, JobCardPartRequisition, RepairLaborLog
from repairs.services.workflow import JobCardWorkflowService


class WorkshopRepairsTestCase(TestCase):
    def setUp(self):
        self.tech = User.objects.create_user(username='tech_sam', email='sam@tech.com', password='pwd', hourly_rate=Decimal('50.00'))
        self.brand = Brand.objects.create(name='Apple', code='AAPL')
        self.cat = LaptopCategory.objects.create(name='Ultrabook', slug='ultra')
        self.cpu = ProcessorSpec.objects.create(brand='APPLE', model_name='M2')
        self.ram = RamSpec.objects.create(ram_type='UNIFIED', capacity_gb=8)
        self.storage = StorageSpec.objects.create(storage_type='NVME_SSD', capacity_gb=256)
        self.display = DisplaySpec.objects.create(size_inches=Decimal('13.6'), resolution='2560x1664')
        self.gpu = GpuSpec.objects.create(brand='APPLE', model_name='Apple GPU')

        self.model = LaptopModel.objects.create(
            brand=self.brand, category=self.cat, model_name='MacBook Air M2', model_number='MBA-M2-01',
            processor=self.cpu, ram=self.ram, storage=self.storage, display=self.display, gpu=self.gpu
        )
        self.unit = LaptopUnit.objects.create(laptop_model=self.model, serial_number='SN-MBA-9901', status='IN_WORKSHOP')
        self.part = ComponentItem.objects.create(brand=self.brand, component_type='BATTERY', part_number='BAT-MBA-M2', name='Replacement Battery', unit_cost=Decimal('80.00'))

    def test_repair_cost_recalculation(self):
        job = WorkshopJobCard.objects.create(job_number='JOB-101', unit=self.unit, assigned_technician=self.tech)
        JobCardPartRequisition.objects.create(job_card=job, component=self.part, quantity=1, unit_cost_at_repair=Decimal('80.00'))
        RepairLaborLog.objects.create(job_card=job, technician=self.tech, hours_spent=Decimal('2.0'), work_performed='Replaced battery and calibrated')

        total_cost = JobCardWorkflowService.recalculate_costs(job)
        self.assertEqual(job.total_parts_cost, Decimal('80.00'))
        self.assertEqual(job.total_labor_cost, Decimal('100.00'))
        self.assertEqual(total_cost, Decimal('180.00'))
