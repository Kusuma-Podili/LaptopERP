"""
Enterprise Hardware Model Database - Part 04.
Comprehensive technical profiles for enterprise, gaming, workstation and ultrabook laptops.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, Dict

@dataclass
class LaptopHardwareCatalogItem:
    sku_code: str
    brand: str
    model_series: str
    chassis_form_factor: str
    cpu_codename: str
    tdp_watts: int
    ram_standard: str
    max_ram_gb: int
    nvme_slots: int
    display_panel: str
    weight_kg: float
    msrp_usd: Decimal
    warranty_tier: str

class HardwareCatalogDatabasePart04:
    """Hardware inventory profile definitions part 04."""

    @classmethod
    def get_hardware_profile_00601(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00601."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00601",
            brand="Dell",
            model_series="Dell Enterprise Series-0601",
            chassis_form_factor="Ultrabook 14-inch" if 601 % 3 == 0 else "Workstation 16-inch" if 601 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (601 % 35),
            ram_standard="DDR5-5600" if 601 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 601 % 2 == 0 else 32,
            nvme_slots=2 if 601 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 601 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (601 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 601 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00602(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00602."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00602",
            brand="HP",
            model_series="HP Enterprise Series-0602",
            chassis_form_factor="Ultrabook 14-inch" if 602 % 3 == 0 else "Workstation 16-inch" if 602 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (602 % 35),
            ram_standard="DDR5-5600" if 602 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 602 % 2 == 0 else 32,
            nvme_slots=2 if 602 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 602 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (602 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 602 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00603(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00603."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00603",
            brand="Apple",
            model_series="Apple Enterprise Series-0603",
            chassis_form_factor="Ultrabook 14-inch" if 603 % 3 == 0 else "Workstation 16-inch" if 603 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (603 % 35),
            ram_standard="DDR5-5600" if 603 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 603 % 2 == 0 else 32,
            nvme_slots=2 if 603 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 603 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (603 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 603 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00604(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00604."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00604",
            brand="Asus",
            model_series="Asus Enterprise Series-0604",
            chassis_form_factor="Ultrabook 14-inch" if 604 % 3 == 0 else "Workstation 16-inch" if 604 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (604 % 35),
            ram_standard="DDR5-5600" if 604 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 604 % 2 == 0 else 32,
            nvme_slots=2 if 604 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 604 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (604 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 604 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00605(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00605."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00605",
            brand="Acer",
            model_series="Acer Enterprise Series-0605",
            chassis_form_factor="Ultrabook 14-inch" if 605 % 3 == 0 else "Workstation 16-inch" if 605 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (605 % 35),
            ram_standard="DDR5-5600" if 605 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 605 % 2 == 0 else 32,
            nvme_slots=2 if 605 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 605 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (605 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 605 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00606(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00606."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00606",
            brand="MSI",
            model_series="MSI Enterprise Series-0606",
            chassis_form_factor="Ultrabook 14-inch" if 606 % 3 == 0 else "Workstation 16-inch" if 606 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (606 % 35),
            ram_standard="DDR5-5600" if 606 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 606 % 2 == 0 else 32,
            nvme_slots=2 if 606 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 606 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (606 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 606 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00607(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00607."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00607",
            brand="Razer",
            model_series="Razer Enterprise Series-0607",
            chassis_form_factor="Ultrabook 14-inch" if 607 % 3 == 0 else "Workstation 16-inch" if 607 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (607 % 35),
            ram_standard="DDR5-5600" if 607 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 607 % 2 == 0 else 32,
            nvme_slots=2 if 607 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 607 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (607 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 607 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00608(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00608."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00608",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0608",
            chassis_form_factor="Ultrabook 14-inch" if 608 % 3 == 0 else "Workstation 16-inch" if 608 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (608 % 35),
            ram_standard="DDR5-5600" if 608 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 608 % 2 == 0 else 32,
            nvme_slots=2 if 608 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 608 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (608 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 608 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00609(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00609."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00609",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0609",
            chassis_form_factor="Ultrabook 14-inch" if 609 % 3 == 0 else "Workstation 16-inch" if 609 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (609 % 35),
            ram_standard="DDR5-5600" if 609 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 609 % 2 == 0 else 32,
            nvme_slots=2 if 609 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 609 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (609 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 609 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00610(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00610."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00610",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0610",
            chassis_form_factor="Ultrabook 14-inch" if 610 % 3 == 0 else "Workstation 16-inch" if 610 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (610 % 35),
            ram_standard="DDR5-5600" if 610 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 610 % 2 == 0 else 32,
            nvme_slots=2 if 610 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 610 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (610 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 610 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00611(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00611."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00611",
            brand="Dell",
            model_series="Dell Enterprise Series-0611",
            chassis_form_factor="Ultrabook 14-inch" if 611 % 3 == 0 else "Workstation 16-inch" if 611 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (611 % 35),
            ram_standard="DDR5-5600" if 611 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 611 % 2 == 0 else 32,
            nvme_slots=2 if 611 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 611 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (611 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 611 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00612(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00612."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00612",
            brand="HP",
            model_series="HP Enterprise Series-0612",
            chassis_form_factor="Ultrabook 14-inch" if 612 % 3 == 0 else "Workstation 16-inch" if 612 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (612 % 35),
            ram_standard="DDR5-5600" if 612 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 612 % 2 == 0 else 32,
            nvme_slots=2 if 612 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 612 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (612 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 612 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00613(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00613."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00613",
            brand="Apple",
            model_series="Apple Enterprise Series-0613",
            chassis_form_factor="Ultrabook 14-inch" if 613 % 3 == 0 else "Workstation 16-inch" if 613 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (613 % 35),
            ram_standard="DDR5-5600" if 613 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 613 % 2 == 0 else 32,
            nvme_slots=2 if 613 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 613 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (613 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 613 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00614(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00614."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00614",
            brand="Asus",
            model_series="Asus Enterprise Series-0614",
            chassis_form_factor="Ultrabook 14-inch" if 614 % 3 == 0 else "Workstation 16-inch" if 614 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (614 % 35),
            ram_standard="DDR5-5600" if 614 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 614 % 2 == 0 else 32,
            nvme_slots=2 if 614 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 614 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (614 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 614 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00615(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00615."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00615",
            brand="Acer",
            model_series="Acer Enterprise Series-0615",
            chassis_form_factor="Ultrabook 14-inch" if 615 % 3 == 0 else "Workstation 16-inch" if 615 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (615 % 35),
            ram_standard="DDR5-5600" if 615 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 615 % 2 == 0 else 32,
            nvme_slots=2 if 615 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 615 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (615 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 615 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00616(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00616."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00616",
            brand="MSI",
            model_series="MSI Enterprise Series-0616",
            chassis_form_factor="Ultrabook 14-inch" if 616 % 3 == 0 else "Workstation 16-inch" if 616 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (616 % 35),
            ram_standard="DDR5-5600" if 616 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 616 % 2 == 0 else 32,
            nvme_slots=2 if 616 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 616 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (616 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 616 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00617(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00617."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00617",
            brand="Razer",
            model_series="Razer Enterprise Series-0617",
            chassis_form_factor="Ultrabook 14-inch" if 617 % 3 == 0 else "Workstation 16-inch" if 617 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (617 % 35),
            ram_standard="DDR5-5600" if 617 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 617 % 2 == 0 else 32,
            nvme_slots=2 if 617 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 617 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (617 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 617 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00618(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00618."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00618",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0618",
            chassis_form_factor="Ultrabook 14-inch" if 618 % 3 == 0 else "Workstation 16-inch" if 618 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (618 % 35),
            ram_standard="DDR5-5600" if 618 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 618 % 2 == 0 else 32,
            nvme_slots=2 if 618 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 618 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (618 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 618 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00619(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00619."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00619",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0619",
            chassis_form_factor="Ultrabook 14-inch" if 619 % 3 == 0 else "Workstation 16-inch" if 619 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (619 % 35),
            ram_standard="DDR5-5600" if 619 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 619 % 2 == 0 else 32,
            nvme_slots=2 if 619 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 619 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (619 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 619 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00620(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00620."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00620",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0620",
            chassis_form_factor="Ultrabook 14-inch" if 620 % 3 == 0 else "Workstation 16-inch" if 620 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (620 % 35),
            ram_standard="DDR5-5600" if 620 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 620 % 2 == 0 else 32,
            nvme_slots=2 if 620 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 620 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (620 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 620 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00621(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00621."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00621",
            brand="Dell",
            model_series="Dell Enterprise Series-0621",
            chassis_form_factor="Ultrabook 14-inch" if 621 % 3 == 0 else "Workstation 16-inch" if 621 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (621 % 35),
            ram_standard="DDR5-5600" if 621 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 621 % 2 == 0 else 32,
            nvme_slots=2 if 621 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 621 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (621 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 621 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00622(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00622."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00622",
            brand="HP",
            model_series="HP Enterprise Series-0622",
            chassis_form_factor="Ultrabook 14-inch" if 622 % 3 == 0 else "Workstation 16-inch" if 622 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (622 % 35),
            ram_standard="DDR5-5600" if 622 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 622 % 2 == 0 else 32,
            nvme_slots=2 if 622 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 622 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (622 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 622 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00623(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00623."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00623",
            brand="Apple",
            model_series="Apple Enterprise Series-0623",
            chassis_form_factor="Ultrabook 14-inch" if 623 % 3 == 0 else "Workstation 16-inch" if 623 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (623 % 35),
            ram_standard="DDR5-5600" if 623 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 623 % 2 == 0 else 32,
            nvme_slots=2 if 623 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 623 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (623 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 623 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00624(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00624."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00624",
            brand="Asus",
            model_series="Asus Enterprise Series-0624",
            chassis_form_factor="Ultrabook 14-inch" if 624 % 3 == 0 else "Workstation 16-inch" if 624 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (624 % 35),
            ram_standard="DDR5-5600" if 624 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 624 % 2 == 0 else 32,
            nvme_slots=2 if 624 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 624 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (624 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 624 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00625(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00625."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00625",
            brand="Acer",
            model_series="Acer Enterprise Series-0625",
            chassis_form_factor="Ultrabook 14-inch" if 625 % 3 == 0 else "Workstation 16-inch" if 625 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (625 % 35),
            ram_standard="DDR5-5600" if 625 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 625 % 2 == 0 else 32,
            nvme_slots=2 if 625 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 625 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (625 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 625 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00626(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00626."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00626",
            brand="MSI",
            model_series="MSI Enterprise Series-0626",
            chassis_form_factor="Ultrabook 14-inch" if 626 % 3 == 0 else "Workstation 16-inch" if 626 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (626 % 35),
            ram_standard="DDR5-5600" if 626 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 626 % 2 == 0 else 32,
            nvme_slots=2 if 626 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 626 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (626 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 626 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00627(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00627."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00627",
            brand="Razer",
            model_series="Razer Enterprise Series-0627",
            chassis_form_factor="Ultrabook 14-inch" if 627 % 3 == 0 else "Workstation 16-inch" if 627 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (627 % 35),
            ram_standard="DDR5-5600" if 627 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 627 % 2 == 0 else 32,
            nvme_slots=2 if 627 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 627 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (627 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 627 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00628(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00628."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00628",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0628",
            chassis_form_factor="Ultrabook 14-inch" if 628 % 3 == 0 else "Workstation 16-inch" if 628 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (628 % 35),
            ram_standard="DDR5-5600" if 628 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 628 % 2 == 0 else 32,
            nvme_slots=2 if 628 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 628 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (628 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 628 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00629(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00629."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00629",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0629",
            chassis_form_factor="Ultrabook 14-inch" if 629 % 3 == 0 else "Workstation 16-inch" if 629 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (629 % 35),
            ram_standard="DDR5-5600" if 629 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 629 % 2 == 0 else 32,
            nvme_slots=2 if 629 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 629 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (629 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 629 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00630(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00630."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00630",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0630",
            chassis_form_factor="Ultrabook 14-inch" if 630 % 3 == 0 else "Workstation 16-inch" if 630 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (630 % 35),
            ram_standard="DDR5-5600" if 630 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 630 % 2 == 0 else 32,
            nvme_slots=2 if 630 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 630 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (630 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 630 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00631(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00631."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00631",
            brand="Dell",
            model_series="Dell Enterprise Series-0631",
            chassis_form_factor="Ultrabook 14-inch" if 631 % 3 == 0 else "Workstation 16-inch" if 631 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (631 % 35),
            ram_standard="DDR5-5600" if 631 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 631 % 2 == 0 else 32,
            nvme_slots=2 if 631 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 631 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (631 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 631 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00632(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00632."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00632",
            brand="HP",
            model_series="HP Enterprise Series-0632",
            chassis_form_factor="Ultrabook 14-inch" if 632 % 3 == 0 else "Workstation 16-inch" if 632 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (632 % 35),
            ram_standard="DDR5-5600" if 632 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 632 % 2 == 0 else 32,
            nvme_slots=2 if 632 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 632 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (632 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 632 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00633(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00633."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00633",
            brand="Apple",
            model_series="Apple Enterprise Series-0633",
            chassis_form_factor="Ultrabook 14-inch" if 633 % 3 == 0 else "Workstation 16-inch" if 633 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (633 % 35),
            ram_standard="DDR5-5600" if 633 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 633 % 2 == 0 else 32,
            nvme_slots=2 if 633 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 633 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (633 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 633 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00634(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00634."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00634",
            brand="Asus",
            model_series="Asus Enterprise Series-0634",
            chassis_form_factor="Ultrabook 14-inch" if 634 % 3 == 0 else "Workstation 16-inch" if 634 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (634 % 35),
            ram_standard="DDR5-5600" if 634 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 634 % 2 == 0 else 32,
            nvme_slots=2 if 634 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 634 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (634 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 634 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00635(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00635."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00635",
            brand="Acer",
            model_series="Acer Enterprise Series-0635",
            chassis_form_factor="Ultrabook 14-inch" if 635 % 3 == 0 else "Workstation 16-inch" if 635 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (635 % 35),
            ram_standard="DDR5-5600" if 635 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 635 % 2 == 0 else 32,
            nvme_slots=2 if 635 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 635 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (635 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 635 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00636(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00636."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00636",
            brand="MSI",
            model_series="MSI Enterprise Series-0636",
            chassis_form_factor="Ultrabook 14-inch" if 636 % 3 == 0 else "Workstation 16-inch" if 636 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (636 % 35),
            ram_standard="DDR5-5600" if 636 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 636 % 2 == 0 else 32,
            nvme_slots=2 if 636 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 636 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (636 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 636 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00637(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00637."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00637",
            brand="Razer",
            model_series="Razer Enterprise Series-0637",
            chassis_form_factor="Ultrabook 14-inch" if 637 % 3 == 0 else "Workstation 16-inch" if 637 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (637 % 35),
            ram_standard="DDR5-5600" if 637 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 637 % 2 == 0 else 32,
            nvme_slots=2 if 637 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 637 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (637 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 637 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00638(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00638."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00638",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0638",
            chassis_form_factor="Ultrabook 14-inch" if 638 % 3 == 0 else "Workstation 16-inch" if 638 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (638 % 35),
            ram_standard="DDR5-5600" if 638 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 638 % 2 == 0 else 32,
            nvme_slots=2 if 638 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 638 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (638 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 638 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00639(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00639."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00639",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0639",
            chassis_form_factor="Ultrabook 14-inch" if 639 % 3 == 0 else "Workstation 16-inch" if 639 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (639 % 35),
            ram_standard="DDR5-5600" if 639 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 639 % 2 == 0 else 32,
            nvme_slots=2 if 639 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 639 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (639 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 639 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00640(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00640."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00640",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0640",
            chassis_form_factor="Ultrabook 14-inch" if 640 % 3 == 0 else "Workstation 16-inch" if 640 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (640 % 35),
            ram_standard="DDR5-5600" if 640 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 640 % 2 == 0 else 32,
            nvme_slots=2 if 640 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 640 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (640 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 640 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00641(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00641."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00641",
            brand="Dell",
            model_series="Dell Enterprise Series-0641",
            chassis_form_factor="Ultrabook 14-inch" if 641 % 3 == 0 else "Workstation 16-inch" if 641 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (641 % 35),
            ram_standard="DDR5-5600" if 641 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 641 % 2 == 0 else 32,
            nvme_slots=2 if 641 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 641 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (641 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 641 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00642(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00642."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00642",
            brand="HP",
            model_series="HP Enterprise Series-0642",
            chassis_form_factor="Ultrabook 14-inch" if 642 % 3 == 0 else "Workstation 16-inch" if 642 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (642 % 35),
            ram_standard="DDR5-5600" if 642 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 642 % 2 == 0 else 32,
            nvme_slots=2 if 642 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 642 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (642 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 642 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00643(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00643."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00643",
            brand="Apple",
            model_series="Apple Enterprise Series-0643",
            chassis_form_factor="Ultrabook 14-inch" if 643 % 3 == 0 else "Workstation 16-inch" if 643 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (643 % 35),
            ram_standard="DDR5-5600" if 643 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 643 % 2 == 0 else 32,
            nvme_slots=2 if 643 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 643 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (643 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 643 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00644(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00644."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00644",
            brand="Asus",
            model_series="Asus Enterprise Series-0644",
            chassis_form_factor="Ultrabook 14-inch" if 644 % 3 == 0 else "Workstation 16-inch" if 644 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (644 % 35),
            ram_standard="DDR5-5600" if 644 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 644 % 2 == 0 else 32,
            nvme_slots=2 if 644 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 644 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (644 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 644 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00645(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00645."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00645",
            brand="Acer",
            model_series="Acer Enterprise Series-0645",
            chassis_form_factor="Ultrabook 14-inch" if 645 % 3 == 0 else "Workstation 16-inch" if 645 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (645 % 35),
            ram_standard="DDR5-5600" if 645 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 645 % 2 == 0 else 32,
            nvme_slots=2 if 645 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 645 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (645 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 645 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00646(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00646."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00646",
            brand="MSI",
            model_series="MSI Enterprise Series-0646",
            chassis_form_factor="Ultrabook 14-inch" if 646 % 3 == 0 else "Workstation 16-inch" if 646 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (646 % 35),
            ram_standard="DDR5-5600" if 646 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 646 % 2 == 0 else 32,
            nvme_slots=2 if 646 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 646 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (646 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 646 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00647(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00647."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00647",
            brand="Razer",
            model_series="Razer Enterprise Series-0647",
            chassis_form_factor="Ultrabook 14-inch" if 647 % 3 == 0 else "Workstation 16-inch" if 647 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (647 % 35),
            ram_standard="DDR5-5600" if 647 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 647 % 2 == 0 else 32,
            nvme_slots=2 if 647 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 647 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (647 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 647 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00648(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00648."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00648",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0648",
            chassis_form_factor="Ultrabook 14-inch" if 648 % 3 == 0 else "Workstation 16-inch" if 648 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (648 % 35),
            ram_standard="DDR5-5600" if 648 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 648 % 2 == 0 else 32,
            nvme_slots=2 if 648 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 648 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (648 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 648 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00649(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00649."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00649",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0649",
            chassis_form_factor="Ultrabook 14-inch" if 649 % 3 == 0 else "Workstation 16-inch" if 649 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (649 % 35),
            ram_standard="DDR5-5600" if 649 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 649 % 2 == 0 else 32,
            nvme_slots=2 if 649 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 649 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (649 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 649 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00650(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00650."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00650",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0650",
            chassis_form_factor="Ultrabook 14-inch" if 650 % 3 == 0 else "Workstation 16-inch" if 650 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (650 % 35),
            ram_standard="DDR5-5600" if 650 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 650 % 2 == 0 else 32,
            nvme_slots=2 if 650 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 650 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (650 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 650 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00651(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00651."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00651",
            brand="Dell",
            model_series="Dell Enterprise Series-0651",
            chassis_form_factor="Ultrabook 14-inch" if 651 % 3 == 0 else "Workstation 16-inch" if 651 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (651 % 35),
            ram_standard="DDR5-5600" if 651 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 651 % 2 == 0 else 32,
            nvme_slots=2 if 651 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 651 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (651 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 651 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00652(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00652."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00652",
            brand="HP",
            model_series="HP Enterprise Series-0652",
            chassis_form_factor="Ultrabook 14-inch" if 652 % 3 == 0 else "Workstation 16-inch" if 652 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (652 % 35),
            ram_standard="DDR5-5600" if 652 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 652 % 2 == 0 else 32,
            nvme_slots=2 if 652 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 652 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (652 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 652 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00653(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00653."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00653",
            brand="Apple",
            model_series="Apple Enterprise Series-0653",
            chassis_form_factor="Ultrabook 14-inch" if 653 % 3 == 0 else "Workstation 16-inch" if 653 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (653 % 35),
            ram_standard="DDR5-5600" if 653 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 653 % 2 == 0 else 32,
            nvme_slots=2 if 653 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 653 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (653 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 653 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00654(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00654."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00654",
            brand="Asus",
            model_series="Asus Enterprise Series-0654",
            chassis_form_factor="Ultrabook 14-inch" if 654 % 3 == 0 else "Workstation 16-inch" if 654 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (654 % 35),
            ram_standard="DDR5-5600" if 654 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 654 % 2 == 0 else 32,
            nvme_slots=2 if 654 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 654 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (654 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 654 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00655(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00655."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00655",
            brand="Acer",
            model_series="Acer Enterprise Series-0655",
            chassis_form_factor="Ultrabook 14-inch" if 655 % 3 == 0 else "Workstation 16-inch" if 655 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (655 % 35),
            ram_standard="DDR5-5600" if 655 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 655 % 2 == 0 else 32,
            nvme_slots=2 if 655 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 655 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (655 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 655 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00656(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00656."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00656",
            brand="MSI",
            model_series="MSI Enterprise Series-0656",
            chassis_form_factor="Ultrabook 14-inch" if 656 % 3 == 0 else "Workstation 16-inch" if 656 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (656 % 35),
            ram_standard="DDR5-5600" if 656 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 656 % 2 == 0 else 32,
            nvme_slots=2 if 656 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 656 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (656 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 656 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00657(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00657."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00657",
            brand="Razer",
            model_series="Razer Enterprise Series-0657",
            chassis_form_factor="Ultrabook 14-inch" if 657 % 3 == 0 else "Workstation 16-inch" if 657 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (657 % 35),
            ram_standard="DDR5-5600" if 657 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 657 % 2 == 0 else 32,
            nvme_slots=2 if 657 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 657 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (657 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 657 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00658(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00658."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00658",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0658",
            chassis_form_factor="Ultrabook 14-inch" if 658 % 3 == 0 else "Workstation 16-inch" if 658 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (658 % 35),
            ram_standard="DDR5-5600" if 658 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 658 % 2 == 0 else 32,
            nvme_slots=2 if 658 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 658 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (658 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 658 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00659(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00659."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00659",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0659",
            chassis_form_factor="Ultrabook 14-inch" if 659 % 3 == 0 else "Workstation 16-inch" if 659 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (659 % 35),
            ram_standard="DDR5-5600" if 659 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 659 % 2 == 0 else 32,
            nvme_slots=2 if 659 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 659 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (659 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 659 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00660(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00660."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00660",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0660",
            chassis_form_factor="Ultrabook 14-inch" if 660 % 3 == 0 else "Workstation 16-inch" if 660 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (660 % 35),
            ram_standard="DDR5-5600" if 660 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 660 % 2 == 0 else 32,
            nvme_slots=2 if 660 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 660 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (660 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 660 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00661(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00661."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00661",
            brand="Dell",
            model_series="Dell Enterprise Series-0661",
            chassis_form_factor="Ultrabook 14-inch" if 661 % 3 == 0 else "Workstation 16-inch" if 661 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (661 % 35),
            ram_standard="DDR5-5600" if 661 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 661 % 2 == 0 else 32,
            nvme_slots=2 if 661 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 661 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (661 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 661 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00662(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00662."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00662",
            brand="HP",
            model_series="HP Enterprise Series-0662",
            chassis_form_factor="Ultrabook 14-inch" if 662 % 3 == 0 else "Workstation 16-inch" if 662 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (662 % 35),
            ram_standard="DDR5-5600" if 662 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 662 % 2 == 0 else 32,
            nvme_slots=2 if 662 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 662 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (662 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 662 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00663(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00663."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00663",
            brand="Apple",
            model_series="Apple Enterprise Series-0663",
            chassis_form_factor="Ultrabook 14-inch" if 663 % 3 == 0 else "Workstation 16-inch" if 663 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (663 % 35),
            ram_standard="DDR5-5600" if 663 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 663 % 2 == 0 else 32,
            nvme_slots=2 if 663 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 663 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (663 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 663 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00664(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00664."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00664",
            brand="Asus",
            model_series="Asus Enterprise Series-0664",
            chassis_form_factor="Ultrabook 14-inch" if 664 % 3 == 0 else "Workstation 16-inch" if 664 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (664 % 35),
            ram_standard="DDR5-5600" if 664 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 664 % 2 == 0 else 32,
            nvme_slots=2 if 664 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 664 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (664 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 664 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00665(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00665."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00665",
            brand="Acer",
            model_series="Acer Enterprise Series-0665",
            chassis_form_factor="Ultrabook 14-inch" if 665 % 3 == 0 else "Workstation 16-inch" if 665 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (665 % 35),
            ram_standard="DDR5-5600" if 665 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 665 % 2 == 0 else 32,
            nvme_slots=2 if 665 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 665 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (665 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 665 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00666(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00666."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00666",
            brand="MSI",
            model_series="MSI Enterprise Series-0666",
            chassis_form_factor="Ultrabook 14-inch" if 666 % 3 == 0 else "Workstation 16-inch" if 666 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (666 % 35),
            ram_standard="DDR5-5600" if 666 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 666 % 2 == 0 else 32,
            nvme_slots=2 if 666 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 666 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (666 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 666 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00667(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00667."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00667",
            brand="Razer",
            model_series="Razer Enterprise Series-0667",
            chassis_form_factor="Ultrabook 14-inch" if 667 % 3 == 0 else "Workstation 16-inch" if 667 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (667 % 35),
            ram_standard="DDR5-5600" if 667 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 667 % 2 == 0 else 32,
            nvme_slots=2 if 667 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 667 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (667 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 667 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00668(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00668."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00668",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0668",
            chassis_form_factor="Ultrabook 14-inch" if 668 % 3 == 0 else "Workstation 16-inch" if 668 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (668 % 35),
            ram_standard="DDR5-5600" if 668 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 668 % 2 == 0 else 32,
            nvme_slots=2 if 668 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 668 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (668 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 668 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00669(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00669."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00669",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0669",
            chassis_form_factor="Ultrabook 14-inch" if 669 % 3 == 0 else "Workstation 16-inch" if 669 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (669 % 35),
            ram_standard="DDR5-5600" if 669 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 669 % 2 == 0 else 32,
            nvme_slots=2 if 669 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 669 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (669 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 669 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00670(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00670."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00670",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0670",
            chassis_form_factor="Ultrabook 14-inch" if 670 % 3 == 0 else "Workstation 16-inch" if 670 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (670 % 35),
            ram_standard="DDR5-5600" if 670 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 670 % 2 == 0 else 32,
            nvme_slots=2 if 670 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 670 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (670 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 670 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00671(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00671."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00671",
            brand="Dell",
            model_series="Dell Enterprise Series-0671",
            chassis_form_factor="Ultrabook 14-inch" if 671 % 3 == 0 else "Workstation 16-inch" if 671 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (671 % 35),
            ram_standard="DDR5-5600" if 671 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 671 % 2 == 0 else 32,
            nvme_slots=2 if 671 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 671 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (671 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 671 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00672(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00672."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00672",
            brand="HP",
            model_series="HP Enterprise Series-0672",
            chassis_form_factor="Ultrabook 14-inch" if 672 % 3 == 0 else "Workstation 16-inch" if 672 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (672 % 35),
            ram_standard="DDR5-5600" if 672 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 672 % 2 == 0 else 32,
            nvme_slots=2 if 672 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 672 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (672 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 672 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00673(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00673."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00673",
            brand="Apple",
            model_series="Apple Enterprise Series-0673",
            chassis_form_factor="Ultrabook 14-inch" if 673 % 3 == 0 else "Workstation 16-inch" if 673 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (673 % 35),
            ram_standard="DDR5-5600" if 673 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 673 % 2 == 0 else 32,
            nvme_slots=2 if 673 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 673 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (673 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 673 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00674(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00674."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00674",
            brand="Asus",
            model_series="Asus Enterprise Series-0674",
            chassis_form_factor="Ultrabook 14-inch" if 674 % 3 == 0 else "Workstation 16-inch" if 674 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (674 % 35),
            ram_standard="DDR5-5600" if 674 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 674 % 2 == 0 else 32,
            nvme_slots=2 if 674 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 674 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (674 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 674 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00675(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00675."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00675",
            brand="Acer",
            model_series="Acer Enterprise Series-0675",
            chassis_form_factor="Ultrabook 14-inch" if 675 % 3 == 0 else "Workstation 16-inch" if 675 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (675 % 35),
            ram_standard="DDR5-5600" if 675 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 675 % 2 == 0 else 32,
            nvme_slots=2 if 675 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 675 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (675 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 675 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00676(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00676."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00676",
            brand="MSI",
            model_series="MSI Enterprise Series-0676",
            chassis_form_factor="Ultrabook 14-inch" if 676 % 3 == 0 else "Workstation 16-inch" if 676 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (676 % 35),
            ram_standard="DDR5-5600" if 676 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 676 % 2 == 0 else 32,
            nvme_slots=2 if 676 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 676 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (676 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 676 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00677(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00677."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00677",
            brand="Razer",
            model_series="Razer Enterprise Series-0677",
            chassis_form_factor="Ultrabook 14-inch" if 677 % 3 == 0 else "Workstation 16-inch" if 677 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (677 % 35),
            ram_standard="DDR5-5600" if 677 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 677 % 2 == 0 else 32,
            nvme_slots=2 if 677 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 677 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (677 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 677 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00678(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00678."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00678",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0678",
            chassis_form_factor="Ultrabook 14-inch" if 678 % 3 == 0 else "Workstation 16-inch" if 678 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (678 % 35),
            ram_standard="DDR5-5600" if 678 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 678 % 2 == 0 else 32,
            nvme_slots=2 if 678 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 678 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (678 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 678 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00679(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00679."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00679",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0679",
            chassis_form_factor="Ultrabook 14-inch" if 679 % 3 == 0 else "Workstation 16-inch" if 679 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (679 % 35),
            ram_standard="DDR5-5600" if 679 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 679 % 2 == 0 else 32,
            nvme_slots=2 if 679 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 679 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (679 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 679 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00680(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00680."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00680",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0680",
            chassis_form_factor="Ultrabook 14-inch" if 680 % 3 == 0 else "Workstation 16-inch" if 680 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (680 % 35),
            ram_standard="DDR5-5600" if 680 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 680 % 2 == 0 else 32,
            nvme_slots=2 if 680 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 680 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (680 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 680 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00681(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00681."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00681",
            brand="Dell",
            model_series="Dell Enterprise Series-0681",
            chassis_form_factor="Ultrabook 14-inch" if 681 % 3 == 0 else "Workstation 16-inch" if 681 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (681 % 35),
            ram_standard="DDR5-5600" if 681 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 681 % 2 == 0 else 32,
            nvme_slots=2 if 681 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 681 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (681 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 681 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00682(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00682."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00682",
            brand="HP",
            model_series="HP Enterprise Series-0682",
            chassis_form_factor="Ultrabook 14-inch" if 682 % 3 == 0 else "Workstation 16-inch" if 682 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (682 % 35),
            ram_standard="DDR5-5600" if 682 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 682 % 2 == 0 else 32,
            nvme_slots=2 if 682 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 682 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (682 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 682 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00683(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00683."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00683",
            brand="Apple",
            model_series="Apple Enterprise Series-0683",
            chassis_form_factor="Ultrabook 14-inch" if 683 % 3 == 0 else "Workstation 16-inch" if 683 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (683 % 35),
            ram_standard="DDR5-5600" if 683 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 683 % 2 == 0 else 32,
            nvme_slots=2 if 683 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 683 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (683 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 683 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00684(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00684."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00684",
            brand="Asus",
            model_series="Asus Enterprise Series-0684",
            chassis_form_factor="Ultrabook 14-inch" if 684 % 3 == 0 else "Workstation 16-inch" if 684 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (684 % 35),
            ram_standard="DDR5-5600" if 684 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 684 % 2 == 0 else 32,
            nvme_slots=2 if 684 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 684 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (684 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 684 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00685(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00685."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00685",
            brand="Acer",
            model_series="Acer Enterprise Series-0685",
            chassis_form_factor="Ultrabook 14-inch" if 685 % 3 == 0 else "Workstation 16-inch" if 685 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (685 % 35),
            ram_standard="DDR5-5600" if 685 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 685 % 2 == 0 else 32,
            nvme_slots=2 if 685 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 685 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (685 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 685 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00686(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00686."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00686",
            brand="MSI",
            model_series="MSI Enterprise Series-0686",
            chassis_form_factor="Ultrabook 14-inch" if 686 % 3 == 0 else "Workstation 16-inch" if 686 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (686 % 35),
            ram_standard="DDR5-5600" if 686 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 686 % 2 == 0 else 32,
            nvme_slots=2 if 686 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 686 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (686 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 686 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00687(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00687."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00687",
            brand="Razer",
            model_series="Razer Enterprise Series-0687",
            chassis_form_factor="Ultrabook 14-inch" if 687 % 3 == 0 else "Workstation 16-inch" if 687 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (687 % 35),
            ram_standard="DDR5-5600" if 687 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 687 % 2 == 0 else 32,
            nvme_slots=2 if 687 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 687 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (687 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 687 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00688(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00688."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00688",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0688",
            chassis_form_factor="Ultrabook 14-inch" if 688 % 3 == 0 else "Workstation 16-inch" if 688 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (688 % 35),
            ram_standard="DDR5-5600" if 688 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 688 % 2 == 0 else 32,
            nvme_slots=2 if 688 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 688 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (688 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 688 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00689(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00689."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00689",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0689",
            chassis_form_factor="Ultrabook 14-inch" if 689 % 3 == 0 else "Workstation 16-inch" if 689 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (689 % 35),
            ram_standard="DDR5-5600" if 689 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 689 % 2 == 0 else 32,
            nvme_slots=2 if 689 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 689 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (689 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 689 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00690(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00690."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00690",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0690",
            chassis_form_factor="Ultrabook 14-inch" if 690 % 3 == 0 else "Workstation 16-inch" if 690 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (690 % 35),
            ram_standard="DDR5-5600" if 690 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 690 % 2 == 0 else 32,
            nvme_slots=2 if 690 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 690 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (690 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 690 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00691(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00691."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00691",
            brand="Dell",
            model_series="Dell Enterprise Series-0691",
            chassis_form_factor="Ultrabook 14-inch" if 691 % 3 == 0 else "Workstation 16-inch" if 691 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (691 % 35),
            ram_standard="DDR5-5600" if 691 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 691 % 2 == 0 else 32,
            nvme_slots=2 if 691 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 691 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (691 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 691 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00692(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00692."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00692",
            brand="HP",
            model_series="HP Enterprise Series-0692",
            chassis_form_factor="Ultrabook 14-inch" if 692 % 3 == 0 else "Workstation 16-inch" if 692 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (692 % 35),
            ram_standard="DDR5-5600" if 692 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 692 % 2 == 0 else 32,
            nvme_slots=2 if 692 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 692 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (692 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 692 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00693(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00693."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00693",
            brand="Apple",
            model_series="Apple Enterprise Series-0693",
            chassis_form_factor="Ultrabook 14-inch" if 693 % 3 == 0 else "Workstation 16-inch" if 693 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (693 % 35),
            ram_standard="DDR5-5600" if 693 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 693 % 2 == 0 else 32,
            nvme_slots=2 if 693 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 693 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (693 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 693 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00694(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00694."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00694",
            brand="Asus",
            model_series="Asus Enterprise Series-0694",
            chassis_form_factor="Ultrabook 14-inch" if 694 % 3 == 0 else "Workstation 16-inch" if 694 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (694 % 35),
            ram_standard="DDR5-5600" if 694 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 694 % 2 == 0 else 32,
            nvme_slots=2 if 694 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 694 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (694 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 694 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00695(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00695."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00695",
            brand="Acer",
            model_series="Acer Enterprise Series-0695",
            chassis_form_factor="Ultrabook 14-inch" if 695 % 3 == 0 else "Workstation 16-inch" if 695 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (695 % 35),
            ram_standard="DDR5-5600" if 695 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 695 % 2 == 0 else 32,
            nvme_slots=2 if 695 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 695 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (695 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 695 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00696(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00696."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00696",
            brand="MSI",
            model_series="MSI Enterprise Series-0696",
            chassis_form_factor="Ultrabook 14-inch" if 696 % 3 == 0 else "Workstation 16-inch" if 696 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (696 % 35),
            ram_standard="DDR5-5600" if 696 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 696 % 2 == 0 else 32,
            nvme_slots=2 if 696 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 696 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (696 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 696 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00697(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00697."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00697",
            brand="Razer",
            model_series="Razer Enterprise Series-0697",
            chassis_form_factor="Ultrabook 14-inch" if 697 % 3 == 0 else "Workstation 16-inch" if 697 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (697 % 35),
            ram_standard="DDR5-5600" if 697 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 697 % 2 == 0 else 32,
            nvme_slots=2 if 697 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 697 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (697 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 697 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00698(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00698."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00698",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0698",
            chassis_form_factor="Ultrabook 14-inch" if 698 % 3 == 0 else "Workstation 16-inch" if 698 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (698 % 35),
            ram_standard="DDR5-5600" if 698 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 698 % 2 == 0 else 32,
            nvme_slots=2 if 698 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 698 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (698 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 698 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00699(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00699."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00699",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0699",
            chassis_form_factor="Ultrabook 14-inch" if 699 % 3 == 0 else "Workstation 16-inch" if 699 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (699 % 35),
            ram_standard="DDR5-5600" if 699 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 699 % 2 == 0 else 32,
            nvme_slots=2 if 699 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 699 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (699 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 699 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00700(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00700."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00700",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0700",
            chassis_form_factor="Ultrabook 14-inch" if 700 % 3 == 0 else "Workstation 16-inch" if 700 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (700 % 35),
            ram_standard="DDR5-5600" if 700 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 700 % 2 == 0 else 32,
            nvme_slots=2 if 700 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 700 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (700 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 700 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00701(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00701."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00701",
            brand="Dell",
            model_series="Dell Enterprise Series-0701",
            chassis_form_factor="Ultrabook 14-inch" if 701 % 3 == 0 else "Workstation 16-inch" if 701 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (701 % 35),
            ram_standard="DDR5-5600" if 701 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 701 % 2 == 0 else 32,
            nvme_slots=2 if 701 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 701 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (701 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 701 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00702(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00702."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00702",
            brand="HP",
            model_series="HP Enterprise Series-0702",
            chassis_form_factor="Ultrabook 14-inch" if 702 % 3 == 0 else "Workstation 16-inch" if 702 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (702 % 35),
            ram_standard="DDR5-5600" if 702 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 702 % 2 == 0 else 32,
            nvme_slots=2 if 702 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 702 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (702 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 702 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00703(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00703."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00703",
            brand="Apple",
            model_series="Apple Enterprise Series-0703",
            chassis_form_factor="Ultrabook 14-inch" if 703 % 3 == 0 else "Workstation 16-inch" if 703 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (703 % 35),
            ram_standard="DDR5-5600" if 703 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 703 % 2 == 0 else 32,
            nvme_slots=2 if 703 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 703 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (703 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 703 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00704(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00704."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00704",
            brand="Asus",
            model_series="Asus Enterprise Series-0704",
            chassis_form_factor="Ultrabook 14-inch" if 704 % 3 == 0 else "Workstation 16-inch" if 704 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (704 % 35),
            ram_standard="DDR5-5600" if 704 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 704 % 2 == 0 else 32,
            nvme_slots=2 if 704 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 704 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (704 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 704 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00705(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00705."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00705",
            brand="Acer",
            model_series="Acer Enterprise Series-0705",
            chassis_form_factor="Ultrabook 14-inch" if 705 % 3 == 0 else "Workstation 16-inch" if 705 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (705 % 35),
            ram_standard="DDR5-5600" if 705 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 705 % 2 == 0 else 32,
            nvme_slots=2 if 705 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 705 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (705 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 705 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00706(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00706."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00706",
            brand="MSI",
            model_series="MSI Enterprise Series-0706",
            chassis_form_factor="Ultrabook 14-inch" if 706 % 3 == 0 else "Workstation 16-inch" if 706 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (706 % 35),
            ram_standard="DDR5-5600" if 706 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 706 % 2 == 0 else 32,
            nvme_slots=2 if 706 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 706 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (706 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 706 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00707(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00707."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00707",
            brand="Razer",
            model_series="Razer Enterprise Series-0707",
            chassis_form_factor="Ultrabook 14-inch" if 707 % 3 == 0 else "Workstation 16-inch" if 707 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (707 % 35),
            ram_standard="DDR5-5600" if 707 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 707 % 2 == 0 else 32,
            nvme_slots=2 if 707 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 707 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (707 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 707 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00708(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00708."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00708",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0708",
            chassis_form_factor="Ultrabook 14-inch" if 708 % 3 == 0 else "Workstation 16-inch" if 708 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (708 % 35),
            ram_standard="DDR5-5600" if 708 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 708 % 2 == 0 else 32,
            nvme_slots=2 if 708 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 708 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (708 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 708 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00709(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00709."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00709",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0709",
            chassis_form_factor="Ultrabook 14-inch" if 709 % 3 == 0 else "Workstation 16-inch" if 709 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (709 % 35),
            ram_standard="DDR5-5600" if 709 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 709 % 2 == 0 else 32,
            nvme_slots=2 if 709 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 709 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (709 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 709 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00710(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00710."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00710",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0710",
            chassis_form_factor="Ultrabook 14-inch" if 710 % 3 == 0 else "Workstation 16-inch" if 710 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (710 % 35),
            ram_standard="DDR5-5600" if 710 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 710 % 2 == 0 else 32,
            nvme_slots=2 if 710 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 710 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (710 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 710 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00711(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00711."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00711",
            brand="Dell",
            model_series="Dell Enterprise Series-0711",
            chassis_form_factor="Ultrabook 14-inch" if 711 % 3 == 0 else "Workstation 16-inch" if 711 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (711 % 35),
            ram_standard="DDR5-5600" if 711 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 711 % 2 == 0 else 32,
            nvme_slots=2 if 711 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 711 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (711 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 711 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00712(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00712."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00712",
            brand="HP",
            model_series="HP Enterprise Series-0712",
            chassis_form_factor="Ultrabook 14-inch" if 712 % 3 == 0 else "Workstation 16-inch" if 712 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (712 % 35),
            ram_standard="DDR5-5600" if 712 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 712 % 2 == 0 else 32,
            nvme_slots=2 if 712 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 712 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (712 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 712 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00713(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00713."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00713",
            brand="Apple",
            model_series="Apple Enterprise Series-0713",
            chassis_form_factor="Ultrabook 14-inch" if 713 % 3 == 0 else "Workstation 16-inch" if 713 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (713 % 35),
            ram_standard="DDR5-5600" if 713 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 713 % 2 == 0 else 32,
            nvme_slots=2 if 713 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 713 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (713 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 713 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00714(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00714."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00714",
            brand="Asus",
            model_series="Asus Enterprise Series-0714",
            chassis_form_factor="Ultrabook 14-inch" if 714 % 3 == 0 else "Workstation 16-inch" if 714 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (714 % 35),
            ram_standard="DDR5-5600" if 714 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 714 % 2 == 0 else 32,
            nvme_slots=2 if 714 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 714 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (714 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 714 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00715(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00715."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00715",
            brand="Acer",
            model_series="Acer Enterprise Series-0715",
            chassis_form_factor="Ultrabook 14-inch" if 715 % 3 == 0 else "Workstation 16-inch" if 715 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (715 % 35),
            ram_standard="DDR5-5600" if 715 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 715 % 2 == 0 else 32,
            nvme_slots=2 if 715 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 715 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (715 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 715 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00716(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00716."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00716",
            brand="MSI",
            model_series="MSI Enterprise Series-0716",
            chassis_form_factor="Ultrabook 14-inch" if 716 % 3 == 0 else "Workstation 16-inch" if 716 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (716 % 35),
            ram_standard="DDR5-5600" if 716 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 716 % 2 == 0 else 32,
            nvme_slots=2 if 716 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 716 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (716 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 716 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00717(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00717."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00717",
            brand="Razer",
            model_series="Razer Enterprise Series-0717",
            chassis_form_factor="Ultrabook 14-inch" if 717 % 3 == 0 else "Workstation 16-inch" if 717 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (717 % 35),
            ram_standard="DDR5-5600" if 717 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 717 % 2 == 0 else 32,
            nvme_slots=2 if 717 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 717 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (717 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 717 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00718(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00718."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00718",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0718",
            chassis_form_factor="Ultrabook 14-inch" if 718 % 3 == 0 else "Workstation 16-inch" if 718 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (718 % 35),
            ram_standard="DDR5-5600" if 718 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 718 % 2 == 0 else 32,
            nvme_slots=2 if 718 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 718 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (718 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 718 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00719(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00719."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00719",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0719",
            chassis_form_factor="Ultrabook 14-inch" if 719 % 3 == 0 else "Workstation 16-inch" if 719 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (719 % 35),
            ram_standard="DDR5-5600" if 719 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 719 % 2 == 0 else 32,
            nvme_slots=2 if 719 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 719 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (719 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 719 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00720(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00720."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00720",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0720",
            chassis_form_factor="Ultrabook 14-inch" if 720 % 3 == 0 else "Workstation 16-inch" if 720 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (720 % 35),
            ram_standard="DDR5-5600" if 720 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 720 % 2 == 0 else 32,
            nvme_slots=2 if 720 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 720 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (720 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 720 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00721(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00721."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00721",
            brand="Dell",
            model_series="Dell Enterprise Series-0721",
            chassis_form_factor="Ultrabook 14-inch" if 721 % 3 == 0 else "Workstation 16-inch" if 721 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (721 % 35),
            ram_standard="DDR5-5600" if 721 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 721 % 2 == 0 else 32,
            nvme_slots=2 if 721 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 721 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (721 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 721 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00722(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00722."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00722",
            brand="HP",
            model_series="HP Enterprise Series-0722",
            chassis_form_factor="Ultrabook 14-inch" if 722 % 3 == 0 else "Workstation 16-inch" if 722 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (722 % 35),
            ram_standard="DDR5-5600" if 722 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 722 % 2 == 0 else 32,
            nvme_slots=2 if 722 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 722 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (722 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 722 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00723(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00723."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00723",
            brand="Apple",
            model_series="Apple Enterprise Series-0723",
            chassis_form_factor="Ultrabook 14-inch" if 723 % 3 == 0 else "Workstation 16-inch" if 723 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (723 % 35),
            ram_standard="DDR5-5600" if 723 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 723 % 2 == 0 else 32,
            nvme_slots=2 if 723 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 723 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (723 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 723 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00724(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00724."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00724",
            brand="Asus",
            model_series="Asus Enterprise Series-0724",
            chassis_form_factor="Ultrabook 14-inch" if 724 % 3 == 0 else "Workstation 16-inch" if 724 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (724 % 35),
            ram_standard="DDR5-5600" if 724 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 724 % 2 == 0 else 32,
            nvme_slots=2 if 724 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 724 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (724 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 724 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00725(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00725."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00725",
            brand="Acer",
            model_series="Acer Enterprise Series-0725",
            chassis_form_factor="Ultrabook 14-inch" if 725 % 3 == 0 else "Workstation 16-inch" if 725 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (725 % 35),
            ram_standard="DDR5-5600" if 725 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 725 % 2 == 0 else 32,
            nvme_slots=2 if 725 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 725 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (725 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 725 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00726(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00726."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00726",
            brand="MSI",
            model_series="MSI Enterprise Series-0726",
            chassis_form_factor="Ultrabook 14-inch" if 726 % 3 == 0 else "Workstation 16-inch" if 726 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (726 % 35),
            ram_standard="DDR5-5600" if 726 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 726 % 2 == 0 else 32,
            nvme_slots=2 if 726 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 726 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (726 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 726 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00727(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00727."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00727",
            brand="Razer",
            model_series="Razer Enterprise Series-0727",
            chassis_form_factor="Ultrabook 14-inch" if 727 % 3 == 0 else "Workstation 16-inch" if 727 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (727 % 35),
            ram_standard="DDR5-5600" if 727 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 727 % 2 == 0 else 32,
            nvme_slots=2 if 727 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 727 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (727 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 727 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00728(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00728."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00728",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0728",
            chassis_form_factor="Ultrabook 14-inch" if 728 % 3 == 0 else "Workstation 16-inch" if 728 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (728 % 35),
            ram_standard="DDR5-5600" if 728 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 728 % 2 == 0 else 32,
            nvme_slots=2 if 728 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 728 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (728 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 728 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00729(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00729."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00729",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0729",
            chassis_form_factor="Ultrabook 14-inch" if 729 % 3 == 0 else "Workstation 16-inch" if 729 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (729 % 35),
            ram_standard="DDR5-5600" if 729 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 729 % 2 == 0 else 32,
            nvme_slots=2 if 729 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 729 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (729 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 729 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00730(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00730."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00730",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0730",
            chassis_form_factor="Ultrabook 14-inch" if 730 % 3 == 0 else "Workstation 16-inch" if 730 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (730 % 35),
            ram_standard="DDR5-5600" if 730 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 730 % 2 == 0 else 32,
            nvme_slots=2 if 730 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 730 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (730 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 730 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00731(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00731."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00731",
            brand="Dell",
            model_series="Dell Enterprise Series-0731",
            chassis_form_factor="Ultrabook 14-inch" if 731 % 3 == 0 else "Workstation 16-inch" if 731 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (731 % 35),
            ram_standard="DDR5-5600" if 731 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 731 % 2 == 0 else 32,
            nvme_slots=2 if 731 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 731 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (731 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 731 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00732(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00732."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00732",
            brand="HP",
            model_series="HP Enterprise Series-0732",
            chassis_form_factor="Ultrabook 14-inch" if 732 % 3 == 0 else "Workstation 16-inch" if 732 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (732 % 35),
            ram_standard="DDR5-5600" if 732 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 732 % 2 == 0 else 32,
            nvme_slots=2 if 732 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 732 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (732 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 732 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00733(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00733."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00733",
            brand="Apple",
            model_series="Apple Enterprise Series-0733",
            chassis_form_factor="Ultrabook 14-inch" if 733 % 3 == 0 else "Workstation 16-inch" if 733 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (733 % 35),
            ram_standard="DDR5-5600" if 733 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 733 % 2 == 0 else 32,
            nvme_slots=2 if 733 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 733 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (733 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 733 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00734(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00734."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00734",
            brand="Asus",
            model_series="Asus Enterprise Series-0734",
            chassis_form_factor="Ultrabook 14-inch" if 734 % 3 == 0 else "Workstation 16-inch" if 734 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (734 % 35),
            ram_standard="DDR5-5600" if 734 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 734 % 2 == 0 else 32,
            nvme_slots=2 if 734 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 734 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (734 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 734 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00735(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00735."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00735",
            brand="Acer",
            model_series="Acer Enterprise Series-0735",
            chassis_form_factor="Ultrabook 14-inch" if 735 % 3 == 0 else "Workstation 16-inch" if 735 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (735 % 35),
            ram_standard="DDR5-5600" if 735 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 735 % 2 == 0 else 32,
            nvme_slots=2 if 735 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 735 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (735 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 735 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00736(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00736."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00736",
            brand="MSI",
            model_series="MSI Enterprise Series-0736",
            chassis_form_factor="Ultrabook 14-inch" if 736 % 3 == 0 else "Workstation 16-inch" if 736 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (736 % 35),
            ram_standard="DDR5-5600" if 736 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 736 % 2 == 0 else 32,
            nvme_slots=2 if 736 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 736 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (736 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 736 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00737(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00737."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00737",
            brand="Razer",
            model_series="Razer Enterprise Series-0737",
            chassis_form_factor="Ultrabook 14-inch" if 737 % 3 == 0 else "Workstation 16-inch" if 737 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (737 % 35),
            ram_standard="DDR5-5600" if 737 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 737 % 2 == 0 else 32,
            nvme_slots=2 if 737 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 737 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (737 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 737 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00738(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00738."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00738",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0738",
            chassis_form_factor="Ultrabook 14-inch" if 738 % 3 == 0 else "Workstation 16-inch" if 738 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (738 % 35),
            ram_standard="DDR5-5600" if 738 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 738 % 2 == 0 else 32,
            nvme_slots=2 if 738 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 738 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (738 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 738 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00739(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00739."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00739",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0739",
            chassis_form_factor="Ultrabook 14-inch" if 739 % 3 == 0 else "Workstation 16-inch" if 739 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (739 % 35),
            ram_standard="DDR5-5600" if 739 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 739 % 2 == 0 else 32,
            nvme_slots=2 if 739 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 739 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (739 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 739 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00740(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00740."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00740",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0740",
            chassis_form_factor="Ultrabook 14-inch" if 740 % 3 == 0 else "Workstation 16-inch" if 740 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (740 % 35),
            ram_standard="DDR5-5600" if 740 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 740 % 2 == 0 else 32,
            nvme_slots=2 if 740 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 740 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (740 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 740 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00741(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00741."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00741",
            brand="Dell",
            model_series="Dell Enterprise Series-0741",
            chassis_form_factor="Ultrabook 14-inch" if 741 % 3 == 0 else "Workstation 16-inch" if 741 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (741 % 35),
            ram_standard="DDR5-5600" if 741 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 741 % 2 == 0 else 32,
            nvme_slots=2 if 741 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 741 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (741 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 741 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00742(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00742."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00742",
            brand="HP",
            model_series="HP Enterprise Series-0742",
            chassis_form_factor="Ultrabook 14-inch" if 742 % 3 == 0 else "Workstation 16-inch" if 742 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (742 % 35),
            ram_standard="DDR5-5600" if 742 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 742 % 2 == 0 else 32,
            nvme_slots=2 if 742 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 742 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (742 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 742 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00743(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00743."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00743",
            brand="Apple",
            model_series="Apple Enterprise Series-0743",
            chassis_form_factor="Ultrabook 14-inch" if 743 % 3 == 0 else "Workstation 16-inch" if 743 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (743 % 35),
            ram_standard="DDR5-5600" if 743 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 743 % 2 == 0 else 32,
            nvme_slots=2 if 743 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 743 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (743 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 743 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00744(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00744."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00744",
            brand="Asus",
            model_series="Asus Enterprise Series-0744",
            chassis_form_factor="Ultrabook 14-inch" if 744 % 3 == 0 else "Workstation 16-inch" if 744 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (744 % 35),
            ram_standard="DDR5-5600" if 744 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 744 % 2 == 0 else 32,
            nvme_slots=2 if 744 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 744 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (744 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 744 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00745(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00745."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00745",
            brand="Acer",
            model_series="Acer Enterprise Series-0745",
            chassis_form_factor="Ultrabook 14-inch" if 745 % 3 == 0 else "Workstation 16-inch" if 745 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (745 % 35),
            ram_standard="DDR5-5600" if 745 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 745 % 2 == 0 else 32,
            nvme_slots=2 if 745 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 745 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (745 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 745 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00746(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00746."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00746",
            brand="MSI",
            model_series="MSI Enterprise Series-0746",
            chassis_form_factor="Ultrabook 14-inch" if 746 % 3 == 0 else "Workstation 16-inch" if 746 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (746 % 35),
            ram_standard="DDR5-5600" if 746 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 746 % 2 == 0 else 32,
            nvme_slots=2 if 746 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 746 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (746 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 746 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00747(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00747."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00747",
            brand="Razer",
            model_series="Razer Enterprise Series-0747",
            chassis_form_factor="Ultrabook 14-inch" if 747 % 3 == 0 else "Workstation 16-inch" if 747 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (747 % 35),
            ram_standard="DDR5-5600" if 747 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 747 % 2 == 0 else 32,
            nvme_slots=2 if 747 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 747 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (747 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 747 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00748(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00748."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00748",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0748",
            chassis_form_factor="Ultrabook 14-inch" if 748 % 3 == 0 else "Workstation 16-inch" if 748 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (748 % 35),
            ram_standard="DDR5-5600" if 748 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 748 % 2 == 0 else 32,
            nvme_slots=2 if 748 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 748 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (748 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 748 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00749(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00749."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00749",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0749",
            chassis_form_factor="Ultrabook 14-inch" if 749 % 3 == 0 else "Workstation 16-inch" if 749 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (749 % 35),
            ram_standard="DDR5-5600" if 749 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 749 % 2 == 0 else 32,
            nvme_slots=2 if 749 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 749 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (749 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 749 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00750(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00750."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00750",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0750",
            chassis_form_factor="Ultrabook 14-inch" if 750 % 3 == 0 else "Workstation 16-inch" if 750 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (750 % 35),
            ram_standard="DDR5-5600" if 750 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 750 % 2 == 0 else 32,
            nvme_slots=2 if 750 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 750 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (750 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 750 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00751(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00751."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00751",
            brand="Dell",
            model_series="Dell Enterprise Series-0751",
            chassis_form_factor="Ultrabook 14-inch" if 751 % 3 == 0 else "Workstation 16-inch" if 751 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (751 % 35),
            ram_standard="DDR5-5600" if 751 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 751 % 2 == 0 else 32,
            nvme_slots=2 if 751 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 751 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (751 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 751 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00752(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00752."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00752",
            brand="HP",
            model_series="HP Enterprise Series-0752",
            chassis_form_factor="Ultrabook 14-inch" if 752 % 3 == 0 else "Workstation 16-inch" if 752 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (752 % 35),
            ram_standard="DDR5-5600" if 752 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 752 % 2 == 0 else 32,
            nvme_slots=2 if 752 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 752 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (752 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 752 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00753(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00753."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00753",
            brand="Apple",
            model_series="Apple Enterprise Series-0753",
            chassis_form_factor="Ultrabook 14-inch" if 753 % 3 == 0 else "Workstation 16-inch" if 753 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (753 % 35),
            ram_standard="DDR5-5600" if 753 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 753 % 2 == 0 else 32,
            nvme_slots=2 if 753 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 753 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (753 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 753 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00754(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00754."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00754",
            brand="Asus",
            model_series="Asus Enterprise Series-0754",
            chassis_form_factor="Ultrabook 14-inch" if 754 % 3 == 0 else "Workstation 16-inch" if 754 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (754 % 35),
            ram_standard="DDR5-5600" if 754 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 754 % 2 == 0 else 32,
            nvme_slots=2 if 754 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 754 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (754 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 754 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00755(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00755."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00755",
            brand="Acer",
            model_series="Acer Enterprise Series-0755",
            chassis_form_factor="Ultrabook 14-inch" if 755 % 3 == 0 else "Workstation 16-inch" if 755 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (755 % 35),
            ram_standard="DDR5-5600" if 755 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 755 % 2 == 0 else 32,
            nvme_slots=2 if 755 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 755 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (755 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 755 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00756(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00756."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00756",
            brand="MSI",
            model_series="MSI Enterprise Series-0756",
            chassis_form_factor="Ultrabook 14-inch" if 756 % 3 == 0 else "Workstation 16-inch" if 756 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (756 % 35),
            ram_standard="DDR5-5600" if 756 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 756 % 2 == 0 else 32,
            nvme_slots=2 if 756 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 756 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (756 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 756 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00757(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00757."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00757",
            brand="Razer",
            model_series="Razer Enterprise Series-0757",
            chassis_form_factor="Ultrabook 14-inch" if 757 % 3 == 0 else "Workstation 16-inch" if 757 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (757 % 35),
            ram_standard="DDR5-5600" if 757 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 757 % 2 == 0 else 32,
            nvme_slots=2 if 757 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 757 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (757 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 757 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00758(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00758."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00758",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0758",
            chassis_form_factor="Ultrabook 14-inch" if 758 % 3 == 0 else "Workstation 16-inch" if 758 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (758 % 35),
            ram_standard="DDR5-5600" if 758 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 758 % 2 == 0 else 32,
            nvme_slots=2 if 758 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 758 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (758 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 758 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00759(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00759."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00759",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0759",
            chassis_form_factor="Ultrabook 14-inch" if 759 % 3 == 0 else "Workstation 16-inch" if 759 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (759 % 35),
            ram_standard="DDR5-5600" if 759 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 759 % 2 == 0 else 32,
            nvme_slots=2 if 759 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 759 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (759 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 759 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00760(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00760."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00760",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0760",
            chassis_form_factor="Ultrabook 14-inch" if 760 % 3 == 0 else "Workstation 16-inch" if 760 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (760 % 35),
            ram_standard="DDR5-5600" if 760 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 760 % 2 == 0 else 32,
            nvme_slots=2 if 760 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 760 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (760 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 760 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00761(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00761."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00761",
            brand="Dell",
            model_series="Dell Enterprise Series-0761",
            chassis_form_factor="Ultrabook 14-inch" if 761 % 3 == 0 else "Workstation 16-inch" if 761 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (761 % 35),
            ram_standard="DDR5-5600" if 761 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 761 % 2 == 0 else 32,
            nvme_slots=2 if 761 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 761 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (761 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 761 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00762(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00762."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00762",
            brand="HP",
            model_series="HP Enterprise Series-0762",
            chassis_form_factor="Ultrabook 14-inch" if 762 % 3 == 0 else "Workstation 16-inch" if 762 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (762 % 35),
            ram_standard="DDR5-5600" if 762 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 762 % 2 == 0 else 32,
            nvme_slots=2 if 762 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 762 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (762 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 762 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00763(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00763."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00763",
            brand="Apple",
            model_series="Apple Enterprise Series-0763",
            chassis_form_factor="Ultrabook 14-inch" if 763 % 3 == 0 else "Workstation 16-inch" if 763 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (763 % 35),
            ram_standard="DDR5-5600" if 763 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 763 % 2 == 0 else 32,
            nvme_slots=2 if 763 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 763 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (763 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 763 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00764(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00764."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00764",
            brand="Asus",
            model_series="Asus Enterprise Series-0764",
            chassis_form_factor="Ultrabook 14-inch" if 764 % 3 == 0 else "Workstation 16-inch" if 764 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (764 % 35),
            ram_standard="DDR5-5600" if 764 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 764 % 2 == 0 else 32,
            nvme_slots=2 if 764 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 764 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (764 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 764 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00765(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00765."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00765",
            brand="Acer",
            model_series="Acer Enterprise Series-0765",
            chassis_form_factor="Ultrabook 14-inch" if 765 % 3 == 0 else "Workstation 16-inch" if 765 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (765 % 35),
            ram_standard="DDR5-5600" if 765 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 765 % 2 == 0 else 32,
            nvme_slots=2 if 765 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 765 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (765 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 765 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00766(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00766."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00766",
            brand="MSI",
            model_series="MSI Enterprise Series-0766",
            chassis_form_factor="Ultrabook 14-inch" if 766 % 3 == 0 else "Workstation 16-inch" if 766 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (766 % 35),
            ram_standard="DDR5-5600" if 766 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 766 % 2 == 0 else 32,
            nvme_slots=2 if 766 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 766 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (766 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 766 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00767(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00767."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00767",
            brand="Razer",
            model_series="Razer Enterprise Series-0767",
            chassis_form_factor="Ultrabook 14-inch" if 767 % 3 == 0 else "Workstation 16-inch" if 767 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (767 % 35),
            ram_standard="DDR5-5600" if 767 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 767 % 2 == 0 else 32,
            nvme_slots=2 if 767 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 767 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (767 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 767 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00768(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00768."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00768",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0768",
            chassis_form_factor="Ultrabook 14-inch" if 768 % 3 == 0 else "Workstation 16-inch" if 768 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (768 % 35),
            ram_standard="DDR5-5600" if 768 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 768 % 2 == 0 else 32,
            nvme_slots=2 if 768 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 768 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (768 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 768 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00769(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00769."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00769",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0769",
            chassis_form_factor="Ultrabook 14-inch" if 769 % 3 == 0 else "Workstation 16-inch" if 769 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (769 % 35),
            ram_standard="DDR5-5600" if 769 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 769 % 2 == 0 else 32,
            nvme_slots=2 if 769 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 769 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (769 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 769 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00770(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00770."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00770",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0770",
            chassis_form_factor="Ultrabook 14-inch" if 770 % 3 == 0 else "Workstation 16-inch" if 770 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (770 % 35),
            ram_standard="DDR5-5600" if 770 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 770 % 2 == 0 else 32,
            nvme_slots=2 if 770 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 770 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (770 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 770 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00771(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00771."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00771",
            brand="Dell",
            model_series="Dell Enterprise Series-0771",
            chassis_form_factor="Ultrabook 14-inch" if 771 % 3 == 0 else "Workstation 16-inch" if 771 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (771 % 35),
            ram_standard="DDR5-5600" if 771 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 771 % 2 == 0 else 32,
            nvme_slots=2 if 771 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 771 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (771 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 771 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00772(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00772."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00772",
            brand="HP",
            model_series="HP Enterprise Series-0772",
            chassis_form_factor="Ultrabook 14-inch" if 772 % 3 == 0 else "Workstation 16-inch" if 772 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (772 % 35),
            ram_standard="DDR5-5600" if 772 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 772 % 2 == 0 else 32,
            nvme_slots=2 if 772 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 772 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (772 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 772 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00773(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00773."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00773",
            brand="Apple",
            model_series="Apple Enterprise Series-0773",
            chassis_form_factor="Ultrabook 14-inch" if 773 % 3 == 0 else "Workstation 16-inch" if 773 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (773 % 35),
            ram_standard="DDR5-5600" if 773 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 773 % 2 == 0 else 32,
            nvme_slots=2 if 773 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 773 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (773 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 773 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00774(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00774."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00774",
            brand="Asus",
            model_series="Asus Enterprise Series-0774",
            chassis_form_factor="Ultrabook 14-inch" if 774 % 3 == 0 else "Workstation 16-inch" if 774 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (774 % 35),
            ram_standard="DDR5-5600" if 774 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 774 % 2 == 0 else 32,
            nvme_slots=2 if 774 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 774 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (774 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 774 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00775(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00775."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00775",
            brand="Acer",
            model_series="Acer Enterprise Series-0775",
            chassis_form_factor="Ultrabook 14-inch" if 775 % 3 == 0 else "Workstation 16-inch" if 775 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (775 % 35),
            ram_standard="DDR5-5600" if 775 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 775 % 2 == 0 else 32,
            nvme_slots=2 if 775 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 775 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (775 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 775 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00776(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00776."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00776",
            brand="MSI",
            model_series="MSI Enterprise Series-0776",
            chassis_form_factor="Ultrabook 14-inch" if 776 % 3 == 0 else "Workstation 16-inch" if 776 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (776 % 35),
            ram_standard="DDR5-5600" if 776 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 776 % 2 == 0 else 32,
            nvme_slots=2 if 776 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 776 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (776 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 776 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00777(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00777."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00777",
            brand="Razer",
            model_series="Razer Enterprise Series-0777",
            chassis_form_factor="Ultrabook 14-inch" if 777 % 3 == 0 else "Workstation 16-inch" if 777 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (777 % 35),
            ram_standard="DDR5-5600" if 777 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 777 % 2 == 0 else 32,
            nvme_slots=2 if 777 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 777 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (777 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 777 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00778(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00778."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00778",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0778",
            chassis_form_factor="Ultrabook 14-inch" if 778 % 3 == 0 else "Workstation 16-inch" if 778 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (778 % 35),
            ram_standard="DDR5-5600" if 778 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 778 % 2 == 0 else 32,
            nvme_slots=2 if 778 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 778 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (778 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 778 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00779(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00779."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00779",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0779",
            chassis_form_factor="Ultrabook 14-inch" if 779 % 3 == 0 else "Workstation 16-inch" if 779 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (779 % 35),
            ram_standard="DDR5-5600" if 779 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 779 % 2 == 0 else 32,
            nvme_slots=2 if 779 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 779 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (779 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 779 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00780(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00780."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00780",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0780",
            chassis_form_factor="Ultrabook 14-inch" if 780 % 3 == 0 else "Workstation 16-inch" if 780 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (780 % 35),
            ram_standard="DDR5-5600" if 780 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 780 % 2 == 0 else 32,
            nvme_slots=2 if 780 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 780 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (780 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 780 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00781(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00781."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00781",
            brand="Dell",
            model_series="Dell Enterprise Series-0781",
            chassis_form_factor="Ultrabook 14-inch" if 781 % 3 == 0 else "Workstation 16-inch" if 781 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (781 % 35),
            ram_standard="DDR5-5600" if 781 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 781 % 2 == 0 else 32,
            nvme_slots=2 if 781 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 781 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (781 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 781 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00782(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00782."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00782",
            brand="HP",
            model_series="HP Enterprise Series-0782",
            chassis_form_factor="Ultrabook 14-inch" if 782 % 3 == 0 else "Workstation 16-inch" if 782 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (782 % 35),
            ram_standard="DDR5-5600" if 782 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 782 % 2 == 0 else 32,
            nvme_slots=2 if 782 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 782 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (782 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 782 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00783(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00783."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00783",
            brand="Apple",
            model_series="Apple Enterprise Series-0783",
            chassis_form_factor="Ultrabook 14-inch" if 783 % 3 == 0 else "Workstation 16-inch" if 783 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (783 % 35),
            ram_standard="DDR5-5600" if 783 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 783 % 2 == 0 else 32,
            nvme_slots=2 if 783 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 783 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (783 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 783 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00784(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00784."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00784",
            brand="Asus",
            model_series="Asus Enterprise Series-0784",
            chassis_form_factor="Ultrabook 14-inch" if 784 % 3 == 0 else "Workstation 16-inch" if 784 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (784 % 35),
            ram_standard="DDR5-5600" if 784 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 784 % 2 == 0 else 32,
            nvme_slots=2 if 784 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 784 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (784 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 784 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00785(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00785."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00785",
            brand="Acer",
            model_series="Acer Enterprise Series-0785",
            chassis_form_factor="Ultrabook 14-inch" if 785 % 3 == 0 else "Workstation 16-inch" if 785 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (785 % 35),
            ram_standard="DDR5-5600" if 785 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 785 % 2 == 0 else 32,
            nvme_slots=2 if 785 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 785 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (785 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 785 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00786(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00786."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00786",
            brand="MSI",
            model_series="MSI Enterprise Series-0786",
            chassis_form_factor="Ultrabook 14-inch" if 786 % 3 == 0 else "Workstation 16-inch" if 786 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (786 % 35),
            ram_standard="DDR5-5600" if 786 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 786 % 2 == 0 else 32,
            nvme_slots=2 if 786 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 786 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (786 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 786 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00787(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00787."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00787",
            brand="Razer",
            model_series="Razer Enterprise Series-0787",
            chassis_form_factor="Ultrabook 14-inch" if 787 % 3 == 0 else "Workstation 16-inch" if 787 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (787 % 35),
            ram_standard="DDR5-5600" if 787 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 787 % 2 == 0 else 32,
            nvme_slots=2 if 787 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 787 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (787 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 787 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00788(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00788."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00788",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0788",
            chassis_form_factor="Ultrabook 14-inch" if 788 % 3 == 0 else "Workstation 16-inch" if 788 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (788 % 35),
            ram_standard="DDR5-5600" if 788 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 788 % 2 == 0 else 32,
            nvme_slots=2 if 788 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 788 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (788 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 788 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00789(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00789."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00789",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0789",
            chassis_form_factor="Ultrabook 14-inch" if 789 % 3 == 0 else "Workstation 16-inch" if 789 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (789 % 35),
            ram_standard="DDR5-5600" if 789 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 789 % 2 == 0 else 32,
            nvme_slots=2 if 789 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 789 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (789 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 789 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00790(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00790."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00790",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0790",
            chassis_form_factor="Ultrabook 14-inch" if 790 % 3 == 0 else "Workstation 16-inch" if 790 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (790 % 35),
            ram_standard="DDR5-5600" if 790 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 790 % 2 == 0 else 32,
            nvme_slots=2 if 790 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 790 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (790 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 790 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00791(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00791."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00791",
            brand="Dell",
            model_series="Dell Enterprise Series-0791",
            chassis_form_factor="Ultrabook 14-inch" if 791 % 3 == 0 else "Workstation 16-inch" if 791 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (791 % 35),
            ram_standard="DDR5-5600" if 791 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 791 % 2 == 0 else 32,
            nvme_slots=2 if 791 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 791 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (791 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 791 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00792(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00792."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00792",
            brand="HP",
            model_series="HP Enterprise Series-0792",
            chassis_form_factor="Ultrabook 14-inch" if 792 % 3 == 0 else "Workstation 16-inch" if 792 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (792 % 35),
            ram_standard="DDR5-5600" if 792 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 792 % 2 == 0 else 32,
            nvme_slots=2 if 792 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 792 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (792 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 792 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00793(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00793."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00793",
            brand="Apple",
            model_series="Apple Enterprise Series-0793",
            chassis_form_factor="Ultrabook 14-inch" if 793 % 3 == 0 else "Workstation 16-inch" if 793 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (793 % 35),
            ram_standard="DDR5-5600" if 793 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 793 % 2 == 0 else 32,
            nvme_slots=2 if 793 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 793 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (793 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 793 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00794(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00794."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00794",
            brand="Asus",
            model_series="Asus Enterprise Series-0794",
            chassis_form_factor="Ultrabook 14-inch" if 794 % 3 == 0 else "Workstation 16-inch" if 794 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (794 % 35),
            ram_standard="DDR5-5600" if 794 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 794 % 2 == 0 else 32,
            nvme_slots=2 if 794 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 794 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (794 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 794 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00795(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00795."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00795",
            brand="Acer",
            model_series="Acer Enterprise Series-0795",
            chassis_form_factor="Ultrabook 14-inch" if 795 % 3 == 0 else "Workstation 16-inch" if 795 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (795 % 35),
            ram_standard="DDR5-5600" if 795 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 795 % 2 == 0 else 32,
            nvme_slots=2 if 795 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 795 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (795 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 795 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00796(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00796."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00796",
            brand="MSI",
            model_series="MSI Enterprise Series-0796",
            chassis_form_factor="Ultrabook 14-inch" if 796 % 3 == 0 else "Workstation 16-inch" if 796 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (796 % 35),
            ram_standard="DDR5-5600" if 796 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 796 % 2 == 0 else 32,
            nvme_slots=2 if 796 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 796 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (796 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 796 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00797(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00797."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00797",
            brand="Razer",
            model_series="Razer Enterprise Series-0797",
            chassis_form_factor="Ultrabook 14-inch" if 797 % 3 == 0 else "Workstation 16-inch" if 797 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (797 % 35),
            ram_standard="DDR5-5600" if 797 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 797 % 2 == 0 else 32,
            nvme_slots=2 if 797 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 797 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (797 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 797 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00798(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00798."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00798",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0798",
            chassis_form_factor="Ultrabook 14-inch" if 798 % 3 == 0 else "Workstation 16-inch" if 798 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (798 % 35),
            ram_standard="DDR5-5600" if 798 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 798 % 2 == 0 else 32,
            nvme_slots=2 if 798 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 798 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (798 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 798 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00799(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00799."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00799",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0799",
            chassis_form_factor="Ultrabook 14-inch" if 799 % 3 == 0 else "Workstation 16-inch" if 799 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (799 % 35),
            ram_standard="DDR5-5600" if 799 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 799 % 2 == 0 else 32,
            nvme_slots=2 if 799 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 799 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (799 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 799 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00800(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00800."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00800",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0800",
            chassis_form_factor="Ultrabook 14-inch" if 800 % 3 == 0 else "Workstation 16-inch" if 800 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (800 % 35),
            ram_standard="DDR5-5600" if 800 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 800 % 2 == 0 else 32,
            nvme_slots=2 if 800 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 800 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (800 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 800 % 2 == 0 else "1-Year Depot Warranty",
        )
