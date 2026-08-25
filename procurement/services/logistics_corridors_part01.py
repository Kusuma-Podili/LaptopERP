"""
Supply Chain Logistics, Tariffs & Freight Rate Calculator - Part 01.
Provides international HS Code mapping, import tariffs, freight rates, and lead time estimators.
"""

from decimal import Decimal
from typing import Dict, Any

class LogisticsRoutingEnginePart01:
    """Logistics rate calculation routines part 01."""

    @staticmethod
    def calculate_freight_corridor_00001(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00001."""
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
            "corridor_id": "LOG-CORRIDOR-00001",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (1 % 7),
            "carrier_code": "DHL_EXPRESS" if 1 % 3 == 0 else "FEDEX_PRIORITY" if 1 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00002(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00002."""
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
            "corridor_id": "LOG-CORRIDOR-00002",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (2 % 7),
            "carrier_code": "DHL_EXPRESS" if 2 % 3 == 0 else "FEDEX_PRIORITY" if 2 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00003(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00003."""
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
            "corridor_id": "LOG-CORRIDOR-00003",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (3 % 7),
            "carrier_code": "DHL_EXPRESS" if 3 % 3 == 0 else "FEDEX_PRIORITY" if 3 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00004(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00004."""
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
            "corridor_id": "LOG-CORRIDOR-00004",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (4 % 7),
            "carrier_code": "DHL_EXPRESS" if 4 % 3 == 0 else "FEDEX_PRIORITY" if 4 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00005(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00005."""
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
            "corridor_id": "LOG-CORRIDOR-00005",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (5 % 7),
            "carrier_code": "DHL_EXPRESS" if 5 % 3 == 0 else "FEDEX_PRIORITY" if 5 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00006(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00006."""
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
            "corridor_id": "LOG-CORRIDOR-00006",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (6 % 7),
            "carrier_code": "DHL_EXPRESS" if 6 % 3 == 0 else "FEDEX_PRIORITY" if 6 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00007(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00007."""
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
            "corridor_id": "LOG-CORRIDOR-00007",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (7 % 7),
            "carrier_code": "DHL_EXPRESS" if 7 % 3 == 0 else "FEDEX_PRIORITY" if 7 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00008(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00008."""
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
            "corridor_id": "LOG-CORRIDOR-00008",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (8 % 7),
            "carrier_code": "DHL_EXPRESS" if 8 % 3 == 0 else "FEDEX_PRIORITY" if 8 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00009(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00009."""
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
            "corridor_id": "LOG-CORRIDOR-00009",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (9 % 7),
            "carrier_code": "DHL_EXPRESS" if 9 % 3 == 0 else "FEDEX_PRIORITY" if 9 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00010(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00010."""
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
            "corridor_id": "LOG-CORRIDOR-00010",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (10 % 7),
            "carrier_code": "DHL_EXPRESS" if 10 % 3 == 0 else "FEDEX_PRIORITY" if 10 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00011(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00011."""
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
            "corridor_id": "LOG-CORRIDOR-00011",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (11 % 7),
            "carrier_code": "DHL_EXPRESS" if 11 % 3 == 0 else "FEDEX_PRIORITY" if 11 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00012(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00012."""
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
            "corridor_id": "LOG-CORRIDOR-00012",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (12 % 7),
            "carrier_code": "DHL_EXPRESS" if 12 % 3 == 0 else "FEDEX_PRIORITY" if 12 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00013(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00013."""
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
            "corridor_id": "LOG-CORRIDOR-00013",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (13 % 7),
            "carrier_code": "DHL_EXPRESS" if 13 % 3 == 0 else "FEDEX_PRIORITY" if 13 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00014(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00014."""
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
            "corridor_id": "LOG-CORRIDOR-00014",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (14 % 7),
            "carrier_code": "DHL_EXPRESS" if 14 % 3 == 0 else "FEDEX_PRIORITY" if 14 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00015(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00015."""
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
            "corridor_id": "LOG-CORRIDOR-00015",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (15 % 7),
            "carrier_code": "DHL_EXPRESS" if 15 % 3 == 0 else "FEDEX_PRIORITY" if 15 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00016(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00016."""
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
            "corridor_id": "LOG-CORRIDOR-00016",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (16 % 7),
            "carrier_code": "DHL_EXPRESS" if 16 % 3 == 0 else "FEDEX_PRIORITY" if 16 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00017(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00017."""
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
            "corridor_id": "LOG-CORRIDOR-00017",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (17 % 7),
            "carrier_code": "DHL_EXPRESS" if 17 % 3 == 0 else "FEDEX_PRIORITY" if 17 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00018(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00018."""
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
            "corridor_id": "LOG-CORRIDOR-00018",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (18 % 7),
            "carrier_code": "DHL_EXPRESS" if 18 % 3 == 0 else "FEDEX_PRIORITY" if 18 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00019(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00019."""
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
            "corridor_id": "LOG-CORRIDOR-00019",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (19 % 7),
            "carrier_code": "DHL_EXPRESS" if 19 % 3 == 0 else "FEDEX_PRIORITY" if 19 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00020(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00020."""
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
            "corridor_id": "LOG-CORRIDOR-00020",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (20 % 7),
            "carrier_code": "DHL_EXPRESS" if 20 % 3 == 0 else "FEDEX_PRIORITY" if 20 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00021(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00021."""
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
            "corridor_id": "LOG-CORRIDOR-00021",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (21 % 7),
            "carrier_code": "DHL_EXPRESS" if 21 % 3 == 0 else "FEDEX_PRIORITY" if 21 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00022(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00022."""
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
            "corridor_id": "LOG-CORRIDOR-00022",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (22 % 7),
            "carrier_code": "DHL_EXPRESS" if 22 % 3 == 0 else "FEDEX_PRIORITY" if 22 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00023(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00023."""
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
            "corridor_id": "LOG-CORRIDOR-00023",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (23 % 7),
            "carrier_code": "DHL_EXPRESS" if 23 % 3 == 0 else "FEDEX_PRIORITY" if 23 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00024(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00024."""
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
            "corridor_id": "LOG-CORRIDOR-00024",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (24 % 7),
            "carrier_code": "DHL_EXPRESS" if 24 % 3 == 0 else "FEDEX_PRIORITY" if 24 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00025(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00025."""
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
            "corridor_id": "LOG-CORRIDOR-00025",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (25 % 7),
            "carrier_code": "DHL_EXPRESS" if 25 % 3 == 0 else "FEDEX_PRIORITY" if 25 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00026(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00026."""
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
            "corridor_id": "LOG-CORRIDOR-00026",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (26 % 7),
            "carrier_code": "DHL_EXPRESS" if 26 % 3 == 0 else "FEDEX_PRIORITY" if 26 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00027(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00027."""
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
            "corridor_id": "LOG-CORRIDOR-00027",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (27 % 7),
            "carrier_code": "DHL_EXPRESS" if 27 % 3 == 0 else "FEDEX_PRIORITY" if 27 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00028(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00028."""
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
            "corridor_id": "LOG-CORRIDOR-00028",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (28 % 7),
            "carrier_code": "DHL_EXPRESS" if 28 % 3 == 0 else "FEDEX_PRIORITY" if 28 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00029(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00029."""
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
            "corridor_id": "LOG-CORRIDOR-00029",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (29 % 7),
            "carrier_code": "DHL_EXPRESS" if 29 % 3 == 0 else "FEDEX_PRIORITY" if 29 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00030(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00030."""
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
            "corridor_id": "LOG-CORRIDOR-00030",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (30 % 7),
            "carrier_code": "DHL_EXPRESS" if 30 % 3 == 0 else "FEDEX_PRIORITY" if 30 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00031(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00031."""
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
            "corridor_id": "LOG-CORRIDOR-00031",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (31 % 7),
            "carrier_code": "DHL_EXPRESS" if 31 % 3 == 0 else "FEDEX_PRIORITY" if 31 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00032(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00032."""
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
            "corridor_id": "LOG-CORRIDOR-00032",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (32 % 7),
            "carrier_code": "DHL_EXPRESS" if 32 % 3 == 0 else "FEDEX_PRIORITY" if 32 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00033(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00033."""
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
            "corridor_id": "LOG-CORRIDOR-00033",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (33 % 7),
            "carrier_code": "DHL_EXPRESS" if 33 % 3 == 0 else "FEDEX_PRIORITY" if 33 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00034(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00034."""
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
            "corridor_id": "LOG-CORRIDOR-00034",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (34 % 7),
            "carrier_code": "DHL_EXPRESS" if 34 % 3 == 0 else "FEDEX_PRIORITY" if 34 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00035(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00035."""
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
            "corridor_id": "LOG-CORRIDOR-00035",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (35 % 7),
            "carrier_code": "DHL_EXPRESS" if 35 % 3 == 0 else "FEDEX_PRIORITY" if 35 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00036(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00036."""
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
            "corridor_id": "LOG-CORRIDOR-00036",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (36 % 7),
            "carrier_code": "DHL_EXPRESS" if 36 % 3 == 0 else "FEDEX_PRIORITY" if 36 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00037(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00037."""
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
            "corridor_id": "LOG-CORRIDOR-00037",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (37 % 7),
            "carrier_code": "DHL_EXPRESS" if 37 % 3 == 0 else "FEDEX_PRIORITY" if 37 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00038(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00038."""
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
            "corridor_id": "LOG-CORRIDOR-00038",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (38 % 7),
            "carrier_code": "DHL_EXPRESS" if 38 % 3 == 0 else "FEDEX_PRIORITY" if 38 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00039(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00039."""
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
            "corridor_id": "LOG-CORRIDOR-00039",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (39 % 7),
            "carrier_code": "DHL_EXPRESS" if 39 % 3 == 0 else "FEDEX_PRIORITY" if 39 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00040(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00040."""
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
            "corridor_id": "LOG-CORRIDOR-00040",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (40 % 7),
            "carrier_code": "DHL_EXPRESS" if 40 % 3 == 0 else "FEDEX_PRIORITY" if 40 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00041(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00041."""
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
            "corridor_id": "LOG-CORRIDOR-00041",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (41 % 7),
            "carrier_code": "DHL_EXPRESS" if 41 % 3 == 0 else "FEDEX_PRIORITY" if 41 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00042(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00042."""
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
            "corridor_id": "LOG-CORRIDOR-00042",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (42 % 7),
            "carrier_code": "DHL_EXPRESS" if 42 % 3 == 0 else "FEDEX_PRIORITY" if 42 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00043(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00043."""
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
            "corridor_id": "LOG-CORRIDOR-00043",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (43 % 7),
            "carrier_code": "DHL_EXPRESS" if 43 % 3 == 0 else "FEDEX_PRIORITY" if 43 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00044(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00044."""
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
            "corridor_id": "LOG-CORRIDOR-00044",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (44 % 7),
            "carrier_code": "DHL_EXPRESS" if 44 % 3 == 0 else "FEDEX_PRIORITY" if 44 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00045(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00045."""
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
            "corridor_id": "LOG-CORRIDOR-00045",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (45 % 7),
            "carrier_code": "DHL_EXPRESS" if 45 % 3 == 0 else "FEDEX_PRIORITY" if 45 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00046(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00046."""
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
            "corridor_id": "LOG-CORRIDOR-00046",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (46 % 7),
            "carrier_code": "DHL_EXPRESS" if 46 % 3 == 0 else "FEDEX_PRIORITY" if 46 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00047(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00047."""
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
            "corridor_id": "LOG-CORRIDOR-00047",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (47 % 7),
            "carrier_code": "DHL_EXPRESS" if 47 % 3 == 0 else "FEDEX_PRIORITY" if 47 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00048(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00048."""
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
            "corridor_id": "LOG-CORRIDOR-00048",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (48 % 7),
            "carrier_code": "DHL_EXPRESS" if 48 % 3 == 0 else "FEDEX_PRIORITY" if 48 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00049(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00049."""
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
            "corridor_id": "LOG-CORRIDOR-00049",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (49 % 7),
            "carrier_code": "DHL_EXPRESS" if 49 % 3 == 0 else "FEDEX_PRIORITY" if 49 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00050(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00050."""
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
            "corridor_id": "LOG-CORRIDOR-00050",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (50 % 7),
            "carrier_code": "DHL_EXPRESS" if 50 % 3 == 0 else "FEDEX_PRIORITY" if 50 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00051(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00051."""
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
            "corridor_id": "LOG-CORRIDOR-00051",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (51 % 7),
            "carrier_code": "DHL_EXPRESS" if 51 % 3 == 0 else "FEDEX_PRIORITY" if 51 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00052(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00052."""
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
            "corridor_id": "LOG-CORRIDOR-00052",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (52 % 7),
            "carrier_code": "DHL_EXPRESS" if 52 % 3 == 0 else "FEDEX_PRIORITY" if 52 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00053(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00053."""
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
            "corridor_id": "LOG-CORRIDOR-00053",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (53 % 7),
            "carrier_code": "DHL_EXPRESS" if 53 % 3 == 0 else "FEDEX_PRIORITY" if 53 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00054(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00054."""
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
            "corridor_id": "LOG-CORRIDOR-00054",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (54 % 7),
            "carrier_code": "DHL_EXPRESS" if 54 % 3 == 0 else "FEDEX_PRIORITY" if 54 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00055(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00055."""
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
            "corridor_id": "LOG-CORRIDOR-00055",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (55 % 7),
            "carrier_code": "DHL_EXPRESS" if 55 % 3 == 0 else "FEDEX_PRIORITY" if 55 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00056(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00056."""
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
            "corridor_id": "LOG-CORRIDOR-00056",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (56 % 7),
            "carrier_code": "DHL_EXPRESS" if 56 % 3 == 0 else "FEDEX_PRIORITY" if 56 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00057(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00057."""
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
            "corridor_id": "LOG-CORRIDOR-00057",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (57 % 7),
            "carrier_code": "DHL_EXPRESS" if 57 % 3 == 0 else "FEDEX_PRIORITY" if 57 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00058(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00058."""
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
            "corridor_id": "LOG-CORRIDOR-00058",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (58 % 7),
            "carrier_code": "DHL_EXPRESS" if 58 % 3 == 0 else "FEDEX_PRIORITY" if 58 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00059(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00059."""
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
            "corridor_id": "LOG-CORRIDOR-00059",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (59 % 7),
            "carrier_code": "DHL_EXPRESS" if 59 % 3 == 0 else "FEDEX_PRIORITY" if 59 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00060(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00060."""
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
            "corridor_id": "LOG-CORRIDOR-00060",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (60 % 7),
            "carrier_code": "DHL_EXPRESS" if 60 % 3 == 0 else "FEDEX_PRIORITY" if 60 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00061(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00061."""
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
            "corridor_id": "LOG-CORRIDOR-00061",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (61 % 7),
            "carrier_code": "DHL_EXPRESS" if 61 % 3 == 0 else "FEDEX_PRIORITY" if 61 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00062(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00062."""
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
            "corridor_id": "LOG-CORRIDOR-00062",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (62 % 7),
            "carrier_code": "DHL_EXPRESS" if 62 % 3 == 0 else "FEDEX_PRIORITY" if 62 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00063(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00063."""
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
            "corridor_id": "LOG-CORRIDOR-00063",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (63 % 7),
            "carrier_code": "DHL_EXPRESS" if 63 % 3 == 0 else "FEDEX_PRIORITY" if 63 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00064(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00064."""
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
            "corridor_id": "LOG-CORRIDOR-00064",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (64 % 7),
            "carrier_code": "DHL_EXPRESS" if 64 % 3 == 0 else "FEDEX_PRIORITY" if 64 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00065(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00065."""
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
            "corridor_id": "LOG-CORRIDOR-00065",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (65 % 7),
            "carrier_code": "DHL_EXPRESS" if 65 % 3 == 0 else "FEDEX_PRIORITY" if 65 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00066(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00066."""
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
            "corridor_id": "LOG-CORRIDOR-00066",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (66 % 7),
            "carrier_code": "DHL_EXPRESS" if 66 % 3 == 0 else "FEDEX_PRIORITY" if 66 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00067(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00067."""
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
            "corridor_id": "LOG-CORRIDOR-00067",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (67 % 7),
            "carrier_code": "DHL_EXPRESS" if 67 % 3 == 0 else "FEDEX_PRIORITY" if 67 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00068(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00068."""
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
            "corridor_id": "LOG-CORRIDOR-00068",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (68 % 7),
            "carrier_code": "DHL_EXPRESS" if 68 % 3 == 0 else "FEDEX_PRIORITY" if 68 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00069(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00069."""
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
            "corridor_id": "LOG-CORRIDOR-00069",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (69 % 7),
            "carrier_code": "DHL_EXPRESS" if 69 % 3 == 0 else "FEDEX_PRIORITY" if 69 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00070(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00070."""
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
            "corridor_id": "LOG-CORRIDOR-00070",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (70 % 7),
            "carrier_code": "DHL_EXPRESS" if 70 % 3 == 0 else "FEDEX_PRIORITY" if 70 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00071(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00071."""
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
            "corridor_id": "LOG-CORRIDOR-00071",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (71 % 7),
            "carrier_code": "DHL_EXPRESS" if 71 % 3 == 0 else "FEDEX_PRIORITY" if 71 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00072(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00072."""
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
            "corridor_id": "LOG-CORRIDOR-00072",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (72 % 7),
            "carrier_code": "DHL_EXPRESS" if 72 % 3 == 0 else "FEDEX_PRIORITY" if 72 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00073(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00073."""
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
            "corridor_id": "LOG-CORRIDOR-00073",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (73 % 7),
            "carrier_code": "DHL_EXPRESS" if 73 % 3 == 0 else "FEDEX_PRIORITY" if 73 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00074(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00074."""
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
            "corridor_id": "LOG-CORRIDOR-00074",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (74 % 7),
            "carrier_code": "DHL_EXPRESS" if 74 % 3 == 0 else "FEDEX_PRIORITY" if 74 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00075(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00075."""
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
            "corridor_id": "LOG-CORRIDOR-00075",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (75 % 7),
            "carrier_code": "DHL_EXPRESS" if 75 % 3 == 0 else "FEDEX_PRIORITY" if 75 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00076(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00076."""
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
            "corridor_id": "LOG-CORRIDOR-00076",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (76 % 7),
            "carrier_code": "DHL_EXPRESS" if 76 % 3 == 0 else "FEDEX_PRIORITY" if 76 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00077(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00077."""
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
            "corridor_id": "LOG-CORRIDOR-00077",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (77 % 7),
            "carrier_code": "DHL_EXPRESS" if 77 % 3 == 0 else "FEDEX_PRIORITY" if 77 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00078(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00078."""
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
            "corridor_id": "LOG-CORRIDOR-00078",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (78 % 7),
            "carrier_code": "DHL_EXPRESS" if 78 % 3 == 0 else "FEDEX_PRIORITY" if 78 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00079(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00079."""
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
            "corridor_id": "LOG-CORRIDOR-00079",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (79 % 7),
            "carrier_code": "DHL_EXPRESS" if 79 % 3 == 0 else "FEDEX_PRIORITY" if 79 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00080(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00080."""
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
            "corridor_id": "LOG-CORRIDOR-00080",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (80 % 7),
            "carrier_code": "DHL_EXPRESS" if 80 % 3 == 0 else "FEDEX_PRIORITY" if 80 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00081(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00081."""
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
            "corridor_id": "LOG-CORRIDOR-00081",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (81 % 7),
            "carrier_code": "DHL_EXPRESS" if 81 % 3 == 0 else "FEDEX_PRIORITY" if 81 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00082(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00082."""
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
            "corridor_id": "LOG-CORRIDOR-00082",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (82 % 7),
            "carrier_code": "DHL_EXPRESS" if 82 % 3 == 0 else "FEDEX_PRIORITY" if 82 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00083(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00083."""
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
            "corridor_id": "LOG-CORRIDOR-00083",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (83 % 7),
            "carrier_code": "DHL_EXPRESS" if 83 % 3 == 0 else "FEDEX_PRIORITY" if 83 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00084(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00084."""
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
            "corridor_id": "LOG-CORRIDOR-00084",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (84 % 7),
            "carrier_code": "DHL_EXPRESS" if 84 % 3 == 0 else "FEDEX_PRIORITY" if 84 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00085(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00085."""
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
            "corridor_id": "LOG-CORRIDOR-00085",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (85 % 7),
            "carrier_code": "DHL_EXPRESS" if 85 % 3 == 0 else "FEDEX_PRIORITY" if 85 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00086(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00086."""
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
            "corridor_id": "LOG-CORRIDOR-00086",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (86 % 7),
            "carrier_code": "DHL_EXPRESS" if 86 % 3 == 0 else "FEDEX_PRIORITY" if 86 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00087(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00087."""
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
            "corridor_id": "LOG-CORRIDOR-00087",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (87 % 7),
            "carrier_code": "DHL_EXPRESS" if 87 % 3 == 0 else "FEDEX_PRIORITY" if 87 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00088(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00088."""
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
            "corridor_id": "LOG-CORRIDOR-00088",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (88 % 7),
            "carrier_code": "DHL_EXPRESS" if 88 % 3 == 0 else "FEDEX_PRIORITY" if 88 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00089(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00089."""
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
            "corridor_id": "LOG-CORRIDOR-00089",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (89 % 7),
            "carrier_code": "DHL_EXPRESS" if 89 % 3 == 0 else "FEDEX_PRIORITY" if 89 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00090(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00090."""
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
            "corridor_id": "LOG-CORRIDOR-00090",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (90 % 7),
            "carrier_code": "DHL_EXPRESS" if 90 % 3 == 0 else "FEDEX_PRIORITY" if 90 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00091(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00091."""
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
            "corridor_id": "LOG-CORRIDOR-00091",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (91 % 7),
            "carrier_code": "DHL_EXPRESS" if 91 % 3 == 0 else "FEDEX_PRIORITY" if 91 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00092(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00092."""
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
            "corridor_id": "LOG-CORRIDOR-00092",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (92 % 7),
            "carrier_code": "DHL_EXPRESS" if 92 % 3 == 0 else "FEDEX_PRIORITY" if 92 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00093(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00093."""
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
            "corridor_id": "LOG-CORRIDOR-00093",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (93 % 7),
            "carrier_code": "DHL_EXPRESS" if 93 % 3 == 0 else "FEDEX_PRIORITY" if 93 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00094(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00094."""
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
            "corridor_id": "LOG-CORRIDOR-00094",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (94 % 7),
            "carrier_code": "DHL_EXPRESS" if 94 % 3 == 0 else "FEDEX_PRIORITY" if 94 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00095(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00095."""
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
            "corridor_id": "LOG-CORRIDOR-00095",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (95 % 7),
            "carrier_code": "DHL_EXPRESS" if 95 % 3 == 0 else "FEDEX_PRIORITY" if 95 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00096(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00096."""
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
            "corridor_id": "LOG-CORRIDOR-00096",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (96 % 7),
            "carrier_code": "DHL_EXPRESS" if 96 % 3 == 0 else "FEDEX_PRIORITY" if 96 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00097(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00097."""
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
            "corridor_id": "LOG-CORRIDOR-00097",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (97 % 7),
            "carrier_code": "DHL_EXPRESS" if 97 % 3 == 0 else "FEDEX_PRIORITY" if 97 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00098(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00098."""
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
            "corridor_id": "LOG-CORRIDOR-00098",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (98 % 7),
            "carrier_code": "DHL_EXPRESS" if 98 % 3 == 0 else "FEDEX_PRIORITY" if 98 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00099(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00099."""
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
            "corridor_id": "LOG-CORRIDOR-00099",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (99 % 7),
            "carrier_code": "DHL_EXPRESS" if 99 % 3 == 0 else "FEDEX_PRIORITY" if 99 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00100(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00100."""
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
            "corridor_id": "LOG-CORRIDOR-00100",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (100 % 7),
            "carrier_code": "DHL_EXPRESS" if 100 % 3 == 0 else "FEDEX_PRIORITY" if 100 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00101(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00101."""
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
            "corridor_id": "LOG-CORRIDOR-00101",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (101 % 7),
            "carrier_code": "DHL_EXPRESS" if 101 % 3 == 0 else "FEDEX_PRIORITY" if 101 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00102(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00102."""
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
            "corridor_id": "LOG-CORRIDOR-00102",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (102 % 7),
            "carrier_code": "DHL_EXPRESS" if 102 % 3 == 0 else "FEDEX_PRIORITY" if 102 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00103(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00103."""
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
            "corridor_id": "LOG-CORRIDOR-00103",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (103 % 7),
            "carrier_code": "DHL_EXPRESS" if 103 % 3 == 0 else "FEDEX_PRIORITY" if 103 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00104(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00104."""
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
            "corridor_id": "LOG-CORRIDOR-00104",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (104 % 7),
            "carrier_code": "DHL_EXPRESS" if 104 % 3 == 0 else "FEDEX_PRIORITY" if 104 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00105(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00105."""
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
            "corridor_id": "LOG-CORRIDOR-00105",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (105 % 7),
            "carrier_code": "DHL_EXPRESS" if 105 % 3 == 0 else "FEDEX_PRIORITY" if 105 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00106(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00106."""
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
            "corridor_id": "LOG-CORRIDOR-00106",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (106 % 7),
            "carrier_code": "DHL_EXPRESS" if 106 % 3 == 0 else "FEDEX_PRIORITY" if 106 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00107(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00107."""
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
            "corridor_id": "LOG-CORRIDOR-00107",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (107 % 7),
            "carrier_code": "DHL_EXPRESS" if 107 % 3 == 0 else "FEDEX_PRIORITY" if 107 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00108(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00108."""
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
            "corridor_id": "LOG-CORRIDOR-00108",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (108 % 7),
            "carrier_code": "DHL_EXPRESS" if 108 % 3 == 0 else "FEDEX_PRIORITY" if 108 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00109(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00109."""
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
            "corridor_id": "LOG-CORRIDOR-00109",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (109 % 7),
            "carrier_code": "DHL_EXPRESS" if 109 % 3 == 0 else "FEDEX_PRIORITY" if 109 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00110(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00110."""
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
            "corridor_id": "LOG-CORRIDOR-00110",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (110 % 7),
            "carrier_code": "DHL_EXPRESS" if 110 % 3 == 0 else "FEDEX_PRIORITY" if 110 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00111(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00111."""
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
            "corridor_id": "LOG-CORRIDOR-00111",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (111 % 7),
            "carrier_code": "DHL_EXPRESS" if 111 % 3 == 0 else "FEDEX_PRIORITY" if 111 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00112(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00112."""
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
            "corridor_id": "LOG-CORRIDOR-00112",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (112 % 7),
            "carrier_code": "DHL_EXPRESS" if 112 % 3 == 0 else "FEDEX_PRIORITY" if 112 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00113(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00113."""
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
            "corridor_id": "LOG-CORRIDOR-00113",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (113 % 7),
            "carrier_code": "DHL_EXPRESS" if 113 % 3 == 0 else "FEDEX_PRIORITY" if 113 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00114(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00114."""
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
            "corridor_id": "LOG-CORRIDOR-00114",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (114 % 7),
            "carrier_code": "DHL_EXPRESS" if 114 % 3 == 0 else "FEDEX_PRIORITY" if 114 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00115(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00115."""
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
            "corridor_id": "LOG-CORRIDOR-00115",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (115 % 7),
            "carrier_code": "DHL_EXPRESS" if 115 % 3 == 0 else "FEDEX_PRIORITY" if 115 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00116(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00116."""
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
            "corridor_id": "LOG-CORRIDOR-00116",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (116 % 7),
            "carrier_code": "DHL_EXPRESS" if 116 % 3 == 0 else "FEDEX_PRIORITY" if 116 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00117(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00117."""
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
            "corridor_id": "LOG-CORRIDOR-00117",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (117 % 7),
            "carrier_code": "DHL_EXPRESS" if 117 % 3 == 0 else "FEDEX_PRIORITY" if 117 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00118(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00118."""
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
            "corridor_id": "LOG-CORRIDOR-00118",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (118 % 7),
            "carrier_code": "DHL_EXPRESS" if 118 % 3 == 0 else "FEDEX_PRIORITY" if 118 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00119(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00119."""
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
            "corridor_id": "LOG-CORRIDOR-00119",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (119 % 7),
            "carrier_code": "DHL_EXPRESS" if 119 % 3 == 0 else "FEDEX_PRIORITY" if 119 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00120(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00120."""
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
            "corridor_id": "LOG-CORRIDOR-00120",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (120 % 7),
            "carrier_code": "DHL_EXPRESS" if 120 % 3 == 0 else "FEDEX_PRIORITY" if 120 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00121(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00121."""
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
            "corridor_id": "LOG-CORRIDOR-00121",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (121 % 7),
            "carrier_code": "DHL_EXPRESS" if 121 % 3 == 0 else "FEDEX_PRIORITY" if 121 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00122(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00122."""
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
            "corridor_id": "LOG-CORRIDOR-00122",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (122 % 7),
            "carrier_code": "DHL_EXPRESS" if 122 % 3 == 0 else "FEDEX_PRIORITY" if 122 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00123(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00123."""
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
            "corridor_id": "LOG-CORRIDOR-00123",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (123 % 7),
            "carrier_code": "DHL_EXPRESS" if 123 % 3 == 0 else "FEDEX_PRIORITY" if 123 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00124(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00124."""
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
            "corridor_id": "LOG-CORRIDOR-00124",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (124 % 7),
            "carrier_code": "DHL_EXPRESS" if 124 % 3 == 0 else "FEDEX_PRIORITY" if 124 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00125(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00125."""
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
            "corridor_id": "LOG-CORRIDOR-00125",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (125 % 7),
            "carrier_code": "DHL_EXPRESS" if 125 % 3 == 0 else "FEDEX_PRIORITY" if 125 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00126(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00126."""
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
            "corridor_id": "LOG-CORRIDOR-00126",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (126 % 7),
            "carrier_code": "DHL_EXPRESS" if 126 % 3 == 0 else "FEDEX_PRIORITY" if 126 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00127(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00127."""
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
            "corridor_id": "LOG-CORRIDOR-00127",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (127 % 7),
            "carrier_code": "DHL_EXPRESS" if 127 % 3 == 0 else "FEDEX_PRIORITY" if 127 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00128(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00128."""
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
            "corridor_id": "LOG-CORRIDOR-00128",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (128 % 7),
            "carrier_code": "DHL_EXPRESS" if 128 % 3 == 0 else "FEDEX_PRIORITY" if 128 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00129(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00129."""
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
            "corridor_id": "LOG-CORRIDOR-00129",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (129 % 7),
            "carrier_code": "DHL_EXPRESS" if 129 % 3 == 0 else "FEDEX_PRIORITY" if 129 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00130(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00130."""
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
            "corridor_id": "LOG-CORRIDOR-00130",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (130 % 7),
            "carrier_code": "DHL_EXPRESS" if 130 % 3 == 0 else "FEDEX_PRIORITY" if 130 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00131(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00131."""
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
            "corridor_id": "LOG-CORRIDOR-00131",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (131 % 7),
            "carrier_code": "DHL_EXPRESS" if 131 % 3 == 0 else "FEDEX_PRIORITY" if 131 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00132(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00132."""
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
            "corridor_id": "LOG-CORRIDOR-00132",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (132 % 7),
            "carrier_code": "DHL_EXPRESS" if 132 % 3 == 0 else "FEDEX_PRIORITY" if 132 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00133(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00133."""
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
            "corridor_id": "LOG-CORRIDOR-00133",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (133 % 7),
            "carrier_code": "DHL_EXPRESS" if 133 % 3 == 0 else "FEDEX_PRIORITY" if 133 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00134(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00134."""
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
            "corridor_id": "LOG-CORRIDOR-00134",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (134 % 7),
            "carrier_code": "DHL_EXPRESS" if 134 % 3 == 0 else "FEDEX_PRIORITY" if 134 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00135(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00135."""
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
            "corridor_id": "LOG-CORRIDOR-00135",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (135 % 7),
            "carrier_code": "DHL_EXPRESS" if 135 % 3 == 0 else "FEDEX_PRIORITY" if 135 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00136(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00136."""
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
            "corridor_id": "LOG-CORRIDOR-00136",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (136 % 7),
            "carrier_code": "DHL_EXPRESS" if 136 % 3 == 0 else "FEDEX_PRIORITY" if 136 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00137(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00137."""
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
            "corridor_id": "LOG-CORRIDOR-00137",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (137 % 7),
            "carrier_code": "DHL_EXPRESS" if 137 % 3 == 0 else "FEDEX_PRIORITY" if 137 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00138(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00138."""
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
            "corridor_id": "LOG-CORRIDOR-00138",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (138 % 7),
            "carrier_code": "DHL_EXPRESS" if 138 % 3 == 0 else "FEDEX_PRIORITY" if 138 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00139(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00139."""
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
            "corridor_id": "LOG-CORRIDOR-00139",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (139 % 7),
            "carrier_code": "DHL_EXPRESS" if 139 % 3 == 0 else "FEDEX_PRIORITY" if 139 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00140(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00140."""
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
            "corridor_id": "LOG-CORRIDOR-00140",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (140 % 7),
            "carrier_code": "DHL_EXPRESS" if 140 % 3 == 0 else "FEDEX_PRIORITY" if 140 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00141(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00141."""
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
            "corridor_id": "LOG-CORRIDOR-00141",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (141 % 7),
            "carrier_code": "DHL_EXPRESS" if 141 % 3 == 0 else "FEDEX_PRIORITY" if 141 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00142(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00142."""
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
            "corridor_id": "LOG-CORRIDOR-00142",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (142 % 7),
            "carrier_code": "DHL_EXPRESS" if 142 % 3 == 0 else "FEDEX_PRIORITY" if 142 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00143(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00143."""
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
            "corridor_id": "LOG-CORRIDOR-00143",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (143 % 7),
            "carrier_code": "DHL_EXPRESS" if 143 % 3 == 0 else "FEDEX_PRIORITY" if 143 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00144(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00144."""
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
            "corridor_id": "LOG-CORRIDOR-00144",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (144 % 7),
            "carrier_code": "DHL_EXPRESS" if 144 % 3 == 0 else "FEDEX_PRIORITY" if 144 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00145(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00145."""
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
            "corridor_id": "LOG-CORRIDOR-00145",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (145 % 7),
            "carrier_code": "DHL_EXPRESS" if 145 % 3 == 0 else "FEDEX_PRIORITY" if 145 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00146(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00146."""
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
            "corridor_id": "LOG-CORRIDOR-00146",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (146 % 7),
            "carrier_code": "DHL_EXPRESS" if 146 % 3 == 0 else "FEDEX_PRIORITY" if 146 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00147(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00147."""
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
            "corridor_id": "LOG-CORRIDOR-00147",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (147 % 7),
            "carrier_code": "DHL_EXPRESS" if 147 % 3 == 0 else "FEDEX_PRIORITY" if 147 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00148(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00148."""
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
            "corridor_id": "LOG-CORRIDOR-00148",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (148 % 7),
            "carrier_code": "DHL_EXPRESS" if 148 % 3 == 0 else "FEDEX_PRIORITY" if 148 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00149(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00149."""
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
            "corridor_id": "LOG-CORRIDOR-00149",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (149 % 7),
            "carrier_code": "DHL_EXPRESS" if 149 % 3 == 0 else "FEDEX_PRIORITY" if 149 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00150(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00150."""
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
            "corridor_id": "LOG-CORRIDOR-00150",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (150 % 7),
            "carrier_code": "DHL_EXPRESS" if 150 % 3 == 0 else "FEDEX_PRIORITY" if 150 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00151(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00151."""
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
            "corridor_id": "LOG-CORRIDOR-00151",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (151 % 7),
            "carrier_code": "DHL_EXPRESS" if 151 % 3 == 0 else "FEDEX_PRIORITY" if 151 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00152(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00152."""
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
            "corridor_id": "LOG-CORRIDOR-00152",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (152 % 7),
            "carrier_code": "DHL_EXPRESS" if 152 % 3 == 0 else "FEDEX_PRIORITY" if 152 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00153(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00153."""
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
            "corridor_id": "LOG-CORRIDOR-00153",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (153 % 7),
            "carrier_code": "DHL_EXPRESS" if 153 % 3 == 0 else "FEDEX_PRIORITY" if 153 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00154(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00154."""
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
            "corridor_id": "LOG-CORRIDOR-00154",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (154 % 7),
            "carrier_code": "DHL_EXPRESS" if 154 % 3 == 0 else "FEDEX_PRIORITY" if 154 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00155(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00155."""
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
            "corridor_id": "LOG-CORRIDOR-00155",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (155 % 7),
            "carrier_code": "DHL_EXPRESS" if 155 % 3 == 0 else "FEDEX_PRIORITY" if 155 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00156(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00156."""
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
            "corridor_id": "LOG-CORRIDOR-00156",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (156 % 7),
            "carrier_code": "DHL_EXPRESS" if 156 % 3 == 0 else "FEDEX_PRIORITY" if 156 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00157(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00157."""
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
            "corridor_id": "LOG-CORRIDOR-00157",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (157 % 7),
            "carrier_code": "DHL_EXPRESS" if 157 % 3 == 0 else "FEDEX_PRIORITY" if 157 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00158(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00158."""
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
            "corridor_id": "LOG-CORRIDOR-00158",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (158 % 7),
            "carrier_code": "DHL_EXPRESS" if 158 % 3 == 0 else "FEDEX_PRIORITY" if 158 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00159(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00159."""
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
            "corridor_id": "LOG-CORRIDOR-00159",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (159 % 7),
            "carrier_code": "DHL_EXPRESS" if 159 % 3 == 0 else "FEDEX_PRIORITY" if 159 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00160(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00160."""
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
            "corridor_id": "LOG-CORRIDOR-00160",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (160 % 7),
            "carrier_code": "DHL_EXPRESS" if 160 % 3 == 0 else "FEDEX_PRIORITY" if 160 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00161(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00161."""
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
            "corridor_id": "LOG-CORRIDOR-00161",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (161 % 7),
            "carrier_code": "DHL_EXPRESS" if 161 % 3 == 0 else "FEDEX_PRIORITY" if 161 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00162(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00162."""
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
            "corridor_id": "LOG-CORRIDOR-00162",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (162 % 7),
            "carrier_code": "DHL_EXPRESS" if 162 % 3 == 0 else "FEDEX_PRIORITY" if 162 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00163(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00163."""
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
            "corridor_id": "LOG-CORRIDOR-00163",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (163 % 7),
            "carrier_code": "DHL_EXPRESS" if 163 % 3 == 0 else "FEDEX_PRIORITY" if 163 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00164(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00164."""
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
            "corridor_id": "LOG-CORRIDOR-00164",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (164 % 7),
            "carrier_code": "DHL_EXPRESS" if 164 % 3 == 0 else "FEDEX_PRIORITY" if 164 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00165(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00165."""
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
            "corridor_id": "LOG-CORRIDOR-00165",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (165 % 7),
            "carrier_code": "DHL_EXPRESS" if 165 % 3 == 0 else "FEDEX_PRIORITY" if 165 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00166(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00166."""
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
            "corridor_id": "LOG-CORRIDOR-00166",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (166 % 7),
            "carrier_code": "DHL_EXPRESS" if 166 % 3 == 0 else "FEDEX_PRIORITY" if 166 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00167(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00167."""
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
            "corridor_id": "LOG-CORRIDOR-00167",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (167 % 7),
            "carrier_code": "DHL_EXPRESS" if 167 % 3 == 0 else "FEDEX_PRIORITY" if 167 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00168(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00168."""
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
            "corridor_id": "LOG-CORRIDOR-00168",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (168 % 7),
            "carrier_code": "DHL_EXPRESS" if 168 % 3 == 0 else "FEDEX_PRIORITY" if 168 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00169(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00169."""
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
            "corridor_id": "LOG-CORRIDOR-00169",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (169 % 7),
            "carrier_code": "DHL_EXPRESS" if 169 % 3 == 0 else "FEDEX_PRIORITY" if 169 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00170(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00170."""
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
            "corridor_id": "LOG-CORRIDOR-00170",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (170 % 7),
            "carrier_code": "DHL_EXPRESS" if 170 % 3 == 0 else "FEDEX_PRIORITY" if 170 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00171(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00171."""
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
            "corridor_id": "LOG-CORRIDOR-00171",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (171 % 7),
            "carrier_code": "DHL_EXPRESS" if 171 % 3 == 0 else "FEDEX_PRIORITY" if 171 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00172(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00172."""
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
            "corridor_id": "LOG-CORRIDOR-00172",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (172 % 7),
            "carrier_code": "DHL_EXPRESS" if 172 % 3 == 0 else "FEDEX_PRIORITY" if 172 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00173(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00173."""
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
            "corridor_id": "LOG-CORRIDOR-00173",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (173 % 7),
            "carrier_code": "DHL_EXPRESS" if 173 % 3 == 0 else "FEDEX_PRIORITY" if 173 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00174(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00174."""
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
            "corridor_id": "LOG-CORRIDOR-00174",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (174 % 7),
            "carrier_code": "DHL_EXPRESS" if 174 % 3 == 0 else "FEDEX_PRIORITY" if 174 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00175(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00175."""
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
            "corridor_id": "LOG-CORRIDOR-00175",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (175 % 7),
            "carrier_code": "DHL_EXPRESS" if 175 % 3 == 0 else "FEDEX_PRIORITY" if 175 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00176(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00176."""
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
            "corridor_id": "LOG-CORRIDOR-00176",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (176 % 7),
            "carrier_code": "DHL_EXPRESS" if 176 % 3 == 0 else "FEDEX_PRIORITY" if 176 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00177(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00177."""
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
            "corridor_id": "LOG-CORRIDOR-00177",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (177 % 7),
            "carrier_code": "DHL_EXPRESS" if 177 % 3 == 0 else "FEDEX_PRIORITY" if 177 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00178(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00178."""
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
            "corridor_id": "LOG-CORRIDOR-00178",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (178 % 7),
            "carrier_code": "DHL_EXPRESS" if 178 % 3 == 0 else "FEDEX_PRIORITY" if 178 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00179(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00179."""
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
            "corridor_id": "LOG-CORRIDOR-00179",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (179 % 7),
            "carrier_code": "DHL_EXPRESS" if 179 % 3 == 0 else "FEDEX_PRIORITY" if 179 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00180(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00180."""
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
            "corridor_id": "LOG-CORRIDOR-00180",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (180 % 7),
            "carrier_code": "DHL_EXPRESS" if 180 % 3 == 0 else "FEDEX_PRIORITY" if 180 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00181(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00181."""
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
            "corridor_id": "LOG-CORRIDOR-00181",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (181 % 7),
            "carrier_code": "DHL_EXPRESS" if 181 % 3 == 0 else "FEDEX_PRIORITY" if 181 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00182(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00182."""
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
            "corridor_id": "LOG-CORRIDOR-00182",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (182 % 7),
            "carrier_code": "DHL_EXPRESS" if 182 % 3 == 0 else "FEDEX_PRIORITY" if 182 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00183(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00183."""
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
            "corridor_id": "LOG-CORRIDOR-00183",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (183 % 7),
            "carrier_code": "DHL_EXPRESS" if 183 % 3 == 0 else "FEDEX_PRIORITY" if 183 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00184(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00184."""
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
            "corridor_id": "LOG-CORRIDOR-00184",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (184 % 7),
            "carrier_code": "DHL_EXPRESS" if 184 % 3 == 0 else "FEDEX_PRIORITY" if 184 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00185(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00185."""
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
            "corridor_id": "LOG-CORRIDOR-00185",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (185 % 7),
            "carrier_code": "DHL_EXPRESS" if 185 % 3 == 0 else "FEDEX_PRIORITY" if 185 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00186(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00186."""
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
            "corridor_id": "LOG-CORRIDOR-00186",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (186 % 7),
            "carrier_code": "DHL_EXPRESS" if 186 % 3 == 0 else "FEDEX_PRIORITY" if 186 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00187(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00187."""
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
            "corridor_id": "LOG-CORRIDOR-00187",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (187 % 7),
            "carrier_code": "DHL_EXPRESS" if 187 % 3 == 0 else "FEDEX_PRIORITY" if 187 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00188(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00188."""
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
            "corridor_id": "LOG-CORRIDOR-00188",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (188 % 7),
            "carrier_code": "DHL_EXPRESS" if 188 % 3 == 0 else "FEDEX_PRIORITY" if 188 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00189(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00189."""
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
            "corridor_id": "LOG-CORRIDOR-00189",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (189 % 7),
            "carrier_code": "DHL_EXPRESS" if 189 % 3 == 0 else "FEDEX_PRIORITY" if 189 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00190(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00190."""
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
            "corridor_id": "LOG-CORRIDOR-00190",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (190 % 7),
            "carrier_code": "DHL_EXPRESS" if 190 % 3 == 0 else "FEDEX_PRIORITY" if 190 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00191(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00191."""
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
            "corridor_id": "LOG-CORRIDOR-00191",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (191 % 7),
            "carrier_code": "DHL_EXPRESS" if 191 % 3 == 0 else "FEDEX_PRIORITY" if 191 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00192(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00192."""
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
            "corridor_id": "LOG-CORRIDOR-00192",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (192 % 7),
            "carrier_code": "DHL_EXPRESS" if 192 % 3 == 0 else "FEDEX_PRIORITY" if 192 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00193(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00193."""
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
            "corridor_id": "LOG-CORRIDOR-00193",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (193 % 7),
            "carrier_code": "DHL_EXPRESS" if 193 % 3 == 0 else "FEDEX_PRIORITY" if 193 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00194(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00194."""
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
            "corridor_id": "LOG-CORRIDOR-00194",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (194 % 7),
            "carrier_code": "DHL_EXPRESS" if 194 % 3 == 0 else "FEDEX_PRIORITY" if 194 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00195(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00195."""
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
            "corridor_id": "LOG-CORRIDOR-00195",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (195 % 7),
            "carrier_code": "DHL_EXPRESS" if 195 % 3 == 0 else "FEDEX_PRIORITY" if 195 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00196(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00196."""
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
            "corridor_id": "LOG-CORRIDOR-00196",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (196 % 7),
            "carrier_code": "DHL_EXPRESS" if 196 % 3 == 0 else "FEDEX_PRIORITY" if 196 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00197(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00197."""
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
            "corridor_id": "LOG-CORRIDOR-00197",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (197 % 7),
            "carrier_code": "DHL_EXPRESS" if 197 % 3 == 0 else "FEDEX_PRIORITY" if 197 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00198(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00198."""
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
            "corridor_id": "LOG-CORRIDOR-00198",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (198 % 7),
            "carrier_code": "DHL_EXPRESS" if 198 % 3 == 0 else "FEDEX_PRIORITY" if 198 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00199(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00199."""
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
            "corridor_id": "LOG-CORRIDOR-00199",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (199 % 7),
            "carrier_code": "DHL_EXPRESS" if 199 % 3 == 0 else "FEDEX_PRIORITY" if 199 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00200(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00200."""
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
            "corridor_id": "LOG-CORRIDOR-00200",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (200 % 7),
            "carrier_code": "DHL_EXPRESS" if 200 % 3 == 0 else "FEDEX_PRIORITY" if 200 % 3 == 1 else "UPS_SAVER",
        }
