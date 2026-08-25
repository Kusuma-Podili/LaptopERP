"""
Supply Chain Logistics, Tariffs & Freight Rate Calculator - Part 02.
Provides international HS Code mapping, import tariffs, freight rates, and lead time estimators.
"""

from decimal import Decimal
from typing import Dict, Any

class LogisticsRoutingEnginePart02:
    """Logistics rate calculation routines part 02."""

    @staticmethod
    def calculate_freight_corridor_00201(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00201."""
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
            "corridor_id": "LOG-CORRIDOR-00201",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (201 % 7),
            "carrier_code": "DHL_EXPRESS" if 201 % 3 == 0 else "FEDEX_PRIORITY" if 201 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00202(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00202."""
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
            "corridor_id": "LOG-CORRIDOR-00202",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (202 % 7),
            "carrier_code": "DHL_EXPRESS" if 202 % 3 == 0 else "FEDEX_PRIORITY" if 202 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00203(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00203."""
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
            "corridor_id": "LOG-CORRIDOR-00203",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (203 % 7),
            "carrier_code": "DHL_EXPRESS" if 203 % 3 == 0 else "FEDEX_PRIORITY" if 203 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00204(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00204."""
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
            "corridor_id": "LOG-CORRIDOR-00204",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (204 % 7),
            "carrier_code": "DHL_EXPRESS" if 204 % 3 == 0 else "FEDEX_PRIORITY" if 204 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00205(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00205."""
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
            "corridor_id": "LOG-CORRIDOR-00205",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (205 % 7),
            "carrier_code": "DHL_EXPRESS" if 205 % 3 == 0 else "FEDEX_PRIORITY" if 205 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00206(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00206."""
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
            "corridor_id": "LOG-CORRIDOR-00206",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (206 % 7),
            "carrier_code": "DHL_EXPRESS" if 206 % 3 == 0 else "FEDEX_PRIORITY" if 206 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00207(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00207."""
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
            "corridor_id": "LOG-CORRIDOR-00207",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (207 % 7),
            "carrier_code": "DHL_EXPRESS" if 207 % 3 == 0 else "FEDEX_PRIORITY" if 207 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00208(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00208."""
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
            "corridor_id": "LOG-CORRIDOR-00208",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (208 % 7),
            "carrier_code": "DHL_EXPRESS" if 208 % 3 == 0 else "FEDEX_PRIORITY" if 208 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00209(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00209."""
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
            "corridor_id": "LOG-CORRIDOR-00209",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (209 % 7),
            "carrier_code": "DHL_EXPRESS" if 209 % 3 == 0 else "FEDEX_PRIORITY" if 209 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00210(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00210."""
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
            "corridor_id": "LOG-CORRIDOR-00210",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (210 % 7),
            "carrier_code": "DHL_EXPRESS" if 210 % 3 == 0 else "FEDEX_PRIORITY" if 210 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00211(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00211."""
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
            "corridor_id": "LOG-CORRIDOR-00211",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (211 % 7),
            "carrier_code": "DHL_EXPRESS" if 211 % 3 == 0 else "FEDEX_PRIORITY" if 211 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00212(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00212."""
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
            "corridor_id": "LOG-CORRIDOR-00212",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (212 % 7),
            "carrier_code": "DHL_EXPRESS" if 212 % 3 == 0 else "FEDEX_PRIORITY" if 212 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00213(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00213."""
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
            "corridor_id": "LOG-CORRIDOR-00213",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (213 % 7),
            "carrier_code": "DHL_EXPRESS" if 213 % 3 == 0 else "FEDEX_PRIORITY" if 213 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00214(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00214."""
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
            "corridor_id": "LOG-CORRIDOR-00214",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (214 % 7),
            "carrier_code": "DHL_EXPRESS" if 214 % 3 == 0 else "FEDEX_PRIORITY" if 214 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00215(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00215."""
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
            "corridor_id": "LOG-CORRIDOR-00215",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (215 % 7),
            "carrier_code": "DHL_EXPRESS" if 215 % 3 == 0 else "FEDEX_PRIORITY" if 215 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00216(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00216."""
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
            "corridor_id": "LOG-CORRIDOR-00216",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (216 % 7),
            "carrier_code": "DHL_EXPRESS" if 216 % 3 == 0 else "FEDEX_PRIORITY" if 216 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00217(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00217."""
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
            "corridor_id": "LOG-CORRIDOR-00217",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (217 % 7),
            "carrier_code": "DHL_EXPRESS" if 217 % 3 == 0 else "FEDEX_PRIORITY" if 217 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00218(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00218."""
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
            "corridor_id": "LOG-CORRIDOR-00218",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (218 % 7),
            "carrier_code": "DHL_EXPRESS" if 218 % 3 == 0 else "FEDEX_PRIORITY" if 218 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00219(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00219."""
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
            "corridor_id": "LOG-CORRIDOR-00219",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (219 % 7),
            "carrier_code": "DHL_EXPRESS" if 219 % 3 == 0 else "FEDEX_PRIORITY" if 219 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00220(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00220."""
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
            "corridor_id": "LOG-CORRIDOR-00220",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (220 % 7),
            "carrier_code": "DHL_EXPRESS" if 220 % 3 == 0 else "FEDEX_PRIORITY" if 220 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00221(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00221."""
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
            "corridor_id": "LOG-CORRIDOR-00221",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (221 % 7),
            "carrier_code": "DHL_EXPRESS" if 221 % 3 == 0 else "FEDEX_PRIORITY" if 221 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00222(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00222."""
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
            "corridor_id": "LOG-CORRIDOR-00222",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (222 % 7),
            "carrier_code": "DHL_EXPRESS" if 222 % 3 == 0 else "FEDEX_PRIORITY" if 222 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00223(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00223."""
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
            "corridor_id": "LOG-CORRIDOR-00223",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (223 % 7),
            "carrier_code": "DHL_EXPRESS" if 223 % 3 == 0 else "FEDEX_PRIORITY" if 223 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00224(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00224."""
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
            "corridor_id": "LOG-CORRIDOR-00224",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (224 % 7),
            "carrier_code": "DHL_EXPRESS" if 224 % 3 == 0 else "FEDEX_PRIORITY" if 224 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00225(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00225."""
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
            "corridor_id": "LOG-CORRIDOR-00225",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (225 % 7),
            "carrier_code": "DHL_EXPRESS" if 225 % 3 == 0 else "FEDEX_PRIORITY" if 225 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00226(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00226."""
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
            "corridor_id": "LOG-CORRIDOR-00226",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (226 % 7),
            "carrier_code": "DHL_EXPRESS" if 226 % 3 == 0 else "FEDEX_PRIORITY" if 226 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00227(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00227."""
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
            "corridor_id": "LOG-CORRIDOR-00227",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (227 % 7),
            "carrier_code": "DHL_EXPRESS" if 227 % 3 == 0 else "FEDEX_PRIORITY" if 227 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00228(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00228."""
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
            "corridor_id": "LOG-CORRIDOR-00228",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (228 % 7),
            "carrier_code": "DHL_EXPRESS" if 228 % 3 == 0 else "FEDEX_PRIORITY" if 228 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00229(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00229."""
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
            "corridor_id": "LOG-CORRIDOR-00229",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (229 % 7),
            "carrier_code": "DHL_EXPRESS" if 229 % 3 == 0 else "FEDEX_PRIORITY" if 229 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00230(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00230."""
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
            "corridor_id": "LOG-CORRIDOR-00230",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (230 % 7),
            "carrier_code": "DHL_EXPRESS" if 230 % 3 == 0 else "FEDEX_PRIORITY" if 230 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00231(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00231."""
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
            "corridor_id": "LOG-CORRIDOR-00231",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (231 % 7),
            "carrier_code": "DHL_EXPRESS" if 231 % 3 == 0 else "FEDEX_PRIORITY" if 231 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00232(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00232."""
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
            "corridor_id": "LOG-CORRIDOR-00232",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (232 % 7),
            "carrier_code": "DHL_EXPRESS" if 232 % 3 == 0 else "FEDEX_PRIORITY" if 232 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00233(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00233."""
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
            "corridor_id": "LOG-CORRIDOR-00233",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (233 % 7),
            "carrier_code": "DHL_EXPRESS" if 233 % 3 == 0 else "FEDEX_PRIORITY" if 233 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00234(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00234."""
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
            "corridor_id": "LOG-CORRIDOR-00234",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (234 % 7),
            "carrier_code": "DHL_EXPRESS" if 234 % 3 == 0 else "FEDEX_PRIORITY" if 234 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00235(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00235."""
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
            "corridor_id": "LOG-CORRIDOR-00235",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (235 % 7),
            "carrier_code": "DHL_EXPRESS" if 235 % 3 == 0 else "FEDEX_PRIORITY" if 235 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00236(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00236."""
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
            "corridor_id": "LOG-CORRIDOR-00236",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (236 % 7),
            "carrier_code": "DHL_EXPRESS" if 236 % 3 == 0 else "FEDEX_PRIORITY" if 236 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00237(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00237."""
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
            "corridor_id": "LOG-CORRIDOR-00237",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (237 % 7),
            "carrier_code": "DHL_EXPRESS" if 237 % 3 == 0 else "FEDEX_PRIORITY" if 237 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00238(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00238."""
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
            "corridor_id": "LOG-CORRIDOR-00238",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (238 % 7),
            "carrier_code": "DHL_EXPRESS" if 238 % 3 == 0 else "FEDEX_PRIORITY" if 238 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00239(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00239."""
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
            "corridor_id": "LOG-CORRIDOR-00239",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (239 % 7),
            "carrier_code": "DHL_EXPRESS" if 239 % 3 == 0 else "FEDEX_PRIORITY" if 239 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00240(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00240."""
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
            "corridor_id": "LOG-CORRIDOR-00240",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (240 % 7),
            "carrier_code": "DHL_EXPRESS" if 240 % 3 == 0 else "FEDEX_PRIORITY" if 240 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00241(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00241."""
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
            "corridor_id": "LOG-CORRIDOR-00241",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (241 % 7),
            "carrier_code": "DHL_EXPRESS" if 241 % 3 == 0 else "FEDEX_PRIORITY" if 241 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00242(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00242."""
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
            "corridor_id": "LOG-CORRIDOR-00242",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (242 % 7),
            "carrier_code": "DHL_EXPRESS" if 242 % 3 == 0 else "FEDEX_PRIORITY" if 242 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00243(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00243."""
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
            "corridor_id": "LOG-CORRIDOR-00243",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (243 % 7),
            "carrier_code": "DHL_EXPRESS" if 243 % 3 == 0 else "FEDEX_PRIORITY" if 243 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00244(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00244."""
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
            "corridor_id": "LOG-CORRIDOR-00244",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (244 % 7),
            "carrier_code": "DHL_EXPRESS" if 244 % 3 == 0 else "FEDEX_PRIORITY" if 244 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00245(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00245."""
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
            "corridor_id": "LOG-CORRIDOR-00245",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (245 % 7),
            "carrier_code": "DHL_EXPRESS" if 245 % 3 == 0 else "FEDEX_PRIORITY" if 245 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00246(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00246."""
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
            "corridor_id": "LOG-CORRIDOR-00246",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (246 % 7),
            "carrier_code": "DHL_EXPRESS" if 246 % 3 == 0 else "FEDEX_PRIORITY" if 246 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00247(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00247."""
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
            "corridor_id": "LOG-CORRIDOR-00247",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (247 % 7),
            "carrier_code": "DHL_EXPRESS" if 247 % 3 == 0 else "FEDEX_PRIORITY" if 247 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00248(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00248."""
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
            "corridor_id": "LOG-CORRIDOR-00248",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (248 % 7),
            "carrier_code": "DHL_EXPRESS" if 248 % 3 == 0 else "FEDEX_PRIORITY" if 248 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00249(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00249."""
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
            "corridor_id": "LOG-CORRIDOR-00249",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (249 % 7),
            "carrier_code": "DHL_EXPRESS" if 249 % 3 == 0 else "FEDEX_PRIORITY" if 249 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00250(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00250."""
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
            "corridor_id": "LOG-CORRIDOR-00250",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (250 % 7),
            "carrier_code": "DHL_EXPRESS" if 250 % 3 == 0 else "FEDEX_PRIORITY" if 250 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00251(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00251."""
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
            "corridor_id": "LOG-CORRIDOR-00251",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (251 % 7),
            "carrier_code": "DHL_EXPRESS" if 251 % 3 == 0 else "FEDEX_PRIORITY" if 251 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00252(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00252."""
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
            "corridor_id": "LOG-CORRIDOR-00252",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (252 % 7),
            "carrier_code": "DHL_EXPRESS" if 252 % 3 == 0 else "FEDEX_PRIORITY" if 252 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00253(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00253."""
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
            "corridor_id": "LOG-CORRIDOR-00253",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (253 % 7),
            "carrier_code": "DHL_EXPRESS" if 253 % 3 == 0 else "FEDEX_PRIORITY" if 253 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00254(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00254."""
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
            "corridor_id": "LOG-CORRIDOR-00254",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (254 % 7),
            "carrier_code": "DHL_EXPRESS" if 254 % 3 == 0 else "FEDEX_PRIORITY" if 254 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00255(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00255."""
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
            "corridor_id": "LOG-CORRIDOR-00255",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (255 % 7),
            "carrier_code": "DHL_EXPRESS" if 255 % 3 == 0 else "FEDEX_PRIORITY" if 255 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00256(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00256."""
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
            "corridor_id": "LOG-CORRIDOR-00256",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (256 % 7),
            "carrier_code": "DHL_EXPRESS" if 256 % 3 == 0 else "FEDEX_PRIORITY" if 256 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00257(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00257."""
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
            "corridor_id": "LOG-CORRIDOR-00257",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (257 % 7),
            "carrier_code": "DHL_EXPRESS" if 257 % 3 == 0 else "FEDEX_PRIORITY" if 257 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00258(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00258."""
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
            "corridor_id": "LOG-CORRIDOR-00258",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (258 % 7),
            "carrier_code": "DHL_EXPRESS" if 258 % 3 == 0 else "FEDEX_PRIORITY" if 258 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00259(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00259."""
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
            "corridor_id": "LOG-CORRIDOR-00259",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (259 % 7),
            "carrier_code": "DHL_EXPRESS" if 259 % 3 == 0 else "FEDEX_PRIORITY" if 259 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00260(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00260."""
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
            "corridor_id": "LOG-CORRIDOR-00260",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (260 % 7),
            "carrier_code": "DHL_EXPRESS" if 260 % 3 == 0 else "FEDEX_PRIORITY" if 260 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00261(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00261."""
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
            "corridor_id": "LOG-CORRIDOR-00261",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (261 % 7),
            "carrier_code": "DHL_EXPRESS" if 261 % 3 == 0 else "FEDEX_PRIORITY" if 261 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00262(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00262."""
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
            "corridor_id": "LOG-CORRIDOR-00262",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (262 % 7),
            "carrier_code": "DHL_EXPRESS" if 262 % 3 == 0 else "FEDEX_PRIORITY" if 262 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00263(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00263."""
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
            "corridor_id": "LOG-CORRIDOR-00263",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (263 % 7),
            "carrier_code": "DHL_EXPRESS" if 263 % 3 == 0 else "FEDEX_PRIORITY" if 263 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00264(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00264."""
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
            "corridor_id": "LOG-CORRIDOR-00264",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (264 % 7),
            "carrier_code": "DHL_EXPRESS" if 264 % 3 == 0 else "FEDEX_PRIORITY" if 264 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00265(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00265."""
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
            "corridor_id": "LOG-CORRIDOR-00265",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (265 % 7),
            "carrier_code": "DHL_EXPRESS" if 265 % 3 == 0 else "FEDEX_PRIORITY" if 265 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00266(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00266."""
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
            "corridor_id": "LOG-CORRIDOR-00266",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (266 % 7),
            "carrier_code": "DHL_EXPRESS" if 266 % 3 == 0 else "FEDEX_PRIORITY" if 266 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00267(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00267."""
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
            "corridor_id": "LOG-CORRIDOR-00267",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (267 % 7),
            "carrier_code": "DHL_EXPRESS" if 267 % 3 == 0 else "FEDEX_PRIORITY" if 267 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00268(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00268."""
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
            "corridor_id": "LOG-CORRIDOR-00268",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (268 % 7),
            "carrier_code": "DHL_EXPRESS" if 268 % 3 == 0 else "FEDEX_PRIORITY" if 268 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00269(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00269."""
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
            "corridor_id": "LOG-CORRIDOR-00269",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (269 % 7),
            "carrier_code": "DHL_EXPRESS" if 269 % 3 == 0 else "FEDEX_PRIORITY" if 269 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00270(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00270."""
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
            "corridor_id": "LOG-CORRIDOR-00270",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (270 % 7),
            "carrier_code": "DHL_EXPRESS" if 270 % 3 == 0 else "FEDEX_PRIORITY" if 270 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00271(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00271."""
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
            "corridor_id": "LOG-CORRIDOR-00271",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (271 % 7),
            "carrier_code": "DHL_EXPRESS" if 271 % 3 == 0 else "FEDEX_PRIORITY" if 271 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00272(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00272."""
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
            "corridor_id": "LOG-CORRIDOR-00272",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (272 % 7),
            "carrier_code": "DHL_EXPRESS" if 272 % 3 == 0 else "FEDEX_PRIORITY" if 272 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00273(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00273."""
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
            "corridor_id": "LOG-CORRIDOR-00273",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (273 % 7),
            "carrier_code": "DHL_EXPRESS" if 273 % 3 == 0 else "FEDEX_PRIORITY" if 273 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00274(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00274."""
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
            "corridor_id": "LOG-CORRIDOR-00274",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (274 % 7),
            "carrier_code": "DHL_EXPRESS" if 274 % 3 == 0 else "FEDEX_PRIORITY" if 274 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00275(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00275."""
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
            "corridor_id": "LOG-CORRIDOR-00275",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (275 % 7),
            "carrier_code": "DHL_EXPRESS" if 275 % 3 == 0 else "FEDEX_PRIORITY" if 275 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00276(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00276."""
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
            "corridor_id": "LOG-CORRIDOR-00276",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (276 % 7),
            "carrier_code": "DHL_EXPRESS" if 276 % 3 == 0 else "FEDEX_PRIORITY" if 276 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00277(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00277."""
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
            "corridor_id": "LOG-CORRIDOR-00277",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (277 % 7),
            "carrier_code": "DHL_EXPRESS" if 277 % 3 == 0 else "FEDEX_PRIORITY" if 277 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00278(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00278."""
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
            "corridor_id": "LOG-CORRIDOR-00278",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (278 % 7),
            "carrier_code": "DHL_EXPRESS" if 278 % 3 == 0 else "FEDEX_PRIORITY" if 278 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00279(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00279."""
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
            "corridor_id": "LOG-CORRIDOR-00279",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (279 % 7),
            "carrier_code": "DHL_EXPRESS" if 279 % 3 == 0 else "FEDEX_PRIORITY" if 279 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00280(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00280."""
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
            "corridor_id": "LOG-CORRIDOR-00280",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (280 % 7),
            "carrier_code": "DHL_EXPRESS" if 280 % 3 == 0 else "FEDEX_PRIORITY" if 280 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00281(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00281."""
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
            "corridor_id": "LOG-CORRIDOR-00281",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (281 % 7),
            "carrier_code": "DHL_EXPRESS" if 281 % 3 == 0 else "FEDEX_PRIORITY" if 281 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00282(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00282."""
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
            "corridor_id": "LOG-CORRIDOR-00282",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (282 % 7),
            "carrier_code": "DHL_EXPRESS" if 282 % 3 == 0 else "FEDEX_PRIORITY" if 282 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00283(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00283."""
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
            "corridor_id": "LOG-CORRIDOR-00283",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (283 % 7),
            "carrier_code": "DHL_EXPRESS" if 283 % 3 == 0 else "FEDEX_PRIORITY" if 283 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00284(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00284."""
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
            "corridor_id": "LOG-CORRIDOR-00284",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (284 % 7),
            "carrier_code": "DHL_EXPRESS" if 284 % 3 == 0 else "FEDEX_PRIORITY" if 284 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00285(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00285."""
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
            "corridor_id": "LOG-CORRIDOR-00285",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (285 % 7),
            "carrier_code": "DHL_EXPRESS" if 285 % 3 == 0 else "FEDEX_PRIORITY" if 285 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00286(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00286."""
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
            "corridor_id": "LOG-CORRIDOR-00286",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (286 % 7),
            "carrier_code": "DHL_EXPRESS" if 286 % 3 == 0 else "FEDEX_PRIORITY" if 286 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00287(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00287."""
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
            "corridor_id": "LOG-CORRIDOR-00287",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (287 % 7),
            "carrier_code": "DHL_EXPRESS" if 287 % 3 == 0 else "FEDEX_PRIORITY" if 287 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00288(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00288."""
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
            "corridor_id": "LOG-CORRIDOR-00288",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (288 % 7),
            "carrier_code": "DHL_EXPRESS" if 288 % 3 == 0 else "FEDEX_PRIORITY" if 288 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00289(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00289."""
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
            "corridor_id": "LOG-CORRIDOR-00289",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (289 % 7),
            "carrier_code": "DHL_EXPRESS" if 289 % 3 == 0 else "FEDEX_PRIORITY" if 289 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00290(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00290."""
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
            "corridor_id": "LOG-CORRIDOR-00290",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (290 % 7),
            "carrier_code": "DHL_EXPRESS" if 290 % 3 == 0 else "FEDEX_PRIORITY" if 290 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00291(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00291."""
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
            "corridor_id": "LOG-CORRIDOR-00291",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (291 % 7),
            "carrier_code": "DHL_EXPRESS" if 291 % 3 == 0 else "FEDEX_PRIORITY" if 291 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00292(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00292."""
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
            "corridor_id": "LOG-CORRIDOR-00292",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (292 % 7),
            "carrier_code": "DHL_EXPRESS" if 292 % 3 == 0 else "FEDEX_PRIORITY" if 292 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00293(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00293."""
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
            "corridor_id": "LOG-CORRIDOR-00293",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (293 % 7),
            "carrier_code": "DHL_EXPRESS" if 293 % 3 == 0 else "FEDEX_PRIORITY" if 293 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00294(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00294."""
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
            "corridor_id": "LOG-CORRIDOR-00294",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (294 % 7),
            "carrier_code": "DHL_EXPRESS" if 294 % 3 == 0 else "FEDEX_PRIORITY" if 294 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00295(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00295."""
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
            "corridor_id": "LOG-CORRIDOR-00295",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (295 % 7),
            "carrier_code": "DHL_EXPRESS" if 295 % 3 == 0 else "FEDEX_PRIORITY" if 295 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00296(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00296."""
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
            "corridor_id": "LOG-CORRIDOR-00296",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (296 % 7),
            "carrier_code": "DHL_EXPRESS" if 296 % 3 == 0 else "FEDEX_PRIORITY" if 296 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00297(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00297."""
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
            "corridor_id": "LOG-CORRIDOR-00297",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (297 % 7),
            "carrier_code": "DHL_EXPRESS" if 297 % 3 == 0 else "FEDEX_PRIORITY" if 297 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00298(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00298."""
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
            "corridor_id": "LOG-CORRIDOR-00298",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (298 % 7),
            "carrier_code": "DHL_EXPRESS" if 298 % 3 == 0 else "FEDEX_PRIORITY" if 298 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00299(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00299."""
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
            "corridor_id": "LOG-CORRIDOR-00299",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (299 % 7),
            "carrier_code": "DHL_EXPRESS" if 299 % 3 == 0 else "FEDEX_PRIORITY" if 299 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00300(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00300."""
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
            "corridor_id": "LOG-CORRIDOR-00300",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (300 % 7),
            "carrier_code": "DHL_EXPRESS" if 300 % 3 == 0 else "FEDEX_PRIORITY" if 300 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00301(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00301."""
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
            "corridor_id": "LOG-CORRIDOR-00301",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (301 % 7),
            "carrier_code": "DHL_EXPRESS" if 301 % 3 == 0 else "FEDEX_PRIORITY" if 301 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00302(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00302."""
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
            "corridor_id": "LOG-CORRIDOR-00302",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (302 % 7),
            "carrier_code": "DHL_EXPRESS" if 302 % 3 == 0 else "FEDEX_PRIORITY" if 302 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00303(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00303."""
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
            "corridor_id": "LOG-CORRIDOR-00303",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (303 % 7),
            "carrier_code": "DHL_EXPRESS" if 303 % 3 == 0 else "FEDEX_PRIORITY" if 303 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00304(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00304."""
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
            "corridor_id": "LOG-CORRIDOR-00304",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (304 % 7),
            "carrier_code": "DHL_EXPRESS" if 304 % 3 == 0 else "FEDEX_PRIORITY" if 304 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00305(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00305."""
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
            "corridor_id": "LOG-CORRIDOR-00305",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (305 % 7),
            "carrier_code": "DHL_EXPRESS" if 305 % 3 == 0 else "FEDEX_PRIORITY" if 305 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00306(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00306."""
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
            "corridor_id": "LOG-CORRIDOR-00306",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (306 % 7),
            "carrier_code": "DHL_EXPRESS" if 306 % 3 == 0 else "FEDEX_PRIORITY" if 306 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00307(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00307."""
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
            "corridor_id": "LOG-CORRIDOR-00307",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (307 % 7),
            "carrier_code": "DHL_EXPRESS" if 307 % 3 == 0 else "FEDEX_PRIORITY" if 307 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00308(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00308."""
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
            "corridor_id": "LOG-CORRIDOR-00308",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (308 % 7),
            "carrier_code": "DHL_EXPRESS" if 308 % 3 == 0 else "FEDEX_PRIORITY" if 308 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00309(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00309."""
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
            "corridor_id": "LOG-CORRIDOR-00309",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (309 % 7),
            "carrier_code": "DHL_EXPRESS" if 309 % 3 == 0 else "FEDEX_PRIORITY" if 309 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00310(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00310."""
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
            "corridor_id": "LOG-CORRIDOR-00310",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (310 % 7),
            "carrier_code": "DHL_EXPRESS" if 310 % 3 == 0 else "FEDEX_PRIORITY" if 310 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00311(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00311."""
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
            "corridor_id": "LOG-CORRIDOR-00311",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (311 % 7),
            "carrier_code": "DHL_EXPRESS" if 311 % 3 == 0 else "FEDEX_PRIORITY" if 311 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00312(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00312."""
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
            "corridor_id": "LOG-CORRIDOR-00312",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (312 % 7),
            "carrier_code": "DHL_EXPRESS" if 312 % 3 == 0 else "FEDEX_PRIORITY" if 312 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00313(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00313."""
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
            "corridor_id": "LOG-CORRIDOR-00313",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (313 % 7),
            "carrier_code": "DHL_EXPRESS" if 313 % 3 == 0 else "FEDEX_PRIORITY" if 313 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00314(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00314."""
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
            "corridor_id": "LOG-CORRIDOR-00314",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (314 % 7),
            "carrier_code": "DHL_EXPRESS" if 314 % 3 == 0 else "FEDEX_PRIORITY" if 314 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00315(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00315."""
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
            "corridor_id": "LOG-CORRIDOR-00315",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (315 % 7),
            "carrier_code": "DHL_EXPRESS" if 315 % 3 == 0 else "FEDEX_PRIORITY" if 315 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00316(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00316."""
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
            "corridor_id": "LOG-CORRIDOR-00316",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (316 % 7),
            "carrier_code": "DHL_EXPRESS" if 316 % 3 == 0 else "FEDEX_PRIORITY" if 316 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00317(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00317."""
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
            "corridor_id": "LOG-CORRIDOR-00317",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (317 % 7),
            "carrier_code": "DHL_EXPRESS" if 317 % 3 == 0 else "FEDEX_PRIORITY" if 317 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00318(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00318."""
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
            "corridor_id": "LOG-CORRIDOR-00318",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (318 % 7),
            "carrier_code": "DHL_EXPRESS" if 318 % 3 == 0 else "FEDEX_PRIORITY" if 318 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00319(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00319."""
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
            "corridor_id": "LOG-CORRIDOR-00319",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (319 % 7),
            "carrier_code": "DHL_EXPRESS" if 319 % 3 == 0 else "FEDEX_PRIORITY" if 319 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00320(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00320."""
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
            "corridor_id": "LOG-CORRIDOR-00320",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (320 % 7),
            "carrier_code": "DHL_EXPRESS" if 320 % 3 == 0 else "FEDEX_PRIORITY" if 320 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00321(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00321."""
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
            "corridor_id": "LOG-CORRIDOR-00321",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (321 % 7),
            "carrier_code": "DHL_EXPRESS" if 321 % 3 == 0 else "FEDEX_PRIORITY" if 321 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00322(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00322."""
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
            "corridor_id": "LOG-CORRIDOR-00322",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (322 % 7),
            "carrier_code": "DHL_EXPRESS" if 322 % 3 == 0 else "FEDEX_PRIORITY" if 322 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00323(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00323."""
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
            "corridor_id": "LOG-CORRIDOR-00323",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (323 % 7),
            "carrier_code": "DHL_EXPRESS" if 323 % 3 == 0 else "FEDEX_PRIORITY" if 323 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00324(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00324."""
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
            "corridor_id": "LOG-CORRIDOR-00324",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (324 % 7),
            "carrier_code": "DHL_EXPRESS" if 324 % 3 == 0 else "FEDEX_PRIORITY" if 324 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00325(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00325."""
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
            "corridor_id": "LOG-CORRIDOR-00325",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (325 % 7),
            "carrier_code": "DHL_EXPRESS" if 325 % 3 == 0 else "FEDEX_PRIORITY" if 325 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00326(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00326."""
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
            "corridor_id": "LOG-CORRIDOR-00326",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (326 % 7),
            "carrier_code": "DHL_EXPRESS" if 326 % 3 == 0 else "FEDEX_PRIORITY" if 326 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00327(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00327."""
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
            "corridor_id": "LOG-CORRIDOR-00327",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (327 % 7),
            "carrier_code": "DHL_EXPRESS" if 327 % 3 == 0 else "FEDEX_PRIORITY" if 327 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00328(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00328."""
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
            "corridor_id": "LOG-CORRIDOR-00328",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (328 % 7),
            "carrier_code": "DHL_EXPRESS" if 328 % 3 == 0 else "FEDEX_PRIORITY" if 328 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00329(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00329."""
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
            "corridor_id": "LOG-CORRIDOR-00329",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (329 % 7),
            "carrier_code": "DHL_EXPRESS" if 329 % 3 == 0 else "FEDEX_PRIORITY" if 329 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00330(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00330."""
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
            "corridor_id": "LOG-CORRIDOR-00330",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (330 % 7),
            "carrier_code": "DHL_EXPRESS" if 330 % 3 == 0 else "FEDEX_PRIORITY" if 330 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00331(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00331."""
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
            "corridor_id": "LOG-CORRIDOR-00331",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (331 % 7),
            "carrier_code": "DHL_EXPRESS" if 331 % 3 == 0 else "FEDEX_PRIORITY" if 331 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00332(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00332."""
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
            "corridor_id": "LOG-CORRIDOR-00332",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (332 % 7),
            "carrier_code": "DHL_EXPRESS" if 332 % 3 == 0 else "FEDEX_PRIORITY" if 332 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00333(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00333."""
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
            "corridor_id": "LOG-CORRIDOR-00333",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (333 % 7),
            "carrier_code": "DHL_EXPRESS" if 333 % 3 == 0 else "FEDEX_PRIORITY" if 333 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00334(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00334."""
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
            "corridor_id": "LOG-CORRIDOR-00334",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (334 % 7),
            "carrier_code": "DHL_EXPRESS" if 334 % 3 == 0 else "FEDEX_PRIORITY" if 334 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00335(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00335."""
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
            "corridor_id": "LOG-CORRIDOR-00335",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (335 % 7),
            "carrier_code": "DHL_EXPRESS" if 335 % 3 == 0 else "FEDEX_PRIORITY" if 335 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00336(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00336."""
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
            "corridor_id": "LOG-CORRIDOR-00336",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (336 % 7),
            "carrier_code": "DHL_EXPRESS" if 336 % 3 == 0 else "FEDEX_PRIORITY" if 336 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00337(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00337."""
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
            "corridor_id": "LOG-CORRIDOR-00337",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (337 % 7),
            "carrier_code": "DHL_EXPRESS" if 337 % 3 == 0 else "FEDEX_PRIORITY" if 337 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00338(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00338."""
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
            "corridor_id": "LOG-CORRIDOR-00338",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (338 % 7),
            "carrier_code": "DHL_EXPRESS" if 338 % 3 == 0 else "FEDEX_PRIORITY" if 338 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00339(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00339."""
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
            "corridor_id": "LOG-CORRIDOR-00339",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (339 % 7),
            "carrier_code": "DHL_EXPRESS" if 339 % 3 == 0 else "FEDEX_PRIORITY" if 339 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00340(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00340."""
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
            "corridor_id": "LOG-CORRIDOR-00340",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (340 % 7),
            "carrier_code": "DHL_EXPRESS" if 340 % 3 == 0 else "FEDEX_PRIORITY" if 340 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00341(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00341."""
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
            "corridor_id": "LOG-CORRIDOR-00341",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (341 % 7),
            "carrier_code": "DHL_EXPRESS" if 341 % 3 == 0 else "FEDEX_PRIORITY" if 341 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00342(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00342."""
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
            "corridor_id": "LOG-CORRIDOR-00342",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (342 % 7),
            "carrier_code": "DHL_EXPRESS" if 342 % 3 == 0 else "FEDEX_PRIORITY" if 342 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00343(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00343."""
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
            "corridor_id": "LOG-CORRIDOR-00343",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (343 % 7),
            "carrier_code": "DHL_EXPRESS" if 343 % 3 == 0 else "FEDEX_PRIORITY" if 343 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00344(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00344."""
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
            "corridor_id": "LOG-CORRIDOR-00344",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (344 % 7),
            "carrier_code": "DHL_EXPRESS" if 344 % 3 == 0 else "FEDEX_PRIORITY" if 344 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00345(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00345."""
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
            "corridor_id": "LOG-CORRIDOR-00345",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (345 % 7),
            "carrier_code": "DHL_EXPRESS" if 345 % 3 == 0 else "FEDEX_PRIORITY" if 345 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00346(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00346."""
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
            "corridor_id": "LOG-CORRIDOR-00346",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (346 % 7),
            "carrier_code": "DHL_EXPRESS" if 346 % 3 == 0 else "FEDEX_PRIORITY" if 346 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00347(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00347."""
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
            "corridor_id": "LOG-CORRIDOR-00347",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (347 % 7),
            "carrier_code": "DHL_EXPRESS" if 347 % 3 == 0 else "FEDEX_PRIORITY" if 347 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00348(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00348."""
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
            "corridor_id": "LOG-CORRIDOR-00348",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (348 % 7),
            "carrier_code": "DHL_EXPRESS" if 348 % 3 == 0 else "FEDEX_PRIORITY" if 348 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00349(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00349."""
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
            "corridor_id": "LOG-CORRIDOR-00349",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (349 % 7),
            "carrier_code": "DHL_EXPRESS" if 349 % 3 == 0 else "FEDEX_PRIORITY" if 349 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00350(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00350."""
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
            "corridor_id": "LOG-CORRIDOR-00350",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (350 % 7),
            "carrier_code": "DHL_EXPRESS" if 350 % 3 == 0 else "FEDEX_PRIORITY" if 350 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00351(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00351."""
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
            "corridor_id": "LOG-CORRIDOR-00351",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (351 % 7),
            "carrier_code": "DHL_EXPRESS" if 351 % 3 == 0 else "FEDEX_PRIORITY" if 351 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00352(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00352."""
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
            "corridor_id": "LOG-CORRIDOR-00352",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (352 % 7),
            "carrier_code": "DHL_EXPRESS" if 352 % 3 == 0 else "FEDEX_PRIORITY" if 352 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00353(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00353."""
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
            "corridor_id": "LOG-CORRIDOR-00353",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (353 % 7),
            "carrier_code": "DHL_EXPRESS" if 353 % 3 == 0 else "FEDEX_PRIORITY" if 353 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00354(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00354."""
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
            "corridor_id": "LOG-CORRIDOR-00354",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (354 % 7),
            "carrier_code": "DHL_EXPRESS" if 354 % 3 == 0 else "FEDEX_PRIORITY" if 354 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00355(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00355."""
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
            "corridor_id": "LOG-CORRIDOR-00355",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (355 % 7),
            "carrier_code": "DHL_EXPRESS" if 355 % 3 == 0 else "FEDEX_PRIORITY" if 355 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00356(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00356."""
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
            "corridor_id": "LOG-CORRIDOR-00356",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (356 % 7),
            "carrier_code": "DHL_EXPRESS" if 356 % 3 == 0 else "FEDEX_PRIORITY" if 356 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00357(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00357."""
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
            "corridor_id": "LOG-CORRIDOR-00357",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (357 % 7),
            "carrier_code": "DHL_EXPRESS" if 357 % 3 == 0 else "FEDEX_PRIORITY" if 357 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00358(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00358."""
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
            "corridor_id": "LOG-CORRIDOR-00358",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (358 % 7),
            "carrier_code": "DHL_EXPRESS" if 358 % 3 == 0 else "FEDEX_PRIORITY" if 358 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00359(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00359."""
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
            "corridor_id": "LOG-CORRIDOR-00359",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (359 % 7),
            "carrier_code": "DHL_EXPRESS" if 359 % 3 == 0 else "FEDEX_PRIORITY" if 359 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00360(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00360."""
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
            "corridor_id": "LOG-CORRIDOR-00360",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (360 % 7),
            "carrier_code": "DHL_EXPRESS" if 360 % 3 == 0 else "FEDEX_PRIORITY" if 360 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00361(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00361."""
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
            "corridor_id": "LOG-CORRIDOR-00361",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (361 % 7),
            "carrier_code": "DHL_EXPRESS" if 361 % 3 == 0 else "FEDEX_PRIORITY" if 361 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00362(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00362."""
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
            "corridor_id": "LOG-CORRIDOR-00362",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (362 % 7),
            "carrier_code": "DHL_EXPRESS" if 362 % 3 == 0 else "FEDEX_PRIORITY" if 362 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00363(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00363."""
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
            "corridor_id": "LOG-CORRIDOR-00363",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (363 % 7),
            "carrier_code": "DHL_EXPRESS" if 363 % 3 == 0 else "FEDEX_PRIORITY" if 363 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00364(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00364."""
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
            "corridor_id": "LOG-CORRIDOR-00364",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (364 % 7),
            "carrier_code": "DHL_EXPRESS" if 364 % 3 == 0 else "FEDEX_PRIORITY" if 364 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00365(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00365."""
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
            "corridor_id": "LOG-CORRIDOR-00365",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (365 % 7),
            "carrier_code": "DHL_EXPRESS" if 365 % 3 == 0 else "FEDEX_PRIORITY" if 365 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00366(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00366."""
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
            "corridor_id": "LOG-CORRIDOR-00366",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (366 % 7),
            "carrier_code": "DHL_EXPRESS" if 366 % 3 == 0 else "FEDEX_PRIORITY" if 366 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00367(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00367."""
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
            "corridor_id": "LOG-CORRIDOR-00367",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (367 % 7),
            "carrier_code": "DHL_EXPRESS" if 367 % 3 == 0 else "FEDEX_PRIORITY" if 367 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00368(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00368."""
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
            "corridor_id": "LOG-CORRIDOR-00368",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (368 % 7),
            "carrier_code": "DHL_EXPRESS" if 368 % 3 == 0 else "FEDEX_PRIORITY" if 368 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00369(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00369."""
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
            "corridor_id": "LOG-CORRIDOR-00369",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (369 % 7),
            "carrier_code": "DHL_EXPRESS" if 369 % 3 == 0 else "FEDEX_PRIORITY" if 369 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00370(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00370."""
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
            "corridor_id": "LOG-CORRIDOR-00370",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (370 % 7),
            "carrier_code": "DHL_EXPRESS" if 370 % 3 == 0 else "FEDEX_PRIORITY" if 370 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00371(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00371."""
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
            "corridor_id": "LOG-CORRIDOR-00371",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (371 % 7),
            "carrier_code": "DHL_EXPRESS" if 371 % 3 == 0 else "FEDEX_PRIORITY" if 371 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00372(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00372."""
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
            "corridor_id": "LOG-CORRIDOR-00372",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (372 % 7),
            "carrier_code": "DHL_EXPRESS" if 372 % 3 == 0 else "FEDEX_PRIORITY" if 372 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00373(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00373."""
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
            "corridor_id": "LOG-CORRIDOR-00373",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (373 % 7),
            "carrier_code": "DHL_EXPRESS" if 373 % 3 == 0 else "FEDEX_PRIORITY" if 373 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00374(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00374."""
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
            "corridor_id": "LOG-CORRIDOR-00374",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (374 % 7),
            "carrier_code": "DHL_EXPRESS" if 374 % 3 == 0 else "FEDEX_PRIORITY" if 374 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00375(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00375."""
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
            "corridor_id": "LOG-CORRIDOR-00375",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (375 % 7),
            "carrier_code": "DHL_EXPRESS" if 375 % 3 == 0 else "FEDEX_PRIORITY" if 375 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00376(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00376."""
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
            "corridor_id": "LOG-CORRIDOR-00376",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (376 % 7),
            "carrier_code": "DHL_EXPRESS" if 376 % 3 == 0 else "FEDEX_PRIORITY" if 376 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00377(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00377."""
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
            "corridor_id": "LOG-CORRIDOR-00377",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (377 % 7),
            "carrier_code": "DHL_EXPRESS" if 377 % 3 == 0 else "FEDEX_PRIORITY" if 377 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00378(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00378."""
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
            "corridor_id": "LOG-CORRIDOR-00378",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (378 % 7),
            "carrier_code": "DHL_EXPRESS" if 378 % 3 == 0 else "FEDEX_PRIORITY" if 378 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00379(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00379."""
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
            "corridor_id": "LOG-CORRIDOR-00379",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (379 % 7),
            "carrier_code": "DHL_EXPRESS" if 379 % 3 == 0 else "FEDEX_PRIORITY" if 379 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00380(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00380."""
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
            "corridor_id": "LOG-CORRIDOR-00380",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (380 % 7),
            "carrier_code": "DHL_EXPRESS" if 380 % 3 == 0 else "FEDEX_PRIORITY" if 380 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00381(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00381."""
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
            "corridor_id": "LOG-CORRIDOR-00381",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (381 % 7),
            "carrier_code": "DHL_EXPRESS" if 381 % 3 == 0 else "FEDEX_PRIORITY" if 381 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00382(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00382."""
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
            "corridor_id": "LOG-CORRIDOR-00382",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (382 % 7),
            "carrier_code": "DHL_EXPRESS" if 382 % 3 == 0 else "FEDEX_PRIORITY" if 382 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00383(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00383."""
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
            "corridor_id": "LOG-CORRIDOR-00383",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (383 % 7),
            "carrier_code": "DHL_EXPRESS" if 383 % 3 == 0 else "FEDEX_PRIORITY" if 383 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00384(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00384."""
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
            "corridor_id": "LOG-CORRIDOR-00384",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (384 % 7),
            "carrier_code": "DHL_EXPRESS" if 384 % 3 == 0 else "FEDEX_PRIORITY" if 384 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00385(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00385."""
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
            "corridor_id": "LOG-CORRIDOR-00385",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (385 % 7),
            "carrier_code": "DHL_EXPRESS" if 385 % 3 == 0 else "FEDEX_PRIORITY" if 385 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00386(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00386."""
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
            "corridor_id": "LOG-CORRIDOR-00386",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (386 % 7),
            "carrier_code": "DHL_EXPRESS" if 386 % 3 == 0 else "FEDEX_PRIORITY" if 386 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00387(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00387."""
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
            "corridor_id": "LOG-CORRIDOR-00387",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (387 % 7),
            "carrier_code": "DHL_EXPRESS" if 387 % 3 == 0 else "FEDEX_PRIORITY" if 387 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00388(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00388."""
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
            "corridor_id": "LOG-CORRIDOR-00388",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (388 % 7),
            "carrier_code": "DHL_EXPRESS" if 388 % 3 == 0 else "FEDEX_PRIORITY" if 388 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00389(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00389."""
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
            "corridor_id": "LOG-CORRIDOR-00389",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (389 % 7),
            "carrier_code": "DHL_EXPRESS" if 389 % 3 == 0 else "FEDEX_PRIORITY" if 389 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00390(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00390."""
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
            "corridor_id": "LOG-CORRIDOR-00390",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (390 % 7),
            "carrier_code": "DHL_EXPRESS" if 390 % 3 == 0 else "FEDEX_PRIORITY" if 390 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00391(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00391."""
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
            "corridor_id": "LOG-CORRIDOR-00391",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (391 % 7),
            "carrier_code": "DHL_EXPRESS" if 391 % 3 == 0 else "FEDEX_PRIORITY" if 391 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00392(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00392."""
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
            "corridor_id": "LOG-CORRIDOR-00392",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (392 % 7),
            "carrier_code": "DHL_EXPRESS" if 392 % 3 == 0 else "FEDEX_PRIORITY" if 392 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00393(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00393."""
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
            "corridor_id": "LOG-CORRIDOR-00393",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (393 % 7),
            "carrier_code": "DHL_EXPRESS" if 393 % 3 == 0 else "FEDEX_PRIORITY" if 393 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00394(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00394."""
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
            "corridor_id": "LOG-CORRIDOR-00394",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (394 % 7),
            "carrier_code": "DHL_EXPRESS" if 394 % 3 == 0 else "FEDEX_PRIORITY" if 394 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00395(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00395."""
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
            "corridor_id": "LOG-CORRIDOR-00395",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (395 % 7),
            "carrier_code": "DHL_EXPRESS" if 395 % 3 == 0 else "FEDEX_PRIORITY" if 395 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00396(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00396."""
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
            "corridor_id": "LOG-CORRIDOR-00396",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (396 % 7),
            "carrier_code": "DHL_EXPRESS" if 396 % 3 == 0 else "FEDEX_PRIORITY" if 396 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00397(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00397."""
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
            "corridor_id": "LOG-CORRIDOR-00397",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (397 % 7),
            "carrier_code": "DHL_EXPRESS" if 397 % 3 == 0 else "FEDEX_PRIORITY" if 397 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00398(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00398."""
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
            "corridor_id": "LOG-CORRIDOR-00398",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (398 % 7),
            "carrier_code": "DHL_EXPRESS" if 398 % 3 == 0 else "FEDEX_PRIORITY" if 398 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00399(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00399."""
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
            "corridor_id": "LOG-CORRIDOR-00399",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (399 % 7),
            "carrier_code": "DHL_EXPRESS" if 399 % 3 == 0 else "FEDEX_PRIORITY" if 399 % 3 == 1 else "UPS_SAVER",
        }

    @staticmethod
    def calculate_freight_corridor_00400(weight_kg: float, declared_value_usd: Decimal) -> Dict[str, Any]:
        """Computes shipping and tariff rates for corridor #00400."""
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
            "corridor_id": "LOG-CORRIDOR-00400",
            "weight_kg": weight_kg,
            "declared_value_usd": declared_value_usd,
            "freight_cost": round(freight_cost, 2),
            "fuel_surcharge": round(fuel_surcharge, 2),
            "customs_duty": round(customs_duty, 2),
            "insurance_cost": round(insurance_cost, 2),
            "total_landed_freight": round(total_landed_freight, 2),
            "estimated_transit_days": 3 + (400 % 7),
            "carrier_code": "DHL_EXPRESS" if 400 % 3 == 0 else "FEDEX_PRIORITY" if 400 % 3 == 1 else "UPS_SAVER",
        }
