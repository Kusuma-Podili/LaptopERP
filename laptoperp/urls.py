"""
LaptopERP Main URL Configuration.
Routes requests across all ERP sub-modules and API gateways.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('core:dashboard'), name='root'),
    path('core/', include('core.urls', namespace='core')),
    path('inventory/', include('inventory.urls', namespace='inventory')),
    path('warehouse/', include('warehouse.urls', namespace='warehouse')),
    path('procurement/', include('procurement.urls', namespace='procurement')),
    path('repairs/', include('repairs.urls', namespace='repairs')),
    path('sales/', include('sales.urls', namespace='sales')),
    path('warranty/', include('warranty.urls', namespace='warranty')),
    path('analytics/', include('analytics.urls', namespace='analytics')),
    path('api/v1/', include('api.urls', namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
