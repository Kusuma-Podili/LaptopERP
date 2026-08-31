from django.test import TestCase
from procurement.services.supplier_ranking import SupplierPerformanceMatrixEngine


class SupplierRankingTestCase(TestCase):
    def test_vendor_tier_calculation(self):
        res = SupplierPerformanceMatrixEngine.calculate_vendor_grade(98.0, 200, 95.0)
        self.assertGreaterEqual(res["composite_score"], 85.0)
        self.assertIn(res["tier"], ["PREFERRED_PARTNER", "APPROVED"])
