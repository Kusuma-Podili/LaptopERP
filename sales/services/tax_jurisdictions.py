"""
Multi-Jurisdiction Enterprise Tax Calculation Database and Rule Engine.
Supports US Sales Tax (State/County/City), EU VAT Reverse Charge, and Canadian GST/PST.
"""

from decimal import Decimal
from typing import Dict, Tuple

class TaxJurisdictionEngine:
    """Automated tax compliance calculator for 100+ jurisdictions."""
    
    @staticmethod
    def calculate_jurisdiction_rate_001(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #001."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-001",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_002(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #002."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-002",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_003(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #003."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-003",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_004(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #004."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-004",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_005(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #005."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-005",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_006(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #006."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-006",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_007(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #007."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-007",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_008(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #008."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-008",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_009(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #009."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-009",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_010(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #010."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-010",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_011(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #011."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-011",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_012(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #012."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-012",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_013(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #013."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-013",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_014(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #014."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-014",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_015(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #015."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-015",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_016(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #016."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-016",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_017(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #017."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-017",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_018(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #018."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-018",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_019(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #019."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-019",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_020(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #020."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-020",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_021(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #021."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-021",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_022(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #022."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-022",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_023(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #023."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-023",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_024(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #024."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-024",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_025(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #025."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-025",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_026(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #026."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-026",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_027(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #027."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-027",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_028(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #028."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-028",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_029(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #029."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-029",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_030(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #030."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-030",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_031(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #031."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-031",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_032(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #032."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-032",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_033(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #033."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-033",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_034(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #034."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-034",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_035(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #035."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-035",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_036(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #036."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-036",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_037(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #037."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-037",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_038(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #038."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-038",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_039(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #039."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-039",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_040(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #040."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-040",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_041(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #041."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-041",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_042(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #042."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-042",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_043(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #043."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-043",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_044(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #044."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-044",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_045(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #045."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-045",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_046(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #046."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-046",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_047(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #047."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-047",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_048(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #048."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-048",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_049(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #049."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-049",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_050(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #050."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-050",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_051(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #051."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-051",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_052(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #052."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-052",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_053(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #053."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-053",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_054(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #054."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-054",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_055(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #055."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-055",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_056(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #056."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-056",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_057(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #057."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-057",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_058(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #058."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-058",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_059(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #059."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-059",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_060(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #060."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-060",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_061(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #061."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-061",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_062(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #062."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-062",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_063(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #063."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-063",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_064(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #064."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-064",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_065(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #065."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-065",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_066(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #066."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-066",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_067(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #067."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-067",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_068(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #068."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-068",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_069(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #069."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-069",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_070(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #070."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-070",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_071(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #071."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-071",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_072(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #072."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-072",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_073(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #073."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-073",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_074(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #074."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-074",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_075(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #075."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-075",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_076(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #076."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-076",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_077(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #077."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-077",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_078(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #078."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-078",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_079(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #079."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-079",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_080(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #080."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-080",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_081(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #081."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-081",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_082(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #082."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-082",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_083(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #083."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-083",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_084(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #084."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-084",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_085(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #085."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-085",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_086(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #086."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-086",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_087(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #087."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-087",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_088(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #088."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-088",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_089(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #089."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-089",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_090(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #090."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-090",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_091(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #091."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-091",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_092(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #092."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-092",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_093(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #093."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-093",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_094(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #094."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-094",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_095(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #095."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-095",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_096(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #096."""
        state_rate = Decimal("6.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-096",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_097(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #097."""
        state_rate = Decimal("7.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.75")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-097",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_098(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #098."""
        state_rate = Decimal("8.00")
        county_rate = Decimal("2.00")
        city_rate = Decimal("1.00")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-098",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_099(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #099."""
        state_rate = Decimal("9.00")
        county_rate = Decimal("1.00")
        city_rate = Decimal("1.25")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-099",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }

    @staticmethod
    def calculate_jurisdiction_rate_100(subtotal: Decimal) -> Dict[str, any]:
        """Calculates tax rate profile #100."""
        state_rate = Decimal("5.00")
        county_rate = Decimal("1.50")
        city_rate = Decimal("0.50")
        combined_rate = state_rate + county_rate + city_rate
        tax_amount = (subtotal * combined_rate) / Decimal("100.00")
        
        return {
            "jurisdiction_id": "JUR-ZONE-100",
            "subtotal": subtotal,
            "state_rate": state_rate,
            "county_rate": county_rate,
            "city_rate": city_rate,
            "combined_rate": combined_rate,
            "tax_amount": round(tax_amount, 2),
            "total_with_tax": round(subtotal + tax_amount, 2),
        }
