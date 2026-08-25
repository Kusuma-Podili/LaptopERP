"""
Stock Valuation and Reorder Services for Hardware Inventory.
"""

from django.db.models import Sum, F, Count, Avg
from decimal import Decimal
from ..models import LaptopUnit, LaptopModel, ComponentItem


class StockService:
    @staticmethod
    def get_inventory_summary():
        total_units = LaptopUnit.objects.count()
        in_stock_units = LaptopUnit.objects.filter(status='IN_STOCK').count()
        in_workshop = LaptopUnit.objects.filter(status='IN_WORKSHOP').count()
        total_valuation = LaptopUnit.objects.filter(status__in=['IN_STOCK', 'IN_WORKSHOP', 'RESERVED']).aggregate(
            val=Sum('purchase_price')
        )['val'] or Decimal('0.00')

        return {
            'total_units': total_units,
            'in_stock_units': in_stock_units,
            'in_workshop': in_workshop,
            'total_valuation': total_valuation,
        }

    @staticmethod
    def get_low_stock_alerts():
        low_models = []
        for model in LaptopModel.objects.all():
            stock = model.current_in_stock_count
            if stock <= model.minimum_stock_threshold:
                low_models.append({
                    'model': model,
                    'current_stock': stock,
                    'threshold': model.minimum_stock_threshold,
                })
        return low_models
