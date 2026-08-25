from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserViewSet, LaptopModelViewSet, LaptopUnitViewSet,
    WarehouseViewSet, SupplierViewSet, PurchaseOrderViewSet,
    WorkshopJobCardViewSet, CustomerViewSet, SalesOrderViewSet,
    InvoiceViewSet, RMATicketViewSet
)

app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'models', LaptopModelViewSet)
router.register(r'units', LaptopUnitViewSet)
router.register(r'warehouses', WarehouseViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'purchase-orders', PurchaseOrderViewSet)
router.register(r'job-cards', WorkshopJobCardViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales-orders', SalesOrderViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'rma-tickets', RMATicketViewSet)

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
