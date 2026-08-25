from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('models/', views.LaptopModelListView.as_view(), name='model_list'),
    path('models/<uuid:pk>/', views.LaptopModelDetailView.as_view(), name='model_detail'),
    path('units/', views.LaptopUnitListView.as_view(), name='unit_list'),
    path('serial-lookup/', views.SerialLookupView.as_view(), name='serial_lookup'),
    path('valuation/', views.StockValuationView.as_view(), name='stock_valuation'),
]
