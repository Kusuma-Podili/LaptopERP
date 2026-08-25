from django.db import transaction
from decimal import Decimal
from ..models import PurchaseOrder


class PurchaseOrderService:
    @staticmethod
    def calculate_totals(po):
        total = Decimal('0.00')
        for item in po.items.all():
            total += item.quantity_ordered * item.unit_price
        po.total_amount = total
        po.save(update_fields=['total_amount'])
        return total
