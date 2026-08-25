"""
Enterprise Vendor Performance & Scorecard Evaluation Engine.
Calculates On-Time In-Full (OTIF), Defect Parts Per Million (PPM), and Pricing Competitiveness.
"""

from decimal import Decimal
from typing import Dict

class VendorScoringEngine:
    """Vendor performance rating calculation routines."""
    
    @staticmethod
    def compute_vendor_scorecard_001(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #001."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-001", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-001",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_002(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #002."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-002", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-002",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_003(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #003."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-003", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-003",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_004(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #004."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-004", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-004",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_005(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #005."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-005", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-005",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_006(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #006."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-006", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-006",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_007(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #007."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-007", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-007",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_008(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #008."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-008", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-008",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_009(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #009."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-009", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-009",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_010(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #010."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-010", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-010",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_011(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #011."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-011", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-011",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_012(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #012."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-012", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-012",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_013(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #013."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-013", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-013",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_014(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #014."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-014", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-014",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_015(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #015."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-015", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-015",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_016(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #016."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-016", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-016",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_017(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #017."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-017", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-017",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_018(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #018."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-018", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-018",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_019(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #019."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-019", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-019",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_020(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #020."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-020", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-020",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_021(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #021."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-021", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-021",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_022(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #022."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-022", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-022",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_023(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #023."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-023", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-023",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_024(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #024."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-024", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-024",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_025(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #025."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-025", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-025",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_026(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #026."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-026", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-026",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_027(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #027."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-027", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-027",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_028(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #028."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-028", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-028",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_029(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #029."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-029", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-029",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_030(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #030."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-030", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-030",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_031(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #031."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-031", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-031",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_032(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #032."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-032", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-032",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_033(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #033."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-033", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-033",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_034(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #034."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-034", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-034",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_035(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #035."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-035", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-035",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_036(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #036."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-036", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-036",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_037(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #037."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-037", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-037",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_038(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #038."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-038", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-038",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_039(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #039."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-039", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-039",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_040(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #040."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-040", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-040",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_041(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #041."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-041", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-041",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_042(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #042."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-042", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-042",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_043(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #043."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-043", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-043",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_044(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #044."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-044", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-044",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_045(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #045."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-045", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-045",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_046(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #046."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-046", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-046",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_047(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #047."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-047", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-047",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_048(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #048."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-048", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-048",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_049(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #049."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-049", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-049",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_050(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #050."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-050", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-050",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_051(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #051."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-051", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-051",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_052(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #052."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-052", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-052",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_053(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #053."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-053", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-053",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_054(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #054."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-054", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-054",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_055(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #055."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-055", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-055",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_056(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #056."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-056", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-056",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_057(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #057."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-057", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-057",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_058(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #058."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-058", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-058",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_059(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #059."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-059", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-059",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_060(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #060."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-060", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-060",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_061(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #061."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-061", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-061",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_062(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #062."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-062", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-062",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_063(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #063."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-063", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-063",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_064(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #064."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-064", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-064",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_065(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #065."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-065", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-065",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_066(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #066."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-066", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-066",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_067(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #067."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-067", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-067",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_068(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #068."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-068", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-068",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_069(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #069."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-069", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-069",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_070(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #070."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-070", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-070",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_071(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #071."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-071", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-071",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_072(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #072."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-072", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-072",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_073(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #073."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-073", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-073",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_074(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #074."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-074", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-074",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_075(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #075."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-075", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-075",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_076(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #076."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-076", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-076",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_077(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #077."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-077", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-077",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_078(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #078."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-078", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-078",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_079(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #079."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-079", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-079",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_080(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #080."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-080", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-080",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_081(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #081."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-081", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-081",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_082(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #082."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-082", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-082",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_083(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #083."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-083", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-083",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_084(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #084."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-084", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-084",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_085(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #085."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-085", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-085",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_086(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #086."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-086", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-086",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_087(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #087."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-087", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-087",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_088(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #088."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-088", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-088",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_089(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #089."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-089", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-089",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_090(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #090."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-090", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-090",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_091(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #091."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-091", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-091",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_092(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #092."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-092", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-092",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_093(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #093."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-093", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-093",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_094(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #094."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-094", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-094",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_095(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #095."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-095", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-095",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_096(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #096."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-096", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-096",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_097(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #097."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-097", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-097",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_098(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #098."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-098", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-098",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_099(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #099."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-099", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-099",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }

    @staticmethod
    def compute_vendor_scorecard_100(orders_count: int, defects_count: int, on_time_count: int) -> Dict[str, any]:
        """Computes scorecard metric #100."""
        if orders_count == 0:
            return {"vendor_eval_id": "VEND-EVAL-100", "overall_score": 5.0, "status": "UNASSESSED"}
        otif_pct = (on_time_count / orders_count) * 100.0
        defect_pct = (defects_count / orders_count) * 100.0
        quality_score = max(0.0, 5.0 - (defect_pct * 0.1))
        delivery_score = min(5.0, (otif_pct / 20.0))
        final_rating = round((quality_score * 0.6) + (delivery_score * 0.4), 2)
        return {
            "vendor_eval_id": "VEND-EVAL-100",
            "otif_percentage": round(otif_pct, 2),
            "defect_percentage": round(defect_pct, 2),
            "quality_score": round(quality_score, 2),
            "delivery_score": round(delivery_score, 2),
            "overall_rating": final_rating,
            "tier": "TIER-1 (Preferred)" if final_rating >= 4.2 else "TIER-2 (Approved)" if final_rating >= 3.5 else "PROBATION",
        }
