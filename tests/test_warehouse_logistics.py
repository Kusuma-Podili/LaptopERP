from django.test import TestCase
from decimal import Decimal
from core.models import User, CompanyProfile, Branch
from warehouse.models import Warehouse, Zone, Bin, StockTransferOrder, StockTransferItem
from warehouse.services.transfer import StockTransferService
from inventory.models import Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec, DisplaySpec, GpuSpec, LaptopModel, LaptopUnit


class WarehouseTransferTestCase(TestCase):
    def setUp(self):
        self.company = CompanyProfile.objects.create(name='Test Company')
        self.branch = Branch.objects.create(company=self.company, code='B1', name='Branch 1', city='City', state='State')
        self.user = User.objects.create_user(username='warehouse_op', email='wh@erp.local', password='pwd')
        
        self.wh_source = Warehouse.objects.create(branch=self.branch, code='WH-SRC', name='Source WH')
        self.wh_dest = Warehouse.objects.create(branch=self.branch, code='WH-DST', name='Dest WH')
        
        self.brand = Brand.objects.create(name='HP', code='HP')
        self.cat = LaptopCategory.objects.create(name='Business', slug='biz')
        self.cpu = ProcessorSpec.objects.create(brand='AMD', model_name='Ryzen 7')
        self.ram = RamSpec.objects.create(ram_type='DDR5', capacity_gb=16)
        self.storage = StorageSpec.objects.create(storage_type='NVME_SSD', capacity_gb=512)
        self.display = DisplaySpec.objects.create(size_inches=Decimal('15.6'), resolution='1920x1080')
        self.gpu = GpuSpec.objects.create(brand='AMD', model_name='Radeon')

        self.model = LaptopModel.objects.create(
            brand=self.brand, category=self.cat, model_name='EliteBook 840', model_number='HP-840-G9',
            processor=self.cpu, ram=self.ram, storage=self.storage, display=self.display, gpu=self.gpu
        )
        self.unit = LaptopUnit.objects.create(laptop_model=self.model, serial_number='SN-HP-1122', status='IN_STOCK')

    def test_inter_warehouse_transfer_workflow(self):
        order = StockTransferOrder.objects.create(
            transfer_number='TRF-2026-01',
            source_warehouse=self.wh_source,
            destination_warehouse=self.wh_dest,
            initiated_by=self.user
        )
        StockTransferItem.objects.create(transfer_order=order, unit=self.unit)
        
        StockTransferService.dispatch_transfer(order, self.user)
        order.refresh_from_db()
        self.assertEqual(order.status, 'IN_TRANSIT')

        StockTransferService.receive_transfer(order, self.user)
        order.refresh_from_db()
        self.assertEqual(order.status, 'RECEIVED')
        self.assertTrue(order.items.first().is_received)
