from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('orders/', views.SalesOrderListView.as_view(), name='order_list'),
    path('invoices/<uuid:pk>/', views.InvoiceDetailView.as_view(), name='invoice_detail'),
]
