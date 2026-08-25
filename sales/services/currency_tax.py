"""
Multi-Currency Exchange and Cross-Border VAT Exemption Engine.
Supports dynamic currency conversion rates and international tax rules.
"""

from decimal import Decimal
from typing import Dict


class CurrencyTaxComplianceEngine:
    EXCHANGE_RATES_TO_USD = {
        'USD': Decimal('1.0000'),
        'EUR': Decimal('1.0850'),
        'GBP': Decimal('1.2720'),
        'CAD': Decimal('0.7420'),
        'AUD': Decimal('0.6550'),
        'JPY': Decimal('0.0067'),
    }

    @classmethod
    def convert_currency(cls, amount: Decimal, from_curr: str, to_curr: str) -> Decimal:
        from_rate = cls.EXCHANGE_RATES_TO_USD.get(from_curr.upper(), Decimal('1.0000'))
        to_rate = cls.EXCHANGE_RATES_TO_USD.get(to_curr.upper(), Decimal('1.0000'))
        
        amount_usd = amount * from_rate
        converted = amount_usd / to_rate
        return round(converted, 2)

    @staticmethod
    def evaluate_cross_border_vat(country_code: str, is_business_client: bool, has_valid_tax_id: bool) -> Dict[str, any]:
        # EU B2B Reverse Charge
        eu_countries = {'DE', 'FR', 'IT', 'ES', 'NL', 'BE', 'PL', 'SE', 'AT', 'IE'}
        is_eu = country_code.upper() in eu_countries

        if is_eu and is_business_client and has_valid_tax_id:
            return {
                'tax_treatment': 'EU_B2B_REVERSE_CHARGE',
                'tax_rate': Decimal('0.00'),
                'exempt': True,
                'invoice_note': 'Reverse charge applies according to Article 196 of EU VAT Directive 2006/112/EC.',
            }
        
        return {
            'tax_treatment': 'STANDARD_DOMESTIC',
            'tax_rate': Decimal('18.00'),
            'exempt': False,
            'invoice_note': 'Standard tax rate applied.',
        }
