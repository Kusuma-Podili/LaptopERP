from django.test import TestCase
from decimal import Decimal
from sales.services.bulk_discounts import BulkDiscountEngine


class BulkDiscountTestCase(TestCase):
    def test_volume_discount_tier(self):
        res = BulkDiscountEngine.calculate_volume_pricing(Decimal("1000.00"), 50, "STANDARD")
        self.assertEqual(res["discount_percentage"], Decimal("10.00"))
        self.assertEqual(res["effective_unit_price"], Decimal("900.00"))
        self.assertEqual(res["total_order_value"], Decimal("45000.00"))
