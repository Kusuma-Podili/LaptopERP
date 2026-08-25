from django.test import TestCase
from decimal import Decimal
from django.utils import timezone
from procurement.models import Supplier, PurchaseOrder, PurchaseOrderItem
from procurement.services.po import PurchaseOrderService
from inventory.models import Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec, DisplaySpec, GpuSpec, LaptopModel


class ProcurementWorkflowTestCase(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(code='SUP-01', company_name='Global Distro', email='info@distro.com', phone='1234')
        self.brand = Brand.objects.create(name='Lenovo', code='LEN')
        self.cat = LaptopCategory.objects.create(name='Business', slug='biz')
        self.cpu = ProcessorSpec.objects.create(brand='INTEL', model_name='i5-1340P')
        self.ram = RamSpec.objects.create(ram_type='DDR4', capacity_gb=8)
        self.storage = StorageSpec.objects.create(storage_type='NVME_SSD', capacity_gb=256)
        self.display = DisplaySpec.objects.create(size_inches=Decimal('14.0'), resolution='1920x1080')
        self.gpu = GpuSpec.objects.create(brand='INTEL', model_name='Iris')

        self.model = LaptopModel.objects.create(
            brand=self.brand, category=self.cat, model_name='ThinkPad E14', model_number='TP-E14-01',
            processor=self.cpu, ram=self.ram, storage=self.storage, display=self.display, gpu=self.gpu
        )

    def test_po_calculation(self):
        po = PurchaseOrder.objects.create(po_number='PO-TEST-01', supplier=self.supplier, order_date=timezone.now().date())
        PurchaseOrderItem.objects.create(purchase_order=po, laptop_model=self.model, quantity_ordered=5, unit_price=Decimal('600.00'))
        
        total = PurchaseOrderService.calculate_totals(po)
        self.assertEqual(total, Decimal('3000.00'))
        self.assertEqual(po.total_amount, Decimal('3000.00'))
