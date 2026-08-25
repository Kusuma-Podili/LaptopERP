from django.test import TestCase
from decimal import Decimal
from django.utils import timezone
from core.models import User
from sales.models import Customer, SalesOrder, SalesOrderItem, Invoice
from sales.services.tax import TaxCalculationEngine
from sales.services.invoice import InvoicingService
from inventory.models import Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec, DisplaySpec, GpuSpec, LaptopModel


class SalesAndTaxTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(customer_number='C-01', name='Enterprise Client Corp', email='corp@client.com', phone='555')
        self.brand = Brand.objects.create(name='Dell', code='DELL')
        self.cat = LaptopCategory.objects.create(name='Business', slug='biz')
        self.cpu = ProcessorSpec.objects.create(brand='INTEL', model_name='i7')
        self.ram = RamSpec.objects.create(ram_type='DDR5', capacity_gb=16)
        self.storage = StorageSpec.objects.create(storage_type='NVME_SSD', capacity_gb=512)
        self.display = DisplaySpec.objects.create(size_inches=Decimal('14.0'), resolution='1920x1080')
        self.gpu = GpuSpec.objects.create(brand='INTEL', model_name='Iris')

        self.model = LaptopModel.objects.create(
            brand=self.brand, category=self.cat, model_name='Latitude 7420', model_number='LAT-7420',
            processor=self.cpu, ram=self.ram, storage=self.storage, display=self.display, gpu=self.gpu
        )

    def test_tax_computation_and_invoicing(self):
        tax_amt, total = TaxCalculationEngine.calculate_tax(Decimal('1000.00'), tax_rate=18.00)
        self.assertEqual(tax_amt, Decimal('180.00'))
        self.assertEqual(total, Decimal('1180.00'))

        order = SalesOrder.objects.create(order_number='SO-TEST-01', customer=self.customer, order_date=timezone.now().date())
        invoice = Invoice.objects.create(
            invoice_number='INV-TEST-01',
            sales_order=order,
            customer=self.customer,
            issue_date=timezone.now().date(),
            due_date=timezone.now().date(),
            subtotal=Decimal('1000.00'),
            tax_amount=Decimal('180.00'),
            total_amount=Decimal('1180.00')
        )
        
        payment = InvoicingService.record_payment(invoice, Decimal('1180.00'), 'BANK_WIRE', 'TXN-998811')
        invoice.refresh_from_db()
        self.assertEqual(invoice.payment_status, 'PAID')
        self.assertEqual(invoice.amount_paid, Decimal('1180.00'))
