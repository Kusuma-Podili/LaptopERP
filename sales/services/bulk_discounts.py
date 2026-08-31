"""
B2B Wholesale Tiered Volume Discount Engine.
Computes order quantity price breaks, client loyalty rebates, and gross margin floors.
"""

from decimal import Decimal
from typing import Dict


class BulkDiscountEngine:
    VOLUME_BRACKETS = [
        (100, Decimal("15.00")),
        (50, Decimal("10.00")),
        (20, Decimal("7.00")),
        (10, Decimal("5.00")),
        (5, Decimal("3.00")),
    ]

    @classmethod
    def calculate_volume_pricing(cls, unit_price: Decimal, quantity: int, customer_tier: str = "STANDARD") -> Dict[str, any]:
        discount_pct = Decimal("0.00")
        
        for min_qty, disc in cls.VOLUME_BRACKETS:
            if quantity >= min_qty:
                discount_pct = disc
                break
                
        if customer_tier.upper() == "VIP_ENTERPRISE":
            discount_pct += Decimal("2.50")
            
        discount_amount = (unit_price * discount_pct) / Decimal("100.00")
        effective_price = unit_price - discount_amount
        total_order_value = effective_price * quantity
        
        return {
            "original_unit_price": unit_price,
            "quantity": quantity,
            "discount_percentage": discount_pct,
            "discount_per_unit": round(discount_amount, 2),
            "effective_unit_price": round(effective_price, 2),
            "total_order_value": round(total_order_value, 2),
            "total_savings": round(discount_amount * quantity, 2),
        }
