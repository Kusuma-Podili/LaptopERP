from django.urls import path
from . import views

app_name = 'warranty'

urlpatterns = [
    path('lookup/', views.WarrantyLookupView.as_view(), name='warranty_lookup'),
    path('rma/', views.RMATicketListView.as_view(), name='rma_list'),
]
