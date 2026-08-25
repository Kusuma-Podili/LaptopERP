from django.test import TestCase
from decimal import Decimal
from sales.services.currency_tax import CurrencyTaxComplianceEngine


class CurrencyAndVATTestCase(TestCase):
    def test_currency_conversion(self):
        converted = CurrencyTaxComplianceEngine.convert_currency(Decimal('100.00'), 'USD', 'USD')
        self.assertEqual(converted, Decimal('100.00'))

    def test_eu_vat_reverse_charge(self):
        res = CurrencyTaxComplianceEngine.evaluate_cross_border_vat('DE', is_business_client=True, has_valid_tax_id=True)
        self.assertTrue(res['exempt'])
        self.assertEqual(res['tax_rate'], Decimal('0.00'))
