from decimal import Decimal
from ..models import TaxRule


class TaxCalculationEngine:
    @staticmethod
    def calculate_tax(subtotal, tax_rate=18.00):
        rate = Decimal(str(tax_rate))
        tax_amount = (subtotal * rate) / Decimal('100.00')
        total = subtotal + tax_amount
        return tax_amount, total
