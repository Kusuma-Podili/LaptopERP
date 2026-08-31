"""
Supplier Performance Matrix & Vendor Rating Scorecard Engine.
Evaluates vendor delivery accuracy, RMA return ratios, and pricing variance.
"""

from decimal import Decimal
from typing import Dict
from procurement.models import Supplier


class SupplierPerformanceMatrixEngine:
    @staticmethod
    def calculate_vendor_grade(on_time_pct: float, defect_rate_ppm: int, pricing_adherence_pct: float) -> Dict[str, any]:
        delivery_score = min(100.0, on_time_pct) * 0.4
        quality_score = max(0.0, 100.0 - (defect_rate_ppm / 50.0)) * 0.4
        price_score = min(100.0, pricing_adherence_pct) * 0.2
        
        composite_score = round(delivery_score + quality_score + price_score, 2)
        
        tier = "PREFERRED_PARTNER" if composite_score >= 90.0 else "APPROVED" if composite_score >= 75.0 else "UNDER_REVIEW"
        
        return {
            "composite_score": composite_score,
            "delivery_score": delivery_score,
            "quality_score": quality_score,
            "pricing_score": price_score,
            "tier": tier,
            "recommended_allocation_pct": 60 if tier == "PREFERRED_PARTNER" else 30 if tier == "APPROVED" else 10,
        }
