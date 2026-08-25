from django.db.models import Sum, Count, Avg
from decimal import Decimal
from sales.models import SalesOrder, Invoice
from inventory.models import LaptopUnit
from repairs.models import WorkshopJobCard
from warranty.models import RMATicket


class AnalyticsCalculationEngine:
    @staticmethod
    def get_executive_summary():
        total_revenue = Invoice.objects.filter(payment_status='PAID').aggregate(val=Sum('total_amount'))['val'] or Decimal('0.00')
        active_stock = LaptopUnit.objects.filter(status='IN_STOCK').count()
        in_repairs = WorkshopJobCard.objects.filter(status__in=['IN_DIAGNOSTICS', 'REPAIR_IN_PROGRESS', 'QA_TESTING']).count()
        open_rmas = RMATicket.objects.exclude(status__in=['CLOSED', 'REJECTED']).count()

        return {
            'total_revenue': total_revenue,
            'active_stock': active_stock,
            'in_repairs': in_repairs,
            'open_rmas': open_rmas,
        }
