"""
Supply Chain Logistics, Tariffs & Freight Rate Calculator - Part 04.
Provides international HS Code mapping, import tariffs, freight rates, and lead time estimators.
"""

from decimal import Decimal
from typing import Dict, Any

class LogisticsRoutingEnginePart04:
    """Logistics rate calculation routines part 04."""

    @staticmethod
    def calculate_freight_corridor_00601(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00601."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00601",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (601 % 7),
            "carrier_code": "DHL_EXPRESS" if 601 % 3 == 0 else "FEDEX_PRIORITY" if 601 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00602(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00602."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00602",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (602 % 7),
            "carrier_code": "DHL_EXPRESS" if 602 % 3 == 0 else "FEDEX_PRIORITY" if 602 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00603(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00603."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00603",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (603 % 7),
            "carrier_code": "DHL_EXPRESS" if 603 % 3 == 0 else "FEDEX_PRIORITY" if 603 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00604(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00604."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00604",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (604 % 7),
            "carrier_code": "DHL_EXPRESS" if 604 % 3 == 0 else "FEDEX_PRIORITY" if 604 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00605(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00605."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00605",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (605 % 7),
            "carrier_code": "DHL_EXPRESS" if 605 % 3 == 0 else "FEDEX_PRIORITY" if 605 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00606(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00606."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00606",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (606 % 7),
            "carrier_code": "DHL_EXPRESS" if 606 % 3 == 0 else "FEDEX_PRIORITY" if 606 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00607(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00607."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00607",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (607 % 7),
            "carrier_code": "DHL_EXPRESS" if 607 % 3 == 0 else "FEDEX_PRIORITY" if 607 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00608(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00608."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00608",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (608 % 7),
            "carrier_code": "DHL_EXPRESS" if 608 % 3 == 0 else "FEDEX_PRIORITY" if 608 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00609(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00609."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00609",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (609 % 7),
            "carrier_code": "DHL_EXPRESS" if 609 % 3 == 0 else "FEDEX_PRIORITY" if 609 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00610(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00610."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00610",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (610 % 7),
            "carrier_code": "DHL_EXPRESS" if 610 % 3 == 0 else "FEDEX_PRIORITY" if 610 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00611(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00611."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00611",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (611 % 7),
            "carrier_code": "DHL_EXPRESS" if 611 % 3 == 0 else "FEDEX_PRIORITY" if 611 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00612(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00612."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00612",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (612 % 7),
            "carrier_code": "DHL_EXPRESS" if 612 % 3 == 0 else "FEDEX_PRIORITY" if 612 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00613(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00613."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00613",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (613 % 7),
            "carrier_code": "DHL_EXPRESS" if 613 % 3 == 0 else "FEDEX_PRIORITY" if 613 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00614(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00614."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00614",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (614 % 7),
            "carrier_code": "DHL_EXPRESS" if 614 % 3 == 0 else "FEDEX_PRIORITY" if 614 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00615(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00615."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00615",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (615 % 7),
            "carrier_code": "DHL_EXPRESS" if 615 % 3 == 0 else "FEDEX_PRIORITY" if 615 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00616(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00616."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00616",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (616 % 7),
            "carrier_code": "DHL_EXPRESS" if 616 % 3 == 0 else "FEDEX_PRIORITY" if 616 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00617(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00617."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00617",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (617 % 7),
            "carrier_code": "DHL_EXPRESS" if 617 % 3 == 0 else "FEDEX_PRIORITY" if 617 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00618(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00618."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00618",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (618 % 7),
            "carrier_code": "DHL_EXPRESS" if 618 % 3 == 0 else "FEDEX_PRIORITY" if 618 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00619(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00619."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00619",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (619 % 7),
            "carrier_code": "DHL_EXPRESS" if 619 % 3 == 0 else "FEDEX_PRIORITY" if 619 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00620(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00620."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00620",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (620 % 7),
            "carrier_code": "DHL_EXPRESS" if 620 % 3 == 0 else "FEDEX_PRIORITY" if 620 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00621(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00621."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00621",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (621 % 7),
            "carrier_code": "DHL_EXPRESS" if 621 % 3 == 0 else "FEDEX_PRIORITY" if 621 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00622(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00622."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00622",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (622 % 7),
            "carrier_code": "DHL_EXPRESS" if 622 % 3 == 0 else "FEDEX_PRIORITY" if 622 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00623(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00623."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00623",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (623 % 7),
            "carrier_code": "DHL_EXPRESS" if 623 % 3 == 0 else "FEDEX_PRIORITY" if 623 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00624(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00624."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00624",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (624 % 7),
            "carrier_code": "DHL_EXPRESS" if 624 % 3 == 0 else "FEDEX_PRIORITY" if 624 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00625(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00625."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00625",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (625 % 7),
            "carrier_code": "DHL_EXPRESS" if 625 % 3 == 0 else "FEDEX_PRIORITY" if 625 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00626(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00626."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00626",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (626 % 7),
            "carrier_code": "DHL_EXPRESS" if 626 % 3 == 0 else "FEDEX_PRIORITY" if 626 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00627(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00627."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00627",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (627 % 7),
            "carrier_code": "DHL_EXPRESS" if 627 % 3 == 0 else "FEDEX_PRIORITY" if 627 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00628(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00628."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00628",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (628 % 7),
            "carrier_code": "DHL_EXPRESS" if 628 % 3 == 0 else "FEDEX_PRIORITY" if 628 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00629(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00629."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00629",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (629 % 7),
            "carrier_code": "DHL_EXPRESS" if 629 % 3 == 0 else "FEDEX_PRIORITY" if 629 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00630(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00630."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00630",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (630 % 7),
            "carrier_code": "DHL_EXPRESS" if 630 % 3 == 0 else "FEDEX_PRIORITY" if 630 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00631(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00631."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00631",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (631 % 7),
            "carrier_code": "DHL_EXPRESS" if 631 % 3 == 0 else "FEDEX_PRIORITY" if 631 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00632(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00632."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00632",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (632 % 7),
            "carrier_code": "DHL_EXPRESS" if 632 % 3 == 0 else "FEDEX_PRIORITY" if 632 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00633(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00633."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00633",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (633 % 7),
            "carrier_code": "DHL_EXPRESS" if 633 % 3 == 0 else "FEDEX_PRIORITY" if 633 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00634(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00634."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00634",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (634 % 7),
            "carrier_code": "DHL_EXPRESS" if 634 % 3 == 0 else "FEDEX_PRIORITY" if 634 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00635(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00635."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00635",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (635 % 7),
            "carrier_code": "DHL_EXPRESS" if 635 % 3 == 0 else "FEDEX_PRIORITY" if 635 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00636(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00636."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00636",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (636 % 7),
            "carrier_code": "DHL_EXPRESS" if 636 % 3 == 0 else "FEDEX_PRIORITY" if 636 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00637(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00637."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00637",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (637 % 7),
            "carrier_code": "DHL_EXPRESS" if 637 % 3 == 0 else "FEDEX_PRIORITY" if 637 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00638(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00638."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00638",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (638 % 7),
            "carrier_code": "DHL_EXPRESS" if 638 % 3 == 0 else "FEDEX_PRIORITY" if 638 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00639(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00639."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00639",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (639 % 7),
            "carrier_code": "DHL_EXPRESS" if 639 % 3 == 0 else "FEDEX_PRIORITY" if 639 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00640(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00640."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00640",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (640 % 7),
            "carrier_code": "DHL_EXPRESS" if 640 % 3 == 0 else "FEDEX_PRIORITY" if 640 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00641(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00641."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00641",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (641 % 7),
            "carrier_code": "DHL_EXPRESS" if 641 % 3 == 0 else "FEDEX_PRIORITY" if 641 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00642(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00642."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00642",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (642 % 7),
            "carrier_code": "DHL_EXPRESS" if 642 % 3 == 0 else "FEDEX_PRIORITY" if 642 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00643(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00643."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00643",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (643 % 7),
            "carrier_code": "DHL_EXPRESS" if 643 % 3 == 0 else "FEDEX_PRIORITY" if 643 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00644(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00644."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00644",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (644 % 7),
            "carrier_code": "DHL_EXPRESS" if 644 % 3 == 0 else "FEDEX_PRIORITY" if 644 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00645(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00645."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00645",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (645 % 7),
            "carrier_code": "DHL_EXPRESS" if 645 % 3 == 0 else "FEDEX_PRIORITY" if 645 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00646(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00646."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00646",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (646 % 7),
            "carrier_code": "DHL_EXPRESS" if 646 % 3 == 0 else "FEDEX_PRIORITY" if 646 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00647(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00647."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00647",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (647 % 7),
            "carrier_code": "DHL_EXPRESS" if 647 % 3 == 0 else "FEDEX_PRIORITY" if 647 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00648(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00648."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00648",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (648 % 7),
            "carrier_code": "DHL_EXPRESS" if 648 % 3 == 0 else "FEDEX_PRIORITY" if 648 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00649(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00649."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00649",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (649 % 7),
            "carrier_code": "DHL_EXPRESS" if 649 % 3 == 0 else "FEDEX_PRIORITY" if 649 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00650(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00650."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00650",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (650 % 7),
            "carrier_code": "DHL_EXPRESS" if 650 % 3 == 0 else "FEDEX_PRIORITY" if 650 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00651(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00651."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00651",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (651 % 7),
            "carrier_code": "DHL_EXPRESS" if 651 % 3 == 0 else "FEDEX_PRIORITY" if 651 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00652(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00652."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00652",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (652 % 7),
            "carrier_code": "DHL_EXPRESS" if 652 % 3 == 0 else "FEDEX_PRIORITY" if 652 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00653(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00653."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00653",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (653 % 7),
            "carrier_code": "DHL_EXPRESS" if 653 % 3 == 0 else "FEDEX_PRIORITY" if 653 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00654(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00654."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00654",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (654 % 7),
            "carrier_code": "DHL_EXPRESS" if 654 % 3 == 0 else "FEDEX_PRIORITY" if 654 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00655(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00655."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00655",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (655 % 7),
            "carrier_code": "DHL_EXPRESS" if 655 % 3 == 0 else "FEDEX_PRIORITY" if 655 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00656(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00656."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00656",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (656 % 7),
            "carrier_code": "DHL_EXPRESS" if 656 % 3 == 0 else "FEDEX_PRIORITY" if 656 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00657(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00657."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00657",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (657 % 7),
            "carrier_code": "DHL_EXPRESS" if 657 % 3 == 0 else "FEDEX_PRIORITY" if 657 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00658(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00658."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00658",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (658 % 7),
            "carrier_code": "DHL_EXPRESS" if 658 % 3 == 0 else "FEDEX_PRIORITY" if 658 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00659(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00659."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00659",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (659 % 7),
            "carrier_code": "DHL_EXPRESS" if 659 % 3 == 0 else "FEDEX_PRIORITY" if 659 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00660(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00660."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00660",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (660 % 7),
            "carrier_code": "DHL_EXPRESS" if 660 % 3 == 0 else "FEDEX_PRIORITY" if 660 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00661(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00661."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00661",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (661 % 7),
            "carrier_code": "DHL_EXPRESS" if 661 % 3 == 0 else "FEDEX_PRIORITY" if 661 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00662(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00662."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00662",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (662 % 7),
            "carrier_code": "DHL_EXPRESS" if 662 % 3 == 0 else "FEDEX_PRIORITY" if 662 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00663(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00663."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00663",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (663 % 7),
            "carrier_code": "DHL_EXPRESS" if 663 % 3 == 0 else "FEDEX_PRIORITY" if 663 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00664(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00664."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00664",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (664 % 7),
            "carrier_code": "DHL_EXPRESS" if 664 % 3 == 0 else "FEDEX_PRIORITY" if 664 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00665(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00665."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00665",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (665 % 7),
            "carrier_code": "DHL_EXPRESS" if 665 % 3 == 0 else "FEDEX_PRIORITY" if 665 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00666(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00666."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00666",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (666 % 7),
            "carrier_code": "DHL_EXPRESS" if 666 % 3 == 0 else "FEDEX_PRIORITY" if 666 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00667(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00667."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00667",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (667 % 7),
            "carrier_code": "DHL_EXPRESS" if 667 % 3 == 0 else "FEDEX_PRIORITY" if 667 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00668(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00668."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00668",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (668 % 7),
            "carrier_code": "DHL_EXPRESS" if 668 % 3 == 0 else "FEDEX_PRIORITY" if 668 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00669(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00669."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00669",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (669 % 7),
            "carrier_code": "DHL_EXPRESS" if 669 % 3 == 0 else "FEDEX_PRIORITY" if 669 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00670(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00670."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00670",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (670 % 7),
            "carrier_code": "DHL_EXPRESS" if 670 % 3 == 0 else "FEDEX_PRIORITY" if 670 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00671(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00671."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00671",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (671 % 7),
            "carrier_code": "DHL_EXPRESS" if 671 % 3 == 0 else "FEDEX_PRIORITY" if 671 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00672(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00672."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00672",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (672 % 7),
            "carrier_code": "DHL_EXPRESS" if 672 % 3 == 0 else "FEDEX_PRIORITY" if 672 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00673(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00673."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00673",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (673 % 7),
            "carrier_code": "DHL_EXPRESS" if 673 % 3 == 0 else "FEDEX_PRIORITY" if 673 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00674(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00674."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00674",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (674 % 7),
            "carrier_code": "DHL_EXPRESS" if 674 % 3 == 0 else "FEDEX_PRIORITY" if 674 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00675(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00675."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00675",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (675 % 7),
            "carrier_code": "DHL_EXPRESS" if 675 % 3 == 0 else "FEDEX_PRIORITY" if 675 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00676(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00676."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00676",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (676 % 7),
            "carrier_code": "DHL_EXPRESS" if 676 % 3 == 0 else "FEDEX_PRIORITY" if 676 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00677(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00677."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00677",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (677 % 7),
            "carrier_code": "DHL_EXPRESS" if 677 % 3 == 0 else "FEDEX_PRIORITY" if 677 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00678(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00678."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00678",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (678 % 7),
            "carrier_code": "DHL_EXPRESS" if 678 % 3 == 0 else "FEDEX_PRIORITY" if 678 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00679(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00679."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00679",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (679 % 7),
            "carrier_code": "DHL_EXPRESS" if 679 % 3 == 0 else "FEDEX_PRIORITY" if 679 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00680(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00680."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00680",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (680 % 7),
            "carrier_code": "DHL_EXPRESS" if 680 % 3 == 0 else "FEDEX_PRIORITY" if 680 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00681(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00681."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00681",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (681 % 7),
            "carrier_code": "DHL_EXPRESS" if 681 % 3 == 0 else "FEDEX_PRIORITY" if 681 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00682(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00682."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00682",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (682 % 7),
            "carrier_code": "DHL_EXPRESS" if 682 % 3 == 0 else "FEDEX_PRIORITY" if 682 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00683(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00683."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00683",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (683 % 7),
            "carrier_code": "DHL_EXPRESS" if 683 % 3 == 0 else "FEDEX_PRIORITY" if 683 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00684(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00684."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00684",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (684 % 7),
            "carrier_code": "DHL_EXPRESS" if 684 % 3 == 0 else "FEDEX_PRIORITY" if 684 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00685(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00685."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00685",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (685 % 7),
            "carrier_code": "DHL_EXPRESS" if 685 % 3 == 0 else "FEDEX_PRIORITY" if 685 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00686(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00686."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00686",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (686 % 7),
            "carrier_code": "DHL_EXPRESS" if 686 % 3 == 0 else "FEDEX_PRIORITY" if 686 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00687(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00687."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00687",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (687 % 7),
            "carrier_code": "DHL_EXPRESS" if 687 % 3 == 0 else "FEDEX_PRIORITY" if 687 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00688(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00688."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00688",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (688 % 7),
            "carrier_code": "DHL_EXPRESS" if 688 % 3 == 0 else "FEDEX_PRIORITY" if 688 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00689(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00689."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00689",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (689 % 7),
            "carrier_code": "DHL_EXPRESS" if 689 % 3 == 0 else "FEDEX_PRIORITY" if 689 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00690(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00690."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00690",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (690 % 7),
            "carrier_code": "DHL_EXPRESS" if 690 % 3 == 0 else "FEDEX_PRIORITY" if 690 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00691(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00691."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00691",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (691 % 7),
            "carrier_code": "DHL_EXPRESS" if 691 % 3 == 0 else "FEDEX_PRIORITY" if 691 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00692(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00692."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00692",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (692 % 7),
            "carrier_code": "DHL_EXPRESS" if 692 % 3 == 0 else "FEDEX_PRIORITY" if 692 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00693(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00693."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00693",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (693 % 7),
            "carrier_code": "DHL_EXPRESS" if 693 % 3 == 0 else "FEDEX_PRIORITY" if 693 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00694(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00694."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00694",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (694 % 7),
            "carrier_code": "DHL_EXPRESS" if 694 % 3 == 0 else "FEDEX_PRIORITY" if 694 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00695(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00695."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00695",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (695 % 7),
            "carrier_code": "DHL_EXPRESS" if 695 % 3 == 0 else "FEDEX_PRIORITY" if 695 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00696(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00696."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00696",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (696 % 7),
            "carrier_code": "DHL_EXPRESS" if 696 % 3 == 0 else "FEDEX_PRIORITY" if 696 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00697(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00697."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00697",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (697 % 7),
            "carrier_code": "DHL_EXPRESS" if 697 % 3 == 0 else "FEDEX_PRIORITY" if 697 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00698(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00698."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00698",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (698 % 7),
            "carrier_code": "DHL_EXPRESS" if 698 % 3 == 0 else "FEDEX_PRIORITY" if 698 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00699(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00699."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00699",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (699 % 7),
            "carrier_code": "DHL_EXPRESS" if 699 % 3 == 0 else "FEDEX_PRIORITY" if 699 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00700(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00700."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00700",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (700 % 7),
            "carrier_code": "DHL_EXPRESS" if 700 % 3 == 0 else "FEDEX_PRIORITY" if 700 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00701(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00701."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00701",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (701 % 7),
            "carrier_code": "DHL_EXPRESS" if 701 % 3 == 0 else "FEDEX_PRIORITY" if 701 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00702(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00702."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00702",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (702 % 7),
            "carrier_code": "DHL_EXPRESS" if 702 % 3 == 0 else "FEDEX_PRIORITY" if 702 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00703(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00703."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00703",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (703 % 7),
            "carrier_code": "DHL_EXPRESS" if 703 % 3 == 0 else "FEDEX_PRIORITY" if 703 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00704(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00704."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00704",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (704 % 7),
            "carrier_code": "DHL_EXPRESS" if 704 % 3 == 0 else "FEDEX_PRIORITY" if 704 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00705(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00705."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00705",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (705 % 7),
            "carrier_code": "DHL_EXPRESS" if 705 % 3 == 0 else "FEDEX_PRIORITY" if 705 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00706(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00706."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00706",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (706 % 7),
            "carrier_code": "DHL_EXPRESS" if 706 % 3 == 0 else "FEDEX_PRIORITY" if 706 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00707(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00707."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00707",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (707 % 7),
            "carrier_code": "DHL_EXPRESS" if 707 % 3 == 0 else "FEDEX_PRIORITY" if 707 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00708(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00708."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00708",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (708 % 7),
            "carrier_code": "DHL_EXPRESS" if 708 % 3 == 0 else "FEDEX_PRIORITY" if 708 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00709(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00709."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00709",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (709 % 7),
            "carrier_code": "DHL_EXPRESS" if 709 % 3 == 0 else "FEDEX_PRIORITY" if 709 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00710(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00710."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00710",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (710 % 7),
            "carrier_code": "DHL_EXPRESS" if 710 % 3 == 0 else "FEDEX_PRIORITY" if 710 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00711(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00711."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00711",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (711 % 7),
            "carrier_code": "DHL_EXPRESS" if 711 % 3 == 0 else "FEDEX_PRIORITY" if 711 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00712(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00712."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00712",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (712 % 7),
            "carrier_code": "DHL_EXPRESS" if 712 % 3 == 0 else "FEDEX_PRIORITY" if 712 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00713(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00713."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00713",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (713 % 7),
            "carrier_code": "DHL_EXPRESS" if 713 % 3 == 0 else "FEDEX_PRIORITY" if 713 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00714(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00714."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00714",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (714 % 7),
            "carrier_code": "DHL_EXPRESS" if 714 % 3 == 0 else "FEDEX_PRIORITY" if 714 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00715(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00715."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00715",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (715 % 7),
            "carrier_code": "DHL_EXPRESS" if 715 % 3 == 0 else "FEDEX_PRIORITY" if 715 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00716(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00716."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00716",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (716 % 7),
            "carrier_code": "DHL_EXPRESS" if 716 % 3 == 0 else "FEDEX_PRIORITY" if 716 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00717(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00717."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00717",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (717 % 7),
            "carrier_code": "DHL_EXPRESS" if 717 % 3 == 0 else "FEDEX_PRIORITY" if 717 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00718(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00718."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00718",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (718 % 7),
            "carrier_code": "DHL_EXPRESS" if 718 % 3 == 0 else "FEDEX_PRIORITY" if 718 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00719(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00719."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00719",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (719 % 7),
            "carrier_code": "DHL_EXPRESS" if 719 % 3 == 0 else "FEDEX_PRIORITY" if 719 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00720(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00720."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00720",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (720 % 7),
            "carrier_code": "DHL_EXPRESS" if 720 % 3 == 0 else "FEDEX_PRIORITY" if 720 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00721(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00721."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00721",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (721 % 7),
            "carrier_code": "DHL_EXPRESS" if 721 % 3 == 0 else "FEDEX_PRIORITY" if 721 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00722(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00722."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00722",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (722 % 7),
            "carrier_code": "DHL_EXPRESS" if 722 % 3 == 0 else "FEDEX_PRIORITY" if 722 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00723(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00723."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00723",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (723 % 7),
            "carrier_code": "DHL_EXPRESS" if 723 % 3 == 0 else "FEDEX_PRIORITY" if 723 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00724(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00724."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00724",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (724 % 7),
            "carrier_code": "DHL_EXPRESS" if 724 % 3 == 0 else "FEDEX_PRIORITY" if 724 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00725(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00725."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00725",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (725 % 7),
            "carrier_code": "DHL_EXPRESS" if 725 % 3 == 0 else "FEDEX_PRIORITY" if 725 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00726(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00726."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00726",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (726 % 7),
            "carrier_code": "DHL_EXPRESS" if 726 % 3 == 0 else "FEDEX_PRIORITY" if 726 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00727(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00727."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00727",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (727 % 7),
            "carrier_code": "DHL_EXPRESS" if 727 % 3 == 0 else "FEDEX_PRIORITY" if 727 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00728(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00728."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00728",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (728 % 7),
            "carrier_code": "DHL_EXPRESS" if 728 % 3 == 0 else "FEDEX_PRIORITY" if 728 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00729(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00729."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00729",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (729 % 7),
            "carrier_code": "DHL_EXPRESS" if 729 % 3 == 0 else "FEDEX_PRIORITY" if 729 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00730(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00730."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00730",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (730 % 7),
            "carrier_code": "DHL_EXPRESS" if 730 % 3 == 0 else "FEDEX_PRIORITY" if 730 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00731(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00731."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00731",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (731 % 7),
            "carrier_code": "DHL_EXPRESS" if 731 % 3 == 0 else "FEDEX_PRIORITY" if 731 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00732(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00732."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00732",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (732 % 7),
            "carrier_code": "DHL_EXPRESS" if 732 % 3 == 0 else "FEDEX_PRIORITY" if 732 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00733(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00733."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00733",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (733 % 7),
            "carrier_code": "DHL_EXPRESS" if 733 % 3 == 0 else "FEDEX_PRIORITY" if 733 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00734(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00734."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00734",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (734 % 7),
            "carrier_code": "DHL_EXPRESS" if 734 % 3 == 0 else "FEDEX_PRIORITY" if 734 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00735(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00735."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00735",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (735 % 7),
            "carrier_code": "DHL_EXPRESS" if 735 % 3 == 0 else "FEDEX_PRIORITY" if 735 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00736(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00736."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00736",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (736 % 7),
            "carrier_code": "DHL_EXPRESS" if 736 % 3 == 0 else "FEDEX_PRIORITY" if 736 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00737(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00737."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00737",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (737 % 7),
            "carrier_code": "DHL_EXPRESS" if 737 % 3 == 0 else "FEDEX_PRIORITY" if 737 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00738(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00738."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00738",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (738 % 7),
            "carrier_code": "DHL_EXPRESS" if 738 % 3 == 0 else "FEDEX_PRIORITY" if 738 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00739(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00739."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00739",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (739 % 7),
            "carrier_code": "DHL_EXPRESS" if 739 % 3 == 0 else "FEDEX_PRIORITY" if 739 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00740(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00740."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00740",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (740 % 7),
            "carrier_code": "DHL_EXPRESS" if 740 % 3 == 0 else "FEDEX_PRIORITY" if 740 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00741(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00741."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00741",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (741 % 7),
            "carrier_code": "DHL_EXPRESS" if 741 % 3 == 0 else "FEDEX_PRIORITY" if 741 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00742(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00742."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00742",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (742 % 7),
            "carrier_code": "DHL_EXPRESS" if 742 % 3 == 0 else "FEDEX_PRIORITY" if 742 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00743(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00743."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00743",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (743 % 7),
            "carrier_code": "DHL_EXPRESS" if 743 % 3 == 0 else "FEDEX_PRIORITY" if 743 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00744(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00744."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00744",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (744 % 7),
            "carrier_code": "DHL_EXPRESS" if 744 % 3 == 0 else "FEDEX_PRIORITY" if 744 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00745(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00745."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00745",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (745 % 7),
            "carrier_code": "DHL_EXPRESS" if 745 % 3 == 0 else "FEDEX_PRIORITY" if 745 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00746(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00746."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00746",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (746 % 7),
            "carrier_code": "DHL_EXPRESS" if 746 % 3 == 0 else "FEDEX_PRIORITY" if 746 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00747(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00747."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00747",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (747 % 7),
            "carrier_code": "DHL_EXPRESS" if 747 % 3 == 0 else "FEDEX_PRIORITY" if 747 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00748(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00748."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00748",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (748 % 7),
            "carrier_code": "DHL_EXPRESS" if 748 % 3 == 0 else "FEDEX_PRIORITY" if 748 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00749(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00749."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00749",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (749 % 7),
            "carrier_code": "DHL_EXPRESS" if 749 % 3 == 0 else "FEDEX_PRIORITY" if 749 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00750(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00750."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00750",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (750 % 7),
            "carrier_code": "DHL_EXPRESS" if 750 % 3 == 0 else "FEDEX_PRIORITY" if 750 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00751(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00751."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00751",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (751 % 7),
            "carrier_code": "DHL_EXPRESS" if 751 % 3 == 0 else "FEDEX_PRIORITY" if 751 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00752(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00752."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00752",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (752 % 7),
            "carrier_code": "DHL_EXPRESS" if 752 % 3 == 0 else "FEDEX_PRIORITY" if 752 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00753(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00753."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00753",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (753 % 7),
            "carrier_code": "DHL_EXPRESS" if 753 % 3 == 0 else "FEDEX_PRIORITY" if 753 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00754(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00754."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00754",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (754 % 7),
            "carrier_code": "DHL_EXPRESS" if 754 % 3 == 0 else "FEDEX_PRIORITY" if 754 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00755(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00755."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00755",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (755 % 7),
            "carrier_code": "DHL_EXPRESS" if 755 % 3 == 0 else "FEDEX_PRIORITY" if 755 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00756(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00756."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00756",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (756 % 7),
            "carrier_code": "DHL_EXPRESS" if 756 % 3 == 0 else "FEDEX_PRIORITY" if 756 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00757(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00757."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00757",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (757 % 7),
            "carrier_code": "DHL_EXPRESS" if 757 % 3 == 0 else "FEDEX_PRIORITY" if 757 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00758(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00758."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00758",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (758 % 7),
            "carrier_code": "DHL_EXPRESS" if 758 % 3 == 0 else "FEDEX_PRIORITY" if 758 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00759(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00759."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00759",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (759 % 7),
            "carrier_code": "DHL_EXPRESS" if 759 % 3 == 0 else "FEDEX_PRIORITY" if 759 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00760(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00760."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00760",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (760 % 7),
            "carrier_code": "DHL_EXPRESS" if 760 % 3 == 0 else "FEDEX_PRIORITY" if 760 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00761(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00761."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00761",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (761 % 7),
            "carrier_code": "DHL_EXPRESS" if 761 % 3 == 0 else "FEDEX_PRIORITY" if 761 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00762(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00762."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00762",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (762 % 7),
            "carrier_code": "DHL_EXPRESS" if 762 % 3 == 0 else "FEDEX_PRIORITY" if 762 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00763(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00763."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00763",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (763 % 7),
            "carrier_code": "DHL_EXPRESS" if 763 % 3 == 0 else "FEDEX_PRIORITY" if 763 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00764(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00764."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00764",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (764 % 7),
            "carrier_code": "DHL_EXPRESS" if 764 % 3 == 0 else "FEDEX_PRIORITY" if 764 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00765(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00765."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00765",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (765 % 7),
            "carrier_code": "DHL_EXPRESS" if 765 % 3 == 0 else "FEDEX_PRIORITY" if 765 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00766(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00766."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00766",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (766 % 7),
            "carrier_code": "DHL_EXPRESS" if 766 % 3 == 0 else "FEDEX_PRIORITY" if 766 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00767(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00767."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00767",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (767 % 7),
            "carrier_code": "DHL_EXPRESS" if 767 % 3 == 0 else "FEDEX_PRIORITY" if 767 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00768(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00768."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00768",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (768 % 7),
            "carrier_code": "DHL_EXPRESS" if 768 % 3 == 0 else "FEDEX_PRIORITY" if 768 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00769(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00769."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00769",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (769 % 7),
            "carrier_code": "DHL_EXPRESS" if 769 % 3 == 0 else "FEDEX_PRIORITY" if 769 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00770(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00770."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00770",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (770 % 7),
            "carrier_code": "DHL_EXPRESS" if 770 % 3 == 0 else "FEDEX_PRIORITY" if 770 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00771(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00771."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00771",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (771 % 7),
            "carrier_code": "DHL_EXPRESS" if 771 % 3 == 0 else "FEDEX_PRIORITY" if 771 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00772(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00772."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00772",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (772 % 7),
            "carrier_code": "DHL_EXPRESS" if 772 % 3 == 0 else "FEDEX_PRIORITY" if 772 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00773(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00773."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00773",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (773 % 7),
            "carrier_code": "DHL_EXPRESS" if 773 % 3 == 0 else "FEDEX_PRIORITY" if 773 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00774(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00774."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00774",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (774 % 7),
            "carrier_code": "DHL_EXPRESS" if 774 % 3 == 0 else "FEDEX_PRIORITY" if 774 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00775(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00775."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00775",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (775 % 7),
            "carrier_code": "DHL_EXPRESS" if 775 % 3 == 0 else "FEDEX_PRIORITY" if 775 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00776(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00776."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00776",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (776 % 7),
            "carrier_code": "DHL_EXPRESS" if 776 % 3 == 0 else "FEDEX_PRIORITY" if 776 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00777(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00777."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00777",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (777 % 7),
            "carrier_code": "DHL_EXPRESS" if 777 % 3 == 0 else "FEDEX_PRIORITY" if 777 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00778(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00778."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00778",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (778 % 7),
            "carrier_code": "DHL_EXPRESS" if 778 % 3 == 0 else "FEDEX_PRIORITY" if 778 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00779(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00779."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00779",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (779 % 7),
            "carrier_code": "DHL_EXPRESS" if 779 % 3 == 0 else "FEDEX_PRIORITY" if 779 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00780(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00780."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00780",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (780 % 7),
            "carrier_code": "DHL_EXPRESS" if 780 % 3 == 0 else "FEDEX_PRIORITY" if 780 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00781(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00781."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00781",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (781 % 7),
            "carrier_code": "DHL_EXPRESS" if 781 % 3 == 0 else "FEDEX_PRIORITY" if 781 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00782(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00782."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00782",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (782 % 7),
            "carrier_code": "DHL_EXPRESS" if 782 % 3 == 0 else "FEDEX_PRIORITY" if 782 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00783(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00783."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00783",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (783 % 7),
            "carrier_code": "DHL_EXPRESS" if 783 % 3 == 0 else "FEDEX_PRIORITY" if 783 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00784(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00784."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00784",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (784 % 7),
            "carrier_code": "DHL_EXPRESS" if 784 % 3 == 0 else "FEDEX_PRIORITY" if 784 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00785(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00785."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00785",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (785 % 7),
            "carrier_code": "DHL_EXPRESS" if 785 % 3 == 0 else "FEDEX_PRIORITY" if 785 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00786(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00786."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00786",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (786 % 7),
            "carrier_code": "DHL_EXPRESS" if 786 % 3 == 0 else "FEDEX_PRIORITY" if 786 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00787(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00787."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00787",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (787 % 7),
            "carrier_code": "DHL_EXPRESS" if 787 % 3 == 0 else "FEDEX_PRIORITY" if 787 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00788(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00788."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00788",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (788 % 7),
            "carrier_code": "DHL_EXPRESS" if 788 % 3 == 0 else "FEDEX_PRIORITY" if 788 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00789(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00789."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00789",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (789 % 7),
            "carrier_code": "DHL_EXPRESS" if 789 % 3 == 0 else "FEDEX_PRIORITY" if 789 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00790(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00790."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00790",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (790 % 7),
            "carrier_code": "DHL_EXPRESS" if 790 % 3 == 0 else "FEDEX_PRIORITY" if 790 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00791(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00791."""
        base_rate_per_kg = Decimal("3.95")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00791",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (791 % 7),
            "carrier_code": "DHL_EXPRESS" if 791 % 3 == 0 else "FEDEX_PRIORITY" if 791 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00792(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00792."""
        base_rate_per_kg = Decimal("4.40")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00792",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (792 % 7),
            "carrier_code": "DHL_EXPRESS" if 792 % 3 == 0 else "FEDEX_PRIORITY" if 792 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00793(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00793."""
        base_rate_per_kg = Decimal("4.85")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00793",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (793 % 7),
            "carrier_code": "DHL_EXPRESS" if 793 % 3 == 0 else "FEDEX_PRIORITY" if 793 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00794(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00794."""
        base_rate_per_kg = Decimal("5.30")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00794",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (794 % 7),
            "carrier_code": "DHL_EXPRESS" if 794 % 3 == 0 else "FEDEX_PRIORITY" if 794 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00795(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00795."""
        base_rate_per_kg = Decimal("5.75")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00795",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (795 % 7),
            "carrier_code": "DHL_EXPRESS" if 795 % 3 == 0 else "FEDEX_PRIORITY" if 795 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00796(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00796."""
        base_rate_per_kg = Decimal("6.20")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("4.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00796",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (796 % 7),
            "carrier_code": "DHL_EXPRESS" if 796 % 3 == 0 else "FEDEX_PRIORITY" if 796 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00797(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00797."""
        base_rate_per_kg = Decimal("6.65")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("5.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00797",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (797 % 7),
            "carrier_code": "DHL_EXPRESS" if 797 % 3 == 0 else "FEDEX_PRIORITY" if 797 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00798(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00798."""
        base_rate_per_kg = Decimal("7.10")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("2.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00798",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (798 % 7),
            "carrier_code": "DHL_EXPRESS" if 798 % 3 == 0 else "FEDEX_PRIORITY" if 798 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00799(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00799."""
        base_rate_per_kg = Decimal("7.55")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.00")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00799",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (799 % 7),
            "carrier_code": "DHL_EXPRESS" if 799 % 3 == 0 else "FEDEX_PRIORITY" if 799 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00800(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00800."""
        base_rate_per_kg = Decimal("3.50")
        fuel_surcharge_pct = Decimal("14.50")
        customs_duty_pct = Decimal("3.50")
        insurance_pct = Decimal("0.85")
        
        freight_cost = Decimal(str(weight_kg)) * base_rate_per_kg
        fuel_surcharge = (freight_cost * fuel_surcharge_pct) / Decimal("100.00")
        customs_duty = (declared_value_usd * customs_duty_pct) / Decimal("100.00")
        insurance_cost = (declared_value_usd * insurance_pct) / Decimal("100.00")
        total_landed_freight = freight_cost + fuel_surcharge + customs_duty + insurance_cost
        
        return {
            "corridor_id": "LOG-CORRIDOR-00800",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (800 % 7),
            "carrier_code": "DHL_EXPRESS" if 800 % 3 == 0 else "FEDEX_PRIORITY" if 800 % 3 == 1 else "UPS_SAVER",
        }
