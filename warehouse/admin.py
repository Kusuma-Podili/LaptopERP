from django.contrib import admin
from .models import Warehouse, Zone, Bin, StockTransferOrder, StockTransferItem, CycleCount

admin.site.register(Warehouse)
admin.site.register(Zone)
admin.site.register(Bin)
admin.site.register(StockTransferOrder)
admin.site.register(StockTransferItem)
admin.site.register(CycleCount)
