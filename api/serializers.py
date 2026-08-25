from rest_framework import serializers
from core.models import User, CompanyProfile, AuditLog
from inventory.models import Brand, LaptopModel, LaptopUnit, ComponentItem
from warehouse.models import Warehouse, Zone, Bin, StockTransferOrder
from procurement.models import Supplier, PurchaseOrder
from repairs.models import WorkshopJobCard, DiagnosticResult
from sales.models import Customer, SalesOrder, Invoice
from warranty.models import WarrantyPolicy, ProductWarrantyRegistration, RMATicket


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'employee_id', 'is_technician']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class LaptopModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = LaptopModel
        fields = '__all__'


class LaptopUnitSerializer(serializers.ModelSerializer):
    model_name = serializers.CharField(source='laptop_model.model_name', read_only=True)

    class Meta:
        model = LaptopUnit
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.company_name', read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class WorkshopJobCardSerializer(serializers.ModelSerializer):
    serial_number = serializers.CharField(source='unit.serial_number', read_only=True)

    class Meta:
        model = WorkshopJobCard
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SalesOrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = SalesOrder
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class RMATicketSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    serial_number = serializers.CharField(source='unit.serial_number', read_only=True)

    class Meta:
        model = RMATicket
        fields = '__all__'
