from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from core.models import User
from inventory.models import Brand, LaptopModel, LaptopUnit, ComponentItem
from warehouse.models import Warehouse, StockTransferOrder
from procurement.models import Supplier, PurchaseOrder
from repairs.models import WorkshopJobCard
from sales.models import Customer, SalesOrder, Invoice
from warranty.models import RMATicket

from .serializers import (
    UserSerializer, BrandSerializer, LaptopModelSerializer, LaptopUnitSerializer,
    WarehouseSerializer, SupplierSerializer, PurchaseOrderSerializer,
    WorkshopJobCardSerializer, CustomerSerializer, SalesOrderSerializer,
    InvoiceSerializer, RMATicketSerializer
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'employee_id']


class LaptopModelViewSet(viewsets.ModelViewSet):
    queryset = LaptopModel.objects.all()
    serializer_class = LaptopModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['brand', 'category']
    search_fields = ['model_name', 'model_number']


class LaptopUnitViewSet(viewsets.ModelViewSet):
    queryset = LaptopUnit.objects.all()
    serializer_class = LaptopUnitSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'condition_grade']
    search_fields = ['serial_number', 'barcode']


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkshopJobCardViewSet(viewsets.ModelViewSet):
    queryset = WorkshopJobCard.objects.all()
    serializer_class = WorkshopJobCardSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class RMATicketViewSet(viewsets.ModelViewSet):
    queryset = RMATicket.objects.all()
    serializer_class = RMATicketSerializer
    permission_classes = [permissions.IsAuthenticated]
