from django.utils import timezone
from ..models import ProductWarrantyRegistration, RMATicket


class WarrantyValidationService:
    @staticmethod
    def is_unit_under_warranty(unit):
        today = timezone.now().date()
        return ProductWarrantyRegistration.objects.filter(
            unit=unit,
            start_date__lte=today,
            end_date__gte=today,
            is_active=True
        ).exists()
