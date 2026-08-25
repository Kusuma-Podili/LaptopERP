from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [
    path('', views.WarehouseListView.as_view(), name='warehouse_list'),
    path('<uuid:pk>/bins/', views.BinMapView.as_view(), name='bin_map'),
    path('transfers/', views.TransferOrderListView.as_view(), name='transfer_orders'),
    path('cycle-counts/', views.CycleCountListView.as_view(), name='cycle_counts'),
]
