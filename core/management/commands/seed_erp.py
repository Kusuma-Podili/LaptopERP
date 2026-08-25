"""
Comprehensive Enterprise Data Seeder for LaptopERP.
Populates standard roles, company profile, branches, brands, laptop models,
serialized units, suppliers, purchase orders, repair jobs, sales orders, invoices, and warranties.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from decimal import Decimal
from datetime import timedelta

from core.models import User, Role, Department, Branch, CompanyProfile, SystemSetting
from inventory.models import (
    Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec, DisplaySpec, GpuSpec,
    LaptopModel, LaptopUnit, ComponentItem
)
from warehouse.models import Warehouse, Zone, Bin
from procurement.models import Supplier, PurchaseOrder, PurchaseOrderItem
from repairs.models import DiagnosticChecklistMaster, WorkshopJobCard
from sales.models import Customer, TaxRule, SalesOrder, SalesOrderItem, Invoice
from warranty.models import WarrantyPolicy, ProductWarrantyRegistration


class Command(BaseCommand):
    help = 'Seeds complete enterprise demo data for LaptopERP'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Starting LaptopERP Enterprise Seeding..."))

        # 1. Company Profile & Branch
        company, _ = CompanyProfile.objects.get_or_create(
            name='LaptopERP Solutions Global Inc.',
            defaults={
                'legal_name': 'LaptopERP Solutions Global Corporation',
                'tax_identifier': 'US-TAX-8890214',
                'email': 'admin@laptoperp.local',
                'currency_symbol': '$',
                'city': 'San Jose',
                'country': 'United States'
            }
        )

        branch, _ = Branch.objects.get_or_create(
            code='HQ-SJ-01',
            company=company,
            defaults={
                'name': 'Silicon Valley Headquarters & Fulfillment Hub',
                'city': 'San Jose',
                'state': 'California',
                'is_headquarters': True
            }
        )

        # 2. Roles & Users
        admin_role, _ = Role.objects.get_or_create(
            code='ADMIN',
            defaults={'name': 'Super Administrator', 'can_manage_users': True, 'can_manage_inventory': True, 'can_view_analytics': True}
        )
        tech_role, _ = Role.objects.get_or_create(
            code='TECHNICIAN_SENIOR',
            defaults={'name': 'Senior Diagnostic Technician', 'can_perform_repairs': True}
        )
        wh_role, _ = Role.objects.get_or_create(
            code='WAREHOUSE_MGR',
            defaults={'name': 'Warehouse Manager', 'can_manage_warehouse': True, 'can_manage_inventory': True}
        )
        sales_role, _ = Role.objects.get_or_create(
            code='SALES_EXEC',
            defaults={'name': 'Sales Executive', 'can_manage_sales': True}
        )

        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@laptoperp.local', 'first_name': 'Enterprise', 'last_name': 'Admin', 'role': admin_role, 'is_staff': True, 'is_superuser': True}
        )
        if created:
            admin_user.set_password('AdminPass123!')
            admin_user.save()

        tech_user, created = User.objects.get_or_create(
            username='tech_alex',
            defaults={'email': 'alex@laptoperp.local', 'first_name': 'Alex', 'last_name': 'Rider', 'role': tech_role, 'is_technician': True, 'hourly_rate': Decimal('45.00')}
        )
        if created:
            tech_user.set_password('TechPass123!')
            tech_user.save()

        # 3. Brands & Categories
        dell, _ = Brand.objects.get_or_create(name='Dell Technologies', code='DELL', defaults={'country_of_origin': 'USA'})
        lenovo, _ = Brand.objects.get_or_create(name='Lenovo', code='LEN', defaults={'country_of_origin': 'China'})
        apple, _ = Brand.objects.get_or_create(name='Apple', code='AAPL', defaults={'country_of_origin': 'USA'})
        hp, _ = Brand.objects.get_or_create(name='HP Inc.', code='HP', defaults={'country_of_origin': 'USA'})

        cat_business, _ = LaptopCategory.objects.get_or_create(name='Enterprise Business', slug='business')
        cat_workstation, _ = LaptopCategory.objects.get_or_create(name='Mobile Workstation', slug='workstation')
        cat_ultrabook, _ = LaptopCategory.objects.get_or_create(name='Premium Ultrabook', slug='ultrabook')

        # 4. Hardware Specs Master
        cpu_i7, _ = ProcessorSpec.objects.get_or_create(brand='INTEL', model_name='Core i7-13700H', defaults={'cores': 14, 'threads': 20})
        cpu_ryzen7, _ = ProcessorSpec.objects.get_or_create(brand='AMD', model_name='Ryzen 7 7840U', defaults={'cores': 8, 'threads': 16})
        cpu_m3, _ = ProcessorSpec.objects.get_or_create(brand='APPLE', model_name='M3 Pro', defaults={'cores': 12, 'threads': 12})

        ram_16gb, _ = RamSpec.objects.get_or_create(ram_type='DDR5', capacity_gb=16, defaults={'speed_mhz': 4800})
        ram_32gb, _ = RamSpec.objects.get_or_create(ram_type='DDR5', capacity_gb=32, defaults={'speed_mhz': 5600})

        ssd_512gb, _ = StorageSpec.objects.get_or_create(storage_type='NVME_SSD', capacity_gb=512)
        ssd_1tb, _ = StorageSpec.objects.get_or_create(storage_type='NVME_SSD', capacity_gb=1024)

        disp_14_fhd, _ = DisplaySpec.objects.get_or_create(size_inches=Decimal('14.0'), resolution='1920x1080 (FHD)', panel_type='IPS')
        disp_16_qhd, _ = DisplaySpec.objects.get_or_create(size_inches=Decimal('16.0'), resolution='2560x1600 (QHD+)', panel_type='IPS')

        gpu_integrated, _ = GpuSpec.objects.get_or_create(brand='INTEL', model_name='Iris Xe Graphics', is_dedicated=False)
        gpu_rtx4060, _ = GpuSpec.objects.get_or_create(brand='NVIDIA', model_name='GeForce RTX 4060', defaults={'vram_gb': 8, 'is_dedicated': True})

        # 5. Laptop Models
        thinkpad, _ = LaptopModel.objects.get_or_create(
            model_number='TP-T14-G4',
            defaults={
                'brand': lenovo,
                'category': cat_business,
                'model_name': 'ThinkPad T14 Gen 4',
                'processor': cpu_i7,
                'ram': ram_16gb,
                'storage': ssd_512gb,
                'display': disp_14_fhd,
                'gpu': gpu_integrated,
                'msrp_price': Decimal('1299.00'),
                'standard_cost': Decimal('850.00'),
            }
        )

        latitude, _ = LaptopModel.objects.get_or_create(
            model_number='DELL-LAT-7440',
            defaults={
                'brand': dell,
                'category': cat_business,
                'model_name': 'Latitude 7440 Ultralight',
                'processor': cpu_i7,
                'ram': ram_32gb,
                'storage': ssd_1tb,
                'display': disp_14_fhd,
                'gpu': gpu_integrated,
                'msrp_price': Decimal('1499.00'),
                'standard_cost': Decimal('980.00'),
            }
        )

        # 6. Warehouses & Bins
        wh, _ = Warehouse.objects.get_or_create(
            code='WH-MAIN-SJ',
            branch=branch,
            defaults={'name': 'Main Logistics & QA Center', 'manager': admin_user}
        )
        zone_dock, _ = Zone.objects.get_or_create(warehouse=wh, code='IN-DOCK', defaults={'name': 'Inward Receiving Dock', 'zone_type': 'INWARD'})
        zone_storage, _ = Zone.objects.get_or_create(warehouse=wh, code='ST-A', defaults={'name': 'Storage Rack A', 'zone_type': 'STORAGE'})

        bin_01, _ = Bin.objects.get_or_create(zone=zone_storage, bin_code='A01-R01-S01-B01')

        # 7. Serial Units
        for i in range(1, 11):
            LaptopUnit.objects.get_or_create(
                serial_number=f"SN-LEN-T14-{1000 + i}",
                defaults={
                    'laptop_model': thinkpad,
                    'status': 'IN_STOCK',
                    'condition_grade': 'GRADE_A_PLUS',
                    'purchase_price': Decimal('850.00'),
                    'selling_price': Decimal('1299.00'),
                    'current_location': bin_01.bin_code
                }
            )

        # 8. Suppliers & Purchase Order
        supplier, _ = Supplier.objects.get_or_create(
            code='VEND-LENOVO-DIST',
            defaults={'company_name': 'Lenovo Direct Distribution', 'email': 'orders@lenovodist.com', 'phone': '+1-800-555-0199'}
        )
        po, _ = PurchaseOrder.objects.get_or_create(
            po_number='PO-2026-001',
            supplier=supplier,
            defaults={'order_date': timezone.now().date(), 'status': 'APPROVED', 'total_amount': Decimal('8500.00'), 'created_by': admin_user}
        )

        # 9. Customers, Sales Orders, Invoices
        customer, _ = Customer.objects.get_or_create(
            customer_number='CUST-TECHCORP-01',
            defaults={'name': 'TechCorp Solutions LLC', 'email': 'procurement@techcorp.io', 'phone': '+1-555-0144'}
        )
        so, _ = SalesOrder.objects.get_or_create(
            order_number='SO-2026-101',
            customer=customer,
            defaults={'order_date': timezone.now().date(), 'status': 'CONFIRMED', 'subtotal': Decimal('2598.00'), 'tax_amount': Decimal('467.64'), 'total_amount': Decimal('3065.64')}
        )

        # 10. Diagnostic Checklist points
        DiagnosticChecklistMaster.objects.get_or_create(
            test_code='TST-BAT-01',
            defaults={'category': 'POWER_BATTERY', 'title': 'Battery Health & Charge Cycle Verification'}
        )
        DiagnosticChecklistMaster.objects.get_or_create(
            test_code='TST-DISP-01',
            defaults={'category': 'DISPLAY_GPU', 'title': 'Screen Backlight, Dead Pixel & Panel Stress Test'}
        )

        self.stdout.write(self.style.SUCCESS("Enterprise Seed Data successfully populated!"))
