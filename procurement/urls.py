from django.urls import path
from . import views

app_name = 'procurement'

urlpatterns = [
    path('suppliers/', views.SupplierListView.as_view(), name='supplier_list'),
    path('orders/', views.PurchaseOrderListView.as_view(), name='po_list'),
    path('orders/<uuid:pk>/', views.PurchaseOrderDetailView.as_view(), name='po_detail'),
]
