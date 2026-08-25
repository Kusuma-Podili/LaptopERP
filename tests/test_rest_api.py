from django.test import TestCase
from rest_framework.test import APIClient
from decimal import Decimal
from core.models import User
from inventory.models import Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec, DisplaySpec, GpuSpec, LaptopModel, LaptopUnit


class RestAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='apiuser', email='api@erp.local', password='pwd')
        self.client.force_authenticate(user=self.user)

        self.brand = Brand.objects.create(name='Asus', code='ASUS')
        self.cat = LaptopCategory.objects.create(name='Gaming', slug='gaming')
        self.cpu = ProcessorSpec.objects.create(brand='AMD', model_name='Ryzen 9')
        self.ram = RamSpec.objects.create(ram_type='DDR5', capacity_gb=32)
        self.storage = StorageSpec.objects.create(storage_type='NVME_SSD', capacity_gb=1024)
        self.display = DisplaySpec.objects.create(size_inches=Decimal('15.6'), resolution='2560x1440')
        self.gpu = GpuSpec.objects.create(brand='NVIDIA', model_name='RTX 4070', is_dedicated=True, vram_gb=8)

        self.model = LaptopModel.objects.create(
            brand=self.brand, category=self.cat, model_name='ROG Zephyrus G16', model_number='ROG-G16-01',
            processor=self.cpu, ram=self.ram, storage=self.storage, display=self.display, gpu=self.gpu
        )
        self.unit = LaptopUnit.objects.create(laptop_model=self.model, serial_number='SN-ROG-5544', status='IN_STOCK')

    def test_api_laptop_units_endpoint(self):
        response = self.client.get('/api/v1/units/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['serial_number'], 'SN-ROG-5544')

    def test_api_models_endpoint(self):
        response = self.client.get('/api/v1/models/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['model_name'], 'ROG Zephyrus G16')
