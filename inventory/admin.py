from django.contrib import admin
from .models import (
    Brand, LaptopCategory, ProcessorSpec, RamSpec, StorageSpec, DisplaySpec, GpuSpec,
    LaptopModel, LaptopUnit, SerialLifecycleHistory, ComponentItem, ComponentCompatibility
)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'country_of_origin']
    search_fields = ['name', 'code']


@admin.register(LaptopModel)
class LaptopModelAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'brand', 'model_number', 'processor', 'ram', 'storage', 'current_in_stock_count']
    list_filter = ['brand', 'category']
    search_fields = ['model_name', 'model_number']


@admin.register(LaptopUnit)
class LaptopUnitAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'laptop_model', 'status', 'condition_grade', 'current_location', 'purchase_price']
    list_filter = ['status', 'condition_grade', 'laptop_model__brand']
    search_fields = ['serial_number', 'barcode', 'laptop_model__model_name']


admin.site.register(LaptopCategory)
admin.site.register(ProcessorSpec)
admin.site.register(RamSpec)
admin.site.register(StorageSpec)
admin.site.register(DisplaySpec)
admin.site.register(GpuSpec)
admin.site.register(SerialLifecycleHistory)
admin.site.register(ComponentItem)
admin.site.register(ComponentCompatibility)
