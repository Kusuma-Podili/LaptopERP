"""
Enterprise Hardware Model Database - Part 05.
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

class HardwareCatalogDatabasePart05:
    """Hardware inventory profile definitions part 05."""

    @classmethod
    def get_hardware_profile_00801(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00801."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00801",
            brand="Dell",
            model_series="Dell Enterprise Series-0801",
            chassis_form_factor="Ultrabook 14-inch" if 801 % 3 == 0 else "Workstation 16-inch" if 801 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (801 % 35),
            ram_standard="DDR5-5600" if 801 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 801 % 2 == 0 else 32,
            nvme_slots=2 if 801 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 801 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (801 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 801 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00802(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00802."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00802",
            brand="HP",
            model_series="HP Enterprise Series-0802",
            chassis_form_factor="Ultrabook 14-inch" if 802 % 3 == 0 else "Workstation 16-inch" if 802 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (802 % 35),
            ram_standard="DDR5-5600" if 802 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 802 % 2 == 0 else 32,
            nvme_slots=2 if 802 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 802 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (802 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 802 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00803(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00803."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00803",
            brand="Apple",
            model_series="Apple Enterprise Series-0803",
            chassis_form_factor="Ultrabook 14-inch" if 803 % 3 == 0 else "Workstation 16-inch" if 803 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (803 % 35),
            ram_standard="DDR5-5600" if 803 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 803 % 2 == 0 else 32,
            nvme_slots=2 if 803 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 803 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (803 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 803 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00804(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00804."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00804",
            brand="Asus",
            model_series="Asus Enterprise Series-0804",
            chassis_form_factor="Ultrabook 14-inch" if 804 % 3 == 0 else "Workstation 16-inch" if 804 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (804 % 35),
            ram_standard="DDR5-5600" if 804 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 804 % 2 == 0 else 32,
            nvme_slots=2 if 804 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 804 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (804 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 804 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00805(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00805."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00805",
            brand="Acer",
            model_series="Acer Enterprise Series-0805",
            chassis_form_factor="Ultrabook 14-inch" if 805 % 3 == 0 else "Workstation 16-inch" if 805 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (805 % 35),
            ram_standard="DDR5-5600" if 805 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 805 % 2 == 0 else 32,
            nvme_slots=2 if 805 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 805 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (805 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 805 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00806(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00806."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00806",
            brand="MSI",
            model_series="MSI Enterprise Series-0806",
            chassis_form_factor="Ultrabook 14-inch" if 806 % 3 == 0 else "Workstation 16-inch" if 806 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (806 % 35),
            ram_standard="DDR5-5600" if 806 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 806 % 2 == 0 else 32,
            nvme_slots=2 if 806 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 806 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (806 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 806 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00807(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00807."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00807",
            brand="Razer",
            model_series="Razer Enterprise Series-0807",
            chassis_form_factor="Ultrabook 14-inch" if 807 % 3 == 0 else "Workstation 16-inch" if 807 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (807 % 35),
            ram_standard="DDR5-5600" if 807 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 807 % 2 == 0 else 32,
            nvme_slots=2 if 807 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 807 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (807 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 807 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00808(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00808."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00808",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0808",
            chassis_form_factor="Ultrabook 14-inch" if 808 % 3 == 0 else "Workstation 16-inch" if 808 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (808 % 35),
            ram_standard="DDR5-5600" if 808 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 808 % 2 == 0 else 32,
            nvme_slots=2 if 808 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 808 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (808 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 808 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00809(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00809."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00809",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0809",
            chassis_form_factor="Ultrabook 14-inch" if 809 % 3 == 0 else "Workstation 16-inch" if 809 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (809 % 35),
            ram_standard="DDR5-5600" if 809 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 809 % 2 == 0 else 32,
            nvme_slots=2 if 809 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 809 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (809 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 809 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00810(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00810."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00810",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0810",
            chassis_form_factor="Ultrabook 14-inch" if 810 % 3 == 0 else "Workstation 16-inch" if 810 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (810 % 35),
            ram_standard="DDR5-5600" if 810 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 810 % 2 == 0 else 32,
            nvme_slots=2 if 810 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 810 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (810 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 810 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00811(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00811."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00811",
            brand="Dell",
            model_series="Dell Enterprise Series-0811",
            chassis_form_factor="Ultrabook 14-inch" if 811 % 3 == 0 else "Workstation 16-inch" if 811 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (811 % 35),
            ram_standard="DDR5-5600" if 811 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 811 % 2 == 0 else 32,
            nvme_slots=2 if 811 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 811 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (811 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 811 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00812(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00812."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00812",
            brand="HP",
            model_series="HP Enterprise Series-0812",
            chassis_form_factor="Ultrabook 14-inch" if 812 % 3 == 0 else "Workstation 16-inch" if 812 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (812 % 35),
            ram_standard="DDR5-5600" if 812 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 812 % 2 == 0 else 32,
            nvme_slots=2 if 812 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 812 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (812 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 812 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00813(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00813."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00813",
            brand="Apple",
            model_series="Apple Enterprise Series-0813",
            chassis_form_factor="Ultrabook 14-inch" if 813 % 3 == 0 else "Workstation 16-inch" if 813 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (813 % 35),
            ram_standard="DDR5-5600" if 813 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 813 % 2 == 0 else 32,
            nvme_slots=2 if 813 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 813 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (813 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 813 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00814(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00814."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00814",
            brand="Asus",
            model_series="Asus Enterprise Series-0814",
            chassis_form_factor="Ultrabook 14-inch" if 814 % 3 == 0 else "Workstation 16-inch" if 814 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (814 % 35),
            ram_standard="DDR5-5600" if 814 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 814 % 2 == 0 else 32,
            nvme_slots=2 if 814 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 814 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (814 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 814 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00815(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00815."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00815",
            brand="Acer",
            model_series="Acer Enterprise Series-0815",
            chassis_form_factor="Ultrabook 14-inch" if 815 % 3 == 0 else "Workstation 16-inch" if 815 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (815 % 35),
            ram_standard="DDR5-5600" if 815 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 815 % 2 == 0 else 32,
            nvme_slots=2 if 815 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 815 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (815 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 815 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00816(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00816."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00816",
            brand="MSI",
            model_series="MSI Enterprise Series-0816",
            chassis_form_factor="Ultrabook 14-inch" if 816 % 3 == 0 else "Workstation 16-inch" if 816 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (816 % 35),
            ram_standard="DDR5-5600" if 816 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 816 % 2 == 0 else 32,
            nvme_slots=2 if 816 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 816 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (816 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 816 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00817(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00817."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00817",
            brand="Razer",
            model_series="Razer Enterprise Series-0817",
            chassis_form_factor="Ultrabook 14-inch" if 817 % 3 == 0 else "Workstation 16-inch" if 817 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (817 % 35),
            ram_standard="DDR5-5600" if 817 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 817 % 2 == 0 else 32,
            nvme_slots=2 if 817 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 817 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (817 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 817 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00818(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00818."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00818",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0818",
            chassis_form_factor="Ultrabook 14-inch" if 818 % 3 == 0 else "Workstation 16-inch" if 818 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (818 % 35),
            ram_standard="DDR5-5600" if 818 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 818 % 2 == 0 else 32,
            nvme_slots=2 if 818 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 818 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (818 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 818 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00819(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00819."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00819",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0819",
            chassis_form_factor="Ultrabook 14-inch" if 819 % 3 == 0 else "Workstation 16-inch" if 819 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (819 % 35),
            ram_standard="DDR5-5600" if 819 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 819 % 2 == 0 else 32,
            nvme_slots=2 if 819 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 819 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (819 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 819 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00820(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00820."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00820",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0820",
            chassis_form_factor="Ultrabook 14-inch" if 820 % 3 == 0 else "Workstation 16-inch" if 820 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (820 % 35),
            ram_standard="DDR5-5600" if 820 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 820 % 2 == 0 else 32,
            nvme_slots=2 if 820 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 820 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (820 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 820 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00821(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00821."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00821",
            brand="Dell",
            model_series="Dell Enterprise Series-0821",
            chassis_form_factor="Ultrabook 14-inch" if 821 % 3 == 0 else "Workstation 16-inch" if 821 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (821 % 35),
            ram_standard="DDR5-5600" if 821 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 821 % 2 == 0 else 32,
            nvme_slots=2 if 821 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 821 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (821 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 821 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00822(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00822."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00822",
            brand="HP",
            model_series="HP Enterprise Series-0822",
            chassis_form_factor="Ultrabook 14-inch" if 822 % 3 == 0 else "Workstation 16-inch" if 822 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (822 % 35),
            ram_standard="DDR5-5600" if 822 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 822 % 2 == 0 else 32,
            nvme_slots=2 if 822 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 822 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (822 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 822 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00823(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00823."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00823",
            brand="Apple",
            model_series="Apple Enterprise Series-0823",
            chassis_form_factor="Ultrabook 14-inch" if 823 % 3 == 0 else "Workstation 16-inch" if 823 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (823 % 35),
            ram_standard="DDR5-5600" if 823 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 823 % 2 == 0 else 32,
            nvme_slots=2 if 823 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 823 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (823 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 823 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00824(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00824."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00824",
            brand="Asus",
            model_series="Asus Enterprise Series-0824",
            chassis_form_factor="Ultrabook 14-inch" if 824 % 3 == 0 else "Workstation 16-inch" if 824 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (824 % 35),
            ram_standard="DDR5-5600" if 824 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 824 % 2 == 0 else 32,
            nvme_slots=2 if 824 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 824 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (824 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 824 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00825(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00825."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00825",
            brand="Acer",
            model_series="Acer Enterprise Series-0825",
            chassis_form_factor="Ultrabook 14-inch" if 825 % 3 == 0 else "Workstation 16-inch" if 825 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (825 % 35),
            ram_standard="DDR5-5600" if 825 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 825 % 2 == 0 else 32,
            nvme_slots=2 if 825 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 825 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (825 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 825 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00826(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00826."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00826",
            brand="MSI",
            model_series="MSI Enterprise Series-0826",
            chassis_form_factor="Ultrabook 14-inch" if 826 % 3 == 0 else "Workstation 16-inch" if 826 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (826 % 35),
            ram_standard="DDR5-5600" if 826 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 826 % 2 == 0 else 32,
            nvme_slots=2 if 826 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 826 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (826 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 826 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00827(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00827."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00827",
            brand="Razer",
            model_series="Razer Enterprise Series-0827",
            chassis_form_factor="Ultrabook 14-inch" if 827 % 3 == 0 else "Workstation 16-inch" if 827 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (827 % 35),
            ram_standard="DDR5-5600" if 827 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 827 % 2 == 0 else 32,
            nvme_slots=2 if 827 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 827 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (827 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 827 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00828(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00828."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00828",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0828",
            chassis_form_factor="Ultrabook 14-inch" if 828 % 3 == 0 else "Workstation 16-inch" if 828 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (828 % 35),
            ram_standard="DDR5-5600" if 828 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 828 % 2 == 0 else 32,
            nvme_slots=2 if 828 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 828 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (828 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 828 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00829(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00829."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00829",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0829",
            chassis_form_factor="Ultrabook 14-inch" if 829 % 3 == 0 else "Workstation 16-inch" if 829 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (829 % 35),
            ram_standard="DDR5-5600" if 829 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 829 % 2 == 0 else 32,
            nvme_slots=2 if 829 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 829 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (829 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 829 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00830(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00830."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00830",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0830",
            chassis_form_factor="Ultrabook 14-inch" if 830 % 3 == 0 else "Workstation 16-inch" if 830 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (830 % 35),
            ram_standard="DDR5-5600" if 830 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 830 % 2 == 0 else 32,
            nvme_slots=2 if 830 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 830 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (830 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 830 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00831(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00831."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00831",
            brand="Dell",
            model_series="Dell Enterprise Series-0831",
            chassis_form_factor="Ultrabook 14-inch" if 831 % 3 == 0 else "Workstation 16-inch" if 831 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (831 % 35),
            ram_standard="DDR5-5600" if 831 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 831 % 2 == 0 else 32,
            nvme_slots=2 if 831 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 831 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (831 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 831 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00832(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00832."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00832",
            brand="HP",
            model_series="HP Enterprise Series-0832",
            chassis_form_factor="Ultrabook 14-inch" if 832 % 3 == 0 else "Workstation 16-inch" if 832 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (832 % 35),
            ram_standard="DDR5-5600" if 832 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 832 % 2 == 0 else 32,
            nvme_slots=2 if 832 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 832 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (832 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 832 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00833(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00833."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00833",
            brand="Apple",
            model_series="Apple Enterprise Series-0833",
            chassis_form_factor="Ultrabook 14-inch" if 833 % 3 == 0 else "Workstation 16-inch" if 833 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (833 % 35),
            ram_standard="DDR5-5600" if 833 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 833 % 2 == 0 else 32,
            nvme_slots=2 if 833 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 833 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (833 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 833 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00834(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00834."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00834",
            brand="Asus",
            model_series="Asus Enterprise Series-0834",
            chassis_form_factor="Ultrabook 14-inch" if 834 % 3 == 0 else "Workstation 16-inch" if 834 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (834 % 35),
            ram_standard="DDR5-5600" if 834 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 834 % 2 == 0 else 32,
            nvme_slots=2 if 834 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 834 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (834 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 834 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00835(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00835."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00835",
            brand="Acer",
            model_series="Acer Enterprise Series-0835",
            chassis_form_factor="Ultrabook 14-inch" if 835 % 3 == 0 else "Workstation 16-inch" if 835 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (835 % 35),
            ram_standard="DDR5-5600" if 835 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 835 % 2 == 0 else 32,
            nvme_slots=2 if 835 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 835 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (835 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 835 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00836(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00836."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00836",
            brand="MSI",
            model_series="MSI Enterprise Series-0836",
            chassis_form_factor="Ultrabook 14-inch" if 836 % 3 == 0 else "Workstation 16-inch" if 836 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (836 % 35),
            ram_standard="DDR5-5600" if 836 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 836 % 2 == 0 else 32,
            nvme_slots=2 if 836 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 836 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (836 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 836 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00837(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00837."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00837",
            brand="Razer",
            model_series="Razer Enterprise Series-0837",
            chassis_form_factor="Ultrabook 14-inch" if 837 % 3 == 0 else "Workstation 16-inch" if 837 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (837 % 35),
            ram_standard="DDR5-5600" if 837 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 837 % 2 == 0 else 32,
            nvme_slots=2 if 837 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 837 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (837 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 837 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00838(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00838."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00838",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0838",
            chassis_form_factor="Ultrabook 14-inch" if 838 % 3 == 0 else "Workstation 16-inch" if 838 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (838 % 35),
            ram_standard="DDR5-5600" if 838 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 838 % 2 == 0 else 32,
            nvme_slots=2 if 838 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 838 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (838 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 838 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00839(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00839."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00839",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0839",
            chassis_form_factor="Ultrabook 14-inch" if 839 % 3 == 0 else "Workstation 16-inch" if 839 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (839 % 35),
            ram_standard="DDR5-5600" if 839 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 839 % 2 == 0 else 32,
            nvme_slots=2 if 839 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 839 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (839 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 839 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00840(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00840."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00840",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0840",
            chassis_form_factor="Ultrabook 14-inch" if 840 % 3 == 0 else "Workstation 16-inch" if 840 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (840 % 35),
            ram_standard="DDR5-5600" if 840 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 840 % 2 == 0 else 32,
            nvme_slots=2 if 840 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 840 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (840 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 840 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00841(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00841."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00841",
            brand="Dell",
            model_series="Dell Enterprise Series-0841",
            chassis_form_factor="Ultrabook 14-inch" if 841 % 3 == 0 else "Workstation 16-inch" if 841 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (841 % 35),
            ram_standard="DDR5-5600" if 841 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 841 % 2 == 0 else 32,
            nvme_slots=2 if 841 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 841 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (841 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 841 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00842(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00842."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00842",
            brand="HP",
            model_series="HP Enterprise Series-0842",
            chassis_form_factor="Ultrabook 14-inch" if 842 % 3 == 0 else "Workstation 16-inch" if 842 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (842 % 35),
            ram_standard="DDR5-5600" if 842 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 842 % 2 == 0 else 32,
            nvme_slots=2 if 842 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 842 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (842 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 842 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00843(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00843."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00843",
            brand="Apple",
            model_series="Apple Enterprise Series-0843",
            chassis_form_factor="Ultrabook 14-inch" if 843 % 3 == 0 else "Workstation 16-inch" if 843 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (843 % 35),
            ram_standard="DDR5-5600" if 843 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 843 % 2 == 0 else 32,
            nvme_slots=2 if 843 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 843 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (843 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 843 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00844(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00844."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00844",
            brand="Asus",
            model_series="Asus Enterprise Series-0844",
            chassis_form_factor="Ultrabook 14-inch" if 844 % 3 == 0 else "Workstation 16-inch" if 844 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (844 % 35),
            ram_standard="DDR5-5600" if 844 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 844 % 2 == 0 else 32,
            nvme_slots=2 if 844 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 844 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (844 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 844 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00845(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00845."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00845",
            brand="Acer",
            model_series="Acer Enterprise Series-0845",
            chassis_form_factor="Ultrabook 14-inch" if 845 % 3 == 0 else "Workstation 16-inch" if 845 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (845 % 35),
            ram_standard="DDR5-5600" if 845 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 845 % 2 == 0 else 32,
            nvme_slots=2 if 845 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 845 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (845 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 845 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00846(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00846."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00846",
            brand="MSI",
            model_series="MSI Enterprise Series-0846",
            chassis_form_factor="Ultrabook 14-inch" if 846 % 3 == 0 else "Workstation 16-inch" if 846 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (846 % 35),
            ram_standard="DDR5-5600" if 846 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 846 % 2 == 0 else 32,
            nvme_slots=2 if 846 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 846 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (846 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 846 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00847(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00847."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00847",
            brand="Razer",
            model_series="Razer Enterprise Series-0847",
            chassis_form_factor="Ultrabook 14-inch" if 847 % 3 == 0 else "Workstation 16-inch" if 847 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (847 % 35),
            ram_standard="DDR5-5600" if 847 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 847 % 2 == 0 else 32,
            nvme_slots=2 if 847 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 847 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (847 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 847 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00848(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00848."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00848",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0848",
            chassis_form_factor="Ultrabook 14-inch" if 848 % 3 == 0 else "Workstation 16-inch" if 848 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (848 % 35),
            ram_standard="DDR5-5600" if 848 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 848 % 2 == 0 else 32,
            nvme_slots=2 if 848 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 848 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (848 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 848 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00849(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00849."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00849",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0849",
            chassis_form_factor="Ultrabook 14-inch" if 849 % 3 == 0 else "Workstation 16-inch" if 849 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (849 % 35),
            ram_standard="DDR5-5600" if 849 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 849 % 2 == 0 else 32,
            nvme_slots=2 if 849 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 849 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (849 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 849 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00850(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00850."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00850",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0850",
            chassis_form_factor="Ultrabook 14-inch" if 850 % 3 == 0 else "Workstation 16-inch" if 850 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (850 % 35),
            ram_standard="DDR5-5600" if 850 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 850 % 2 == 0 else 32,
            nvme_slots=2 if 850 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 850 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (850 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 850 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00851(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00851."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00851",
            brand="Dell",
            model_series="Dell Enterprise Series-0851",
            chassis_form_factor="Ultrabook 14-inch" if 851 % 3 == 0 else "Workstation 16-inch" if 851 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (851 % 35),
            ram_standard="DDR5-5600" if 851 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 851 % 2 == 0 else 32,
            nvme_slots=2 if 851 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 851 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (851 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 851 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00852(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00852."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00852",
            brand="HP",
            model_series="HP Enterprise Series-0852",
            chassis_form_factor="Ultrabook 14-inch" if 852 % 3 == 0 else "Workstation 16-inch" if 852 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (852 % 35),
            ram_standard="DDR5-5600" if 852 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 852 % 2 == 0 else 32,
            nvme_slots=2 if 852 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 852 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (852 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 852 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00853(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00853."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00853",
            brand="Apple",
            model_series="Apple Enterprise Series-0853",
            chassis_form_factor="Ultrabook 14-inch" if 853 % 3 == 0 else "Workstation 16-inch" if 853 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (853 % 35),
            ram_standard="DDR5-5600" if 853 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 853 % 2 == 0 else 32,
            nvme_slots=2 if 853 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 853 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (853 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 853 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00854(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00854."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00854",
            brand="Asus",
            model_series="Asus Enterprise Series-0854",
            chassis_form_factor="Ultrabook 14-inch" if 854 % 3 == 0 else "Workstation 16-inch" if 854 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (854 % 35),
            ram_standard="DDR5-5600" if 854 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 854 % 2 == 0 else 32,
            nvme_slots=2 if 854 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 854 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (854 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 854 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00855(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00855."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00855",
            brand="Acer",
            model_series="Acer Enterprise Series-0855",
            chassis_form_factor="Ultrabook 14-inch" if 855 % 3 == 0 else "Workstation 16-inch" if 855 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (855 % 35),
            ram_standard="DDR5-5600" if 855 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 855 % 2 == 0 else 32,
            nvme_slots=2 if 855 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 855 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (855 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 855 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00856(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00856."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00856",
            brand="MSI",
            model_series="MSI Enterprise Series-0856",
            chassis_form_factor="Ultrabook 14-inch" if 856 % 3 == 0 else "Workstation 16-inch" if 856 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (856 % 35),
            ram_standard="DDR5-5600" if 856 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 856 % 2 == 0 else 32,
            nvme_slots=2 if 856 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 856 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (856 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 856 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00857(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00857."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00857",
            brand="Razer",
            model_series="Razer Enterprise Series-0857",
            chassis_form_factor="Ultrabook 14-inch" if 857 % 3 == 0 else "Workstation 16-inch" if 857 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (857 % 35),
            ram_standard="DDR5-5600" if 857 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 857 % 2 == 0 else 32,
            nvme_slots=2 if 857 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 857 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (857 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 857 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00858(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00858."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00858",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0858",
            chassis_form_factor="Ultrabook 14-inch" if 858 % 3 == 0 else "Workstation 16-inch" if 858 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (858 % 35),
            ram_standard="DDR5-5600" if 858 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 858 % 2 == 0 else 32,
            nvme_slots=2 if 858 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 858 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (858 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 858 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00859(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00859."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00859",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0859",
            chassis_form_factor="Ultrabook 14-inch" if 859 % 3 == 0 else "Workstation 16-inch" if 859 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (859 % 35),
            ram_standard="DDR5-5600" if 859 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 859 % 2 == 0 else 32,
            nvme_slots=2 if 859 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 859 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (859 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 859 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00860(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00860."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00860",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0860",
            chassis_form_factor="Ultrabook 14-inch" if 860 % 3 == 0 else "Workstation 16-inch" if 860 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (860 % 35),
            ram_standard="DDR5-5600" if 860 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 860 % 2 == 0 else 32,
            nvme_slots=2 if 860 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 860 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (860 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 860 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00861(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00861."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00861",
            brand="Dell",
            model_series="Dell Enterprise Series-0861",
            chassis_form_factor="Ultrabook 14-inch" if 861 % 3 == 0 else "Workstation 16-inch" if 861 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (861 % 35),
            ram_standard="DDR5-5600" if 861 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 861 % 2 == 0 else 32,
            nvme_slots=2 if 861 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 861 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (861 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 861 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00862(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00862."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00862",
            brand="HP",
            model_series="HP Enterprise Series-0862",
            chassis_form_factor="Ultrabook 14-inch" if 862 % 3 == 0 else "Workstation 16-inch" if 862 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (862 % 35),
            ram_standard="DDR5-5600" if 862 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 862 % 2 == 0 else 32,
            nvme_slots=2 if 862 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 862 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (862 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 862 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00863(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00863."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00863",
            brand="Apple",
            model_series="Apple Enterprise Series-0863",
            chassis_form_factor="Ultrabook 14-inch" if 863 % 3 == 0 else "Workstation 16-inch" if 863 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (863 % 35),
            ram_standard="DDR5-5600" if 863 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 863 % 2 == 0 else 32,
            nvme_slots=2 if 863 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 863 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (863 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 863 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00864(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00864."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00864",
            brand="Asus",
            model_series="Asus Enterprise Series-0864",
            chassis_form_factor="Ultrabook 14-inch" if 864 % 3 == 0 else "Workstation 16-inch" if 864 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (864 % 35),
            ram_standard="DDR5-5600" if 864 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 864 % 2 == 0 else 32,
            nvme_slots=2 if 864 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 864 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (864 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 864 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00865(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00865."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00865",
            brand="Acer",
            model_series="Acer Enterprise Series-0865",
            chassis_form_factor="Ultrabook 14-inch" if 865 % 3 == 0 else "Workstation 16-inch" if 865 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (865 % 35),
            ram_standard="DDR5-5600" if 865 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 865 % 2 == 0 else 32,
            nvme_slots=2 if 865 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 865 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (865 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 865 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00866(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00866."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00866",
            brand="MSI",
            model_series="MSI Enterprise Series-0866",
            chassis_form_factor="Ultrabook 14-inch" if 866 % 3 == 0 else "Workstation 16-inch" if 866 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (866 % 35),
            ram_standard="DDR5-5600" if 866 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 866 % 2 == 0 else 32,
            nvme_slots=2 if 866 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 866 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (866 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 866 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00867(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00867."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00867",
            brand="Razer",
            model_series="Razer Enterprise Series-0867",
            chassis_form_factor="Ultrabook 14-inch" if 867 % 3 == 0 else "Workstation 16-inch" if 867 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (867 % 35),
            ram_standard="DDR5-5600" if 867 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 867 % 2 == 0 else 32,
            nvme_slots=2 if 867 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 867 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (867 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 867 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00868(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00868."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00868",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0868",
            chassis_form_factor="Ultrabook 14-inch" if 868 % 3 == 0 else "Workstation 16-inch" if 868 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (868 % 35),
            ram_standard="DDR5-5600" if 868 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 868 % 2 == 0 else 32,
            nvme_slots=2 if 868 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 868 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (868 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 868 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00869(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00869."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00869",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0869",
            chassis_form_factor="Ultrabook 14-inch" if 869 % 3 == 0 else "Workstation 16-inch" if 869 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (869 % 35),
            ram_standard="DDR5-5600" if 869 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 869 % 2 == 0 else 32,
            nvme_slots=2 if 869 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 869 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (869 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 869 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00870(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00870."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00870",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0870",
            chassis_form_factor="Ultrabook 14-inch" if 870 % 3 == 0 else "Workstation 16-inch" if 870 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (870 % 35),
            ram_standard="DDR5-5600" if 870 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 870 % 2 == 0 else 32,
            nvme_slots=2 if 870 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 870 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (870 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 870 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00871(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00871."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00871",
            brand="Dell",
            model_series="Dell Enterprise Series-0871",
            chassis_form_factor="Ultrabook 14-inch" if 871 % 3 == 0 else "Workstation 16-inch" if 871 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (871 % 35),
            ram_standard="DDR5-5600" if 871 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 871 % 2 == 0 else 32,
            nvme_slots=2 if 871 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 871 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (871 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 871 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00872(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00872."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00872",
            brand="HP",
            model_series="HP Enterprise Series-0872",
            chassis_form_factor="Ultrabook 14-inch" if 872 % 3 == 0 else "Workstation 16-inch" if 872 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (872 % 35),
            ram_standard="DDR5-5600" if 872 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 872 % 2 == 0 else 32,
            nvme_slots=2 if 872 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 872 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (872 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 872 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00873(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00873."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00873",
            brand="Apple",
            model_series="Apple Enterprise Series-0873",
            chassis_form_factor="Ultrabook 14-inch" if 873 % 3 == 0 else "Workstation 16-inch" if 873 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (873 % 35),
            ram_standard="DDR5-5600" if 873 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 873 % 2 == 0 else 32,
            nvme_slots=2 if 873 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 873 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (873 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 873 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00874(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00874."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00874",
            brand="Asus",
            model_series="Asus Enterprise Series-0874",
            chassis_form_factor="Ultrabook 14-inch" if 874 % 3 == 0 else "Workstation 16-inch" if 874 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (874 % 35),
            ram_standard="DDR5-5600" if 874 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 874 % 2 == 0 else 32,
            nvme_slots=2 if 874 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 874 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (874 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 874 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00875(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00875."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00875",
            brand="Acer",
            model_series="Acer Enterprise Series-0875",
            chassis_form_factor="Ultrabook 14-inch" if 875 % 3 == 0 else "Workstation 16-inch" if 875 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (875 % 35),
            ram_standard="DDR5-5600" if 875 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 875 % 2 == 0 else 32,
            nvme_slots=2 if 875 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 875 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (875 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 875 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00876(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00876."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00876",
            brand="MSI",
            model_series="MSI Enterprise Series-0876",
            chassis_form_factor="Ultrabook 14-inch" if 876 % 3 == 0 else "Workstation 16-inch" if 876 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (876 % 35),
            ram_standard="DDR5-5600" if 876 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 876 % 2 == 0 else 32,
            nvme_slots=2 if 876 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 876 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (876 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 876 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00877(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00877."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00877",
            brand="Razer",
            model_series="Razer Enterprise Series-0877",
            chassis_form_factor="Ultrabook 14-inch" if 877 % 3 == 0 else "Workstation 16-inch" if 877 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (877 % 35),
            ram_standard="DDR5-5600" if 877 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 877 % 2 == 0 else 32,
            nvme_slots=2 if 877 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 877 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (877 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 877 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00878(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00878."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00878",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0878",
            chassis_form_factor="Ultrabook 14-inch" if 878 % 3 == 0 else "Workstation 16-inch" if 878 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (878 % 35),
            ram_standard="DDR5-5600" if 878 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 878 % 2 == 0 else 32,
            nvme_slots=2 if 878 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 878 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (878 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 878 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00879(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00879."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00879",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0879",
            chassis_form_factor="Ultrabook 14-inch" if 879 % 3 == 0 else "Workstation 16-inch" if 879 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (879 % 35),
            ram_standard="DDR5-5600" if 879 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 879 % 2 == 0 else 32,
            nvme_slots=2 if 879 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 879 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (879 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 879 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00880(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00880."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00880",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0880",
            chassis_form_factor="Ultrabook 14-inch" if 880 % 3 == 0 else "Workstation 16-inch" if 880 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (880 % 35),
            ram_standard="DDR5-5600" if 880 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 880 % 2 == 0 else 32,
            nvme_slots=2 if 880 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 880 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (880 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 880 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00881(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00881."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00881",
            brand="Dell",
            model_series="Dell Enterprise Series-0881",
            chassis_form_factor="Ultrabook 14-inch" if 881 % 3 == 0 else "Workstation 16-inch" if 881 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (881 % 35),
            ram_standard="DDR5-5600" if 881 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 881 % 2 == 0 else 32,
            nvme_slots=2 if 881 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 881 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (881 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 881 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00882(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00882."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00882",
            brand="HP",
            model_series="HP Enterprise Series-0882",
            chassis_form_factor="Ultrabook 14-inch" if 882 % 3 == 0 else "Workstation 16-inch" if 882 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (882 % 35),
            ram_standard="DDR5-5600" if 882 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 882 % 2 == 0 else 32,
            nvme_slots=2 if 882 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 882 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (882 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 882 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00883(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00883."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00883",
            brand="Apple",
            model_series="Apple Enterprise Series-0883",
            chassis_form_factor="Ultrabook 14-inch" if 883 % 3 == 0 else "Workstation 16-inch" if 883 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (883 % 35),
            ram_standard="DDR5-5600" if 883 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 883 % 2 == 0 else 32,
            nvme_slots=2 if 883 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 883 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (883 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 883 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00884(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00884."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00884",
            brand="Asus",
            model_series="Asus Enterprise Series-0884",
            chassis_form_factor="Ultrabook 14-inch" if 884 % 3 == 0 else "Workstation 16-inch" if 884 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (884 % 35),
            ram_standard="DDR5-5600" if 884 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 884 % 2 == 0 else 32,
            nvme_slots=2 if 884 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 884 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (884 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 884 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00885(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00885."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00885",
            brand="Acer",
            model_series="Acer Enterprise Series-0885",
            chassis_form_factor="Ultrabook 14-inch" if 885 % 3 == 0 else "Workstation 16-inch" if 885 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (885 % 35),
            ram_standard="DDR5-5600" if 885 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 885 % 2 == 0 else 32,
            nvme_slots=2 if 885 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 885 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (885 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 885 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00886(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00886."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00886",
            brand="MSI",
            model_series="MSI Enterprise Series-0886",
            chassis_form_factor="Ultrabook 14-inch" if 886 % 3 == 0 else "Workstation 16-inch" if 886 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (886 % 35),
            ram_standard="DDR5-5600" if 886 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 886 % 2 == 0 else 32,
            nvme_slots=2 if 886 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 886 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (886 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 886 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00887(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00887."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00887",
            brand="Razer",
            model_series="Razer Enterprise Series-0887",
            chassis_form_factor="Ultrabook 14-inch" if 887 % 3 == 0 else "Workstation 16-inch" if 887 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (887 % 35),
            ram_standard="DDR5-5600" if 887 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 887 % 2 == 0 else 32,
            nvme_slots=2 if 887 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 887 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (887 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 887 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00888(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00888."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00888",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0888",
            chassis_form_factor="Ultrabook 14-inch" if 888 % 3 == 0 else "Workstation 16-inch" if 888 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (888 % 35),
            ram_standard="DDR5-5600" if 888 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 888 % 2 == 0 else 32,
            nvme_slots=2 if 888 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 888 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (888 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 888 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00889(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00889."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00889",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0889",
            chassis_form_factor="Ultrabook 14-inch" if 889 % 3 == 0 else "Workstation 16-inch" if 889 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (889 % 35),
            ram_standard="DDR5-5600" if 889 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 889 % 2 == 0 else 32,
            nvme_slots=2 if 889 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 889 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (889 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 889 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00890(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00890."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00890",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0890",
            chassis_form_factor="Ultrabook 14-inch" if 890 % 3 == 0 else "Workstation 16-inch" if 890 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (890 % 35),
            ram_standard="DDR5-5600" if 890 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 890 % 2 == 0 else 32,
            nvme_slots=2 if 890 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 890 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (890 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 890 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00891(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00891."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00891",
            brand="Dell",
            model_series="Dell Enterprise Series-0891",
            chassis_form_factor="Ultrabook 14-inch" if 891 % 3 == 0 else "Workstation 16-inch" if 891 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (891 % 35),
            ram_standard="DDR5-5600" if 891 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 891 % 2 == 0 else 32,
            nvme_slots=2 if 891 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 891 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (891 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 891 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00892(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00892."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00892",
            brand="HP",
            model_series="HP Enterprise Series-0892",
            chassis_form_factor="Ultrabook 14-inch" if 892 % 3 == 0 else "Workstation 16-inch" if 892 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (892 % 35),
            ram_standard="DDR5-5600" if 892 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 892 % 2 == 0 else 32,
            nvme_slots=2 if 892 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 892 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (892 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 892 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00893(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00893."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00893",
            brand="Apple",
            model_series="Apple Enterprise Series-0893",
            chassis_form_factor="Ultrabook 14-inch" if 893 % 3 == 0 else "Workstation 16-inch" if 893 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (893 % 35),
            ram_standard="DDR5-5600" if 893 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 893 % 2 == 0 else 32,
            nvme_slots=2 if 893 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 893 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (893 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 893 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00894(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00894."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00894",
            brand="Asus",
            model_series="Asus Enterprise Series-0894",
            chassis_form_factor="Ultrabook 14-inch" if 894 % 3 == 0 else "Workstation 16-inch" if 894 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (894 % 35),
            ram_standard="DDR5-5600" if 894 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 894 % 2 == 0 else 32,
            nvme_slots=2 if 894 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 894 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (894 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 894 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00895(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00895."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00895",
            brand="Acer",
            model_series="Acer Enterprise Series-0895",
            chassis_form_factor="Ultrabook 14-inch" if 895 % 3 == 0 else "Workstation 16-inch" if 895 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (895 % 35),
            ram_standard="DDR5-5600" if 895 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 895 % 2 == 0 else 32,
            nvme_slots=2 if 895 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 895 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (895 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 895 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00896(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00896."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00896",
            brand="MSI",
            model_series="MSI Enterprise Series-0896",
            chassis_form_factor="Ultrabook 14-inch" if 896 % 3 == 0 else "Workstation 16-inch" if 896 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (896 % 35),
            ram_standard="DDR5-5600" if 896 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 896 % 2 == 0 else 32,
            nvme_slots=2 if 896 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 896 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (896 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 896 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00897(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00897."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00897",
            brand="Razer",
            model_series="Razer Enterprise Series-0897",
            chassis_form_factor="Ultrabook 14-inch" if 897 % 3 == 0 else "Workstation 16-inch" if 897 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (897 % 35),
            ram_standard="DDR5-5600" if 897 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 897 % 2 == 0 else 32,
            nvme_slots=2 if 897 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 897 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (897 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 897 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00898(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00898."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00898",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0898",
            chassis_form_factor="Ultrabook 14-inch" if 898 % 3 == 0 else "Workstation 16-inch" if 898 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (898 % 35),
            ram_standard="DDR5-5600" if 898 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 898 % 2 == 0 else 32,
            nvme_slots=2 if 898 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 898 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (898 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 898 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00899(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00899."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00899",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0899",
            chassis_form_factor="Ultrabook 14-inch" if 899 % 3 == 0 else "Workstation 16-inch" if 899 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (899 % 35),
            ram_standard="DDR5-5600" if 899 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 899 % 2 == 0 else 32,
            nvme_slots=2 if 899 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 899 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (899 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 899 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00900(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00900."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00900",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0900",
            chassis_form_factor="Ultrabook 14-inch" if 900 % 3 == 0 else "Workstation 16-inch" if 900 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (900 % 35),
            ram_standard="DDR5-5600" if 900 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 900 % 2 == 0 else 32,
            nvme_slots=2 if 900 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 900 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (900 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 900 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00901(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00901."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00901",
            brand="Dell",
            model_series="Dell Enterprise Series-0901",
            chassis_form_factor="Ultrabook 14-inch" if 901 % 3 == 0 else "Workstation 16-inch" if 901 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (901 % 35),
            ram_standard="DDR5-5600" if 901 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 901 % 2 == 0 else 32,
            nvme_slots=2 if 901 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 901 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (901 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 901 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00902(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00902."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00902",
            brand="HP",
            model_series="HP Enterprise Series-0902",
            chassis_form_factor="Ultrabook 14-inch" if 902 % 3 == 0 else "Workstation 16-inch" if 902 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (902 % 35),
            ram_standard="DDR5-5600" if 902 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 902 % 2 == 0 else 32,
            nvme_slots=2 if 902 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 902 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (902 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 902 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00903(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00903."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00903",
            brand="Apple",
            model_series="Apple Enterprise Series-0903",
            chassis_form_factor="Ultrabook 14-inch" if 903 % 3 == 0 else "Workstation 16-inch" if 903 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (903 % 35),
            ram_standard="DDR5-5600" if 903 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 903 % 2 == 0 else 32,
            nvme_slots=2 if 903 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 903 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (903 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 903 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00904(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00904."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00904",
            brand="Asus",
            model_series="Asus Enterprise Series-0904",
            chassis_form_factor="Ultrabook 14-inch" if 904 % 3 == 0 else "Workstation 16-inch" if 904 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (904 % 35),
            ram_standard="DDR5-5600" if 904 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 904 % 2 == 0 else 32,
            nvme_slots=2 if 904 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 904 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (904 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 904 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00905(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00905."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00905",
            brand="Acer",
            model_series="Acer Enterprise Series-0905",
            chassis_form_factor="Ultrabook 14-inch" if 905 % 3 == 0 else "Workstation 16-inch" if 905 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (905 % 35),
            ram_standard="DDR5-5600" if 905 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 905 % 2 == 0 else 32,
            nvme_slots=2 if 905 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 905 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (905 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 905 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00906(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00906."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00906",
            brand="MSI",
            model_series="MSI Enterprise Series-0906",
            chassis_form_factor="Ultrabook 14-inch" if 906 % 3 == 0 else "Workstation 16-inch" if 906 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (906 % 35),
            ram_standard="DDR5-5600" if 906 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 906 % 2 == 0 else 32,
            nvme_slots=2 if 906 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 906 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (906 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 906 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00907(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00907."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00907",
            brand="Razer",
            model_series="Razer Enterprise Series-0907",
            chassis_form_factor="Ultrabook 14-inch" if 907 % 3 == 0 else "Workstation 16-inch" if 907 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (907 % 35),
            ram_standard="DDR5-5600" if 907 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 907 % 2 == 0 else 32,
            nvme_slots=2 if 907 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 907 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (907 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 907 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00908(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00908."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00908",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0908",
            chassis_form_factor="Ultrabook 14-inch" if 908 % 3 == 0 else "Workstation 16-inch" if 908 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (908 % 35),
            ram_standard="DDR5-5600" if 908 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 908 % 2 == 0 else 32,
            nvme_slots=2 if 908 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 908 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (908 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 908 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00909(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00909."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00909",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0909",
            chassis_form_factor="Ultrabook 14-inch" if 909 % 3 == 0 else "Workstation 16-inch" if 909 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (909 % 35),
            ram_standard="DDR5-5600" if 909 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 909 % 2 == 0 else 32,
            nvme_slots=2 if 909 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 909 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (909 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 909 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00910(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00910."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00910",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0910",
            chassis_form_factor="Ultrabook 14-inch" if 910 % 3 == 0 else "Workstation 16-inch" if 910 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (910 % 35),
            ram_standard="DDR5-5600" if 910 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 910 % 2 == 0 else 32,
            nvme_slots=2 if 910 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 910 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (910 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 910 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00911(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00911."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00911",
            brand="Dell",
            model_series="Dell Enterprise Series-0911",
            chassis_form_factor="Ultrabook 14-inch" if 911 % 3 == 0 else "Workstation 16-inch" if 911 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (911 % 35),
            ram_standard="DDR5-5600" if 911 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 911 % 2 == 0 else 32,
            nvme_slots=2 if 911 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 911 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (911 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 911 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00912(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00912."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00912",
            brand="HP",
            model_series="HP Enterprise Series-0912",
            chassis_form_factor="Ultrabook 14-inch" if 912 % 3 == 0 else "Workstation 16-inch" if 912 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (912 % 35),
            ram_standard="DDR5-5600" if 912 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 912 % 2 == 0 else 32,
            nvme_slots=2 if 912 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 912 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (912 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 912 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00913(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00913."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00913",
            brand="Apple",
            model_series="Apple Enterprise Series-0913",
            chassis_form_factor="Ultrabook 14-inch" if 913 % 3 == 0 else "Workstation 16-inch" if 913 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (913 % 35),
            ram_standard="DDR5-5600" if 913 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 913 % 2 == 0 else 32,
            nvme_slots=2 if 913 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 913 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (913 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 913 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00914(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00914."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00914",
            brand="Asus",
            model_series="Asus Enterprise Series-0914",
            chassis_form_factor="Ultrabook 14-inch" if 914 % 3 == 0 else "Workstation 16-inch" if 914 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (914 % 35),
            ram_standard="DDR5-5600" if 914 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 914 % 2 == 0 else 32,
            nvme_slots=2 if 914 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 914 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (914 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 914 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00915(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00915."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00915",
            brand="Acer",
            model_series="Acer Enterprise Series-0915",
            chassis_form_factor="Ultrabook 14-inch" if 915 % 3 == 0 else "Workstation 16-inch" if 915 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (915 % 35),
            ram_standard="DDR5-5600" if 915 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 915 % 2 == 0 else 32,
            nvme_slots=2 if 915 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 915 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (915 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 915 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00916(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00916."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00916",
            brand="MSI",
            model_series="MSI Enterprise Series-0916",
            chassis_form_factor="Ultrabook 14-inch" if 916 % 3 == 0 else "Workstation 16-inch" if 916 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (916 % 35),
            ram_standard="DDR5-5600" if 916 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 916 % 2 == 0 else 32,
            nvme_slots=2 if 916 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 916 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (916 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 916 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00917(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00917."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00917",
            brand="Razer",
            model_series="Razer Enterprise Series-0917",
            chassis_form_factor="Ultrabook 14-inch" if 917 % 3 == 0 else "Workstation 16-inch" if 917 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (917 % 35),
            ram_standard="DDR5-5600" if 917 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 917 % 2 == 0 else 32,
            nvme_slots=2 if 917 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 917 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (917 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 917 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00918(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00918."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00918",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0918",
            chassis_form_factor="Ultrabook 14-inch" if 918 % 3 == 0 else "Workstation 16-inch" if 918 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (918 % 35),
            ram_standard="DDR5-5600" if 918 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 918 % 2 == 0 else 32,
            nvme_slots=2 if 918 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 918 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (918 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 918 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00919(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00919."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00919",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0919",
            chassis_form_factor="Ultrabook 14-inch" if 919 % 3 == 0 else "Workstation 16-inch" if 919 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (919 % 35),
            ram_standard="DDR5-5600" if 919 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 919 % 2 == 0 else 32,
            nvme_slots=2 if 919 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 919 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (919 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 919 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00920(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00920."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00920",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0920",
            chassis_form_factor="Ultrabook 14-inch" if 920 % 3 == 0 else "Workstation 16-inch" if 920 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (920 % 35),
            ram_standard="DDR5-5600" if 920 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 920 % 2 == 0 else 32,
            nvme_slots=2 if 920 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 920 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (920 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 920 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00921(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00921."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00921",
            brand="Dell",
            model_series="Dell Enterprise Series-0921",
            chassis_form_factor="Ultrabook 14-inch" if 921 % 3 == 0 else "Workstation 16-inch" if 921 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (921 % 35),
            ram_standard="DDR5-5600" if 921 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 921 % 2 == 0 else 32,
            nvme_slots=2 if 921 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 921 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (921 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 921 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00922(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00922."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00922",
            brand="HP",
            model_series="HP Enterprise Series-0922",
            chassis_form_factor="Ultrabook 14-inch" if 922 % 3 == 0 else "Workstation 16-inch" if 922 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (922 % 35),
            ram_standard="DDR5-5600" if 922 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 922 % 2 == 0 else 32,
            nvme_slots=2 if 922 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 922 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (922 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 922 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00923(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00923."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00923",
            brand="Apple",
            model_series="Apple Enterprise Series-0923",
            chassis_form_factor="Ultrabook 14-inch" if 923 % 3 == 0 else "Workstation 16-inch" if 923 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (923 % 35),
            ram_standard="DDR5-5600" if 923 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 923 % 2 == 0 else 32,
            nvme_slots=2 if 923 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 923 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (923 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 923 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00924(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00924."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00924",
            brand="Asus",
            model_series="Asus Enterprise Series-0924",
            chassis_form_factor="Ultrabook 14-inch" if 924 % 3 == 0 else "Workstation 16-inch" if 924 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (924 % 35),
            ram_standard="DDR5-5600" if 924 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 924 % 2 == 0 else 32,
            nvme_slots=2 if 924 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 924 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (924 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 924 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00925(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00925."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00925",
            brand="Acer",
            model_series="Acer Enterprise Series-0925",
            chassis_form_factor="Ultrabook 14-inch" if 925 % 3 == 0 else "Workstation 16-inch" if 925 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (925 % 35),
            ram_standard="DDR5-5600" if 925 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 925 % 2 == 0 else 32,
            nvme_slots=2 if 925 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 925 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (925 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 925 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00926(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00926."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00926",
            brand="MSI",
            model_series="MSI Enterprise Series-0926",
            chassis_form_factor="Ultrabook 14-inch" if 926 % 3 == 0 else "Workstation 16-inch" if 926 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (926 % 35),
            ram_standard="DDR5-5600" if 926 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 926 % 2 == 0 else 32,
            nvme_slots=2 if 926 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 926 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (926 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 926 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00927(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00927."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00927",
            brand="Razer",
            model_series="Razer Enterprise Series-0927",
            chassis_form_factor="Ultrabook 14-inch" if 927 % 3 == 0 else "Workstation 16-inch" if 927 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (927 % 35),
            ram_standard="DDR5-5600" if 927 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 927 % 2 == 0 else 32,
            nvme_slots=2 if 927 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 927 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (927 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 927 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00928(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00928."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00928",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0928",
            chassis_form_factor="Ultrabook 14-inch" if 928 % 3 == 0 else "Workstation 16-inch" if 928 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (928 % 35),
            ram_standard="DDR5-5600" if 928 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 928 % 2 == 0 else 32,
            nvme_slots=2 if 928 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 928 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (928 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 928 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00929(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00929."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00929",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0929",
            chassis_form_factor="Ultrabook 14-inch" if 929 % 3 == 0 else "Workstation 16-inch" if 929 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (929 % 35),
            ram_standard="DDR5-5600" if 929 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 929 % 2 == 0 else 32,
            nvme_slots=2 if 929 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 929 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (929 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 929 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00930(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00930."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00930",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0930",
            chassis_form_factor="Ultrabook 14-inch" if 930 % 3 == 0 else "Workstation 16-inch" if 930 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (930 % 35),
            ram_standard="DDR5-5600" if 930 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 930 % 2 == 0 else 32,
            nvme_slots=2 if 930 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 930 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (930 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 930 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00931(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00931."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00931",
            brand="Dell",
            model_series="Dell Enterprise Series-0931",
            chassis_form_factor="Ultrabook 14-inch" if 931 % 3 == 0 else "Workstation 16-inch" if 931 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (931 % 35),
            ram_standard="DDR5-5600" if 931 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 931 % 2 == 0 else 32,
            nvme_slots=2 if 931 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 931 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (931 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 931 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00932(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00932."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00932",
            brand="HP",
            model_series="HP Enterprise Series-0932",
            chassis_form_factor="Ultrabook 14-inch" if 932 % 3 == 0 else "Workstation 16-inch" if 932 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (932 % 35),
            ram_standard="DDR5-5600" if 932 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 932 % 2 == 0 else 32,
            nvme_slots=2 if 932 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 932 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (932 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 932 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00933(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00933."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00933",
            brand="Apple",
            model_series="Apple Enterprise Series-0933",
            chassis_form_factor="Ultrabook 14-inch" if 933 % 3 == 0 else "Workstation 16-inch" if 933 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (933 % 35),
            ram_standard="DDR5-5600" if 933 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 933 % 2 == 0 else 32,
            nvme_slots=2 if 933 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 933 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (933 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 933 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00934(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00934."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00934",
            brand="Asus",
            model_series="Asus Enterprise Series-0934",
            chassis_form_factor="Ultrabook 14-inch" if 934 % 3 == 0 else "Workstation 16-inch" if 934 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (934 % 35),
            ram_standard="DDR5-5600" if 934 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 934 % 2 == 0 else 32,
            nvme_slots=2 if 934 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 934 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (934 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 934 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00935(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00935."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00935",
            brand="Acer",
            model_series="Acer Enterprise Series-0935",
            chassis_form_factor="Ultrabook 14-inch" if 935 % 3 == 0 else "Workstation 16-inch" if 935 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (935 % 35),
            ram_standard="DDR5-5600" if 935 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 935 % 2 == 0 else 32,
            nvme_slots=2 if 935 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 935 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (935 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 935 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00936(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00936."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00936",
            brand="MSI",
            model_series="MSI Enterprise Series-0936",
            chassis_form_factor="Ultrabook 14-inch" if 936 % 3 == 0 else "Workstation 16-inch" if 936 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (936 % 35),
            ram_standard="DDR5-5600" if 936 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 936 % 2 == 0 else 32,
            nvme_slots=2 if 936 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 936 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (936 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 936 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00937(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00937."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00937",
            brand="Razer",
            model_series="Razer Enterprise Series-0937",
            chassis_form_factor="Ultrabook 14-inch" if 937 % 3 == 0 else "Workstation 16-inch" if 937 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (937 % 35),
            ram_standard="DDR5-5600" if 937 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 937 % 2 == 0 else 32,
            nvme_slots=2 if 937 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 937 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (937 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 937 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00938(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00938."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00938",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0938",
            chassis_form_factor="Ultrabook 14-inch" if 938 % 3 == 0 else "Workstation 16-inch" if 938 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (938 % 35),
            ram_standard="DDR5-5600" if 938 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 938 % 2 == 0 else 32,
            nvme_slots=2 if 938 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 938 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (938 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 938 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00939(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00939."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00939",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0939",
            chassis_form_factor="Ultrabook 14-inch" if 939 % 3 == 0 else "Workstation 16-inch" if 939 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (939 % 35),
            ram_standard="DDR5-5600" if 939 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 939 % 2 == 0 else 32,
            nvme_slots=2 if 939 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 939 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (939 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 939 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00940(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00940."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00940",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0940",
            chassis_form_factor="Ultrabook 14-inch" if 940 % 3 == 0 else "Workstation 16-inch" if 940 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (940 % 35),
            ram_standard="DDR5-5600" if 940 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 940 % 2 == 0 else 32,
            nvme_slots=2 if 940 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 940 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (940 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 940 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00941(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00941."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00941",
            brand="Dell",
            model_series="Dell Enterprise Series-0941",
            chassis_form_factor="Ultrabook 14-inch" if 941 % 3 == 0 else "Workstation 16-inch" if 941 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (941 % 35),
            ram_standard="DDR5-5600" if 941 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 941 % 2 == 0 else 32,
            nvme_slots=2 if 941 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 941 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (941 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 941 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00942(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00942."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00942",
            brand="HP",
            model_series="HP Enterprise Series-0942",
            chassis_form_factor="Ultrabook 14-inch" if 942 % 3 == 0 else "Workstation 16-inch" if 942 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (942 % 35),
            ram_standard="DDR5-5600" if 942 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 942 % 2 == 0 else 32,
            nvme_slots=2 if 942 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 942 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (942 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 942 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00943(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00943."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00943",
            brand="Apple",
            model_series="Apple Enterprise Series-0943",
            chassis_form_factor="Ultrabook 14-inch" if 943 % 3 == 0 else "Workstation 16-inch" if 943 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (943 % 35),
            ram_standard="DDR5-5600" if 943 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 943 % 2 == 0 else 32,
            nvme_slots=2 if 943 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 943 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (943 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 943 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00944(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00944."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00944",
            brand="Asus",
            model_series="Asus Enterprise Series-0944",
            chassis_form_factor="Ultrabook 14-inch" if 944 % 3 == 0 else "Workstation 16-inch" if 944 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (944 % 35),
            ram_standard="DDR5-5600" if 944 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 944 % 2 == 0 else 32,
            nvme_slots=2 if 944 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 944 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (944 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 944 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00945(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00945."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00945",
            brand="Acer",
            model_series="Acer Enterprise Series-0945",
            chassis_form_factor="Ultrabook 14-inch" if 945 % 3 == 0 else "Workstation 16-inch" if 945 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (945 % 35),
            ram_standard="DDR5-5600" if 945 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 945 % 2 == 0 else 32,
            nvme_slots=2 if 945 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 945 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (945 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 945 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00946(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00946."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00946",
            brand="MSI",
            model_series="MSI Enterprise Series-0946",
            chassis_form_factor="Ultrabook 14-inch" if 946 % 3 == 0 else "Workstation 16-inch" if 946 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (946 % 35),
            ram_standard="DDR5-5600" if 946 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 946 % 2 == 0 else 32,
            nvme_slots=2 if 946 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 946 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (946 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 946 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00947(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00947."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00947",
            brand="Razer",
            model_series="Razer Enterprise Series-0947",
            chassis_form_factor="Ultrabook 14-inch" if 947 % 3 == 0 else "Workstation 16-inch" if 947 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (947 % 35),
            ram_standard="DDR5-5600" if 947 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 947 % 2 == 0 else 32,
            nvme_slots=2 if 947 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 947 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (947 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 947 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00948(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00948."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00948",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0948",
            chassis_form_factor="Ultrabook 14-inch" if 948 % 3 == 0 else "Workstation 16-inch" if 948 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (948 % 35),
            ram_standard="DDR5-5600" if 948 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 948 % 2 == 0 else 32,
            nvme_slots=2 if 948 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 948 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (948 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 948 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00949(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00949."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00949",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0949",
            chassis_form_factor="Ultrabook 14-inch" if 949 % 3 == 0 else "Workstation 16-inch" if 949 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (949 % 35),
            ram_standard="DDR5-5600" if 949 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 949 % 2 == 0 else 32,
            nvme_slots=2 if 949 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 949 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (949 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 949 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00950(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00950."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00950",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0950",
            chassis_form_factor="Ultrabook 14-inch" if 950 % 3 == 0 else "Workstation 16-inch" if 950 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (950 % 35),
            ram_standard="DDR5-5600" if 950 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 950 % 2 == 0 else 32,
            nvme_slots=2 if 950 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 950 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (950 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 950 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00951(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00951."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00951",
            brand="Dell",
            model_series="Dell Enterprise Series-0951",
            chassis_form_factor="Ultrabook 14-inch" if 951 % 3 == 0 else "Workstation 16-inch" if 951 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (951 % 35),
            ram_standard="DDR5-5600" if 951 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 951 % 2 == 0 else 32,
            nvme_slots=2 if 951 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 951 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (951 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 951 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00952(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00952."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00952",
            brand="HP",
            model_series="HP Enterprise Series-0952",
            chassis_form_factor="Ultrabook 14-inch" if 952 % 3 == 0 else "Workstation 16-inch" if 952 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (952 % 35),
            ram_standard="DDR5-5600" if 952 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 952 % 2 == 0 else 32,
            nvme_slots=2 if 952 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 952 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (952 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 952 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00953(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00953."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00953",
            brand="Apple",
            model_series="Apple Enterprise Series-0953",
            chassis_form_factor="Ultrabook 14-inch" if 953 % 3 == 0 else "Workstation 16-inch" if 953 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (953 % 35),
            ram_standard="DDR5-5600" if 953 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 953 % 2 == 0 else 32,
            nvme_slots=2 if 953 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 953 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (953 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 953 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00954(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00954."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00954",
            brand="Asus",
            model_series="Asus Enterprise Series-0954",
            chassis_form_factor="Ultrabook 14-inch" if 954 % 3 == 0 else "Workstation 16-inch" if 954 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (954 % 35),
            ram_standard="DDR5-5600" if 954 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 954 % 2 == 0 else 32,
            nvme_slots=2 if 954 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 954 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (954 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 954 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00955(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00955."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00955",
            brand="Acer",
            model_series="Acer Enterprise Series-0955",
            chassis_form_factor="Ultrabook 14-inch" if 955 % 3 == 0 else "Workstation 16-inch" if 955 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (955 % 35),
            ram_standard="DDR5-5600" if 955 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 955 % 2 == 0 else 32,
            nvme_slots=2 if 955 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 955 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (955 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 955 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00956(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00956."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00956",
            brand="MSI",
            model_series="MSI Enterprise Series-0956",
            chassis_form_factor="Ultrabook 14-inch" if 956 % 3 == 0 else "Workstation 16-inch" if 956 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (956 % 35),
            ram_standard="DDR5-5600" if 956 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 956 % 2 == 0 else 32,
            nvme_slots=2 if 956 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 956 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (956 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 956 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00957(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00957."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00957",
            brand="Razer",
            model_series="Razer Enterprise Series-0957",
            chassis_form_factor="Ultrabook 14-inch" if 957 % 3 == 0 else "Workstation 16-inch" if 957 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (957 % 35),
            ram_standard="DDR5-5600" if 957 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 957 % 2 == 0 else 32,
            nvme_slots=2 if 957 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 957 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (957 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 957 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00958(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00958."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00958",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0958",
            chassis_form_factor="Ultrabook 14-inch" if 958 % 3 == 0 else "Workstation 16-inch" if 958 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (958 % 35),
            ram_standard="DDR5-5600" if 958 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 958 % 2 == 0 else 32,
            nvme_slots=2 if 958 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 958 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (958 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 958 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00959(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00959."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00959",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0959",
            chassis_form_factor="Ultrabook 14-inch" if 959 % 3 == 0 else "Workstation 16-inch" if 959 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (959 % 35),
            ram_standard="DDR5-5600" if 959 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 959 % 2 == 0 else 32,
            nvme_slots=2 if 959 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 959 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (959 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 959 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00960(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00960."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00960",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0960",
            chassis_form_factor="Ultrabook 14-inch" if 960 % 3 == 0 else "Workstation 16-inch" if 960 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (960 % 35),
            ram_standard="DDR5-5600" if 960 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 960 % 2 == 0 else 32,
            nvme_slots=2 if 960 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 960 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (960 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 960 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00961(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00961."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00961",
            brand="Dell",
            model_series="Dell Enterprise Series-0961",
            chassis_form_factor="Ultrabook 14-inch" if 961 % 3 == 0 else "Workstation 16-inch" if 961 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (961 % 35),
            ram_standard="DDR5-5600" if 961 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 961 % 2 == 0 else 32,
            nvme_slots=2 if 961 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 961 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (961 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 961 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00962(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00962."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00962",
            brand="HP",
            model_series="HP Enterprise Series-0962",
            chassis_form_factor="Ultrabook 14-inch" if 962 % 3 == 0 else "Workstation 16-inch" if 962 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (962 % 35),
            ram_standard="DDR5-5600" if 962 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 962 % 2 == 0 else 32,
            nvme_slots=2 if 962 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 962 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (962 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 962 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00963(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00963."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00963",
            brand="Apple",
            model_series="Apple Enterprise Series-0963",
            chassis_form_factor="Ultrabook 14-inch" if 963 % 3 == 0 else "Workstation 16-inch" if 963 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (963 % 35),
            ram_standard="DDR5-5600" if 963 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 963 % 2 == 0 else 32,
            nvme_slots=2 if 963 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 963 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (963 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 963 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00964(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00964."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00964",
            brand="Asus",
            model_series="Asus Enterprise Series-0964",
            chassis_form_factor="Ultrabook 14-inch" if 964 % 3 == 0 else "Workstation 16-inch" if 964 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (964 % 35),
            ram_standard="DDR5-5600" if 964 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 964 % 2 == 0 else 32,
            nvme_slots=2 if 964 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 964 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (964 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 964 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00965(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00965."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00965",
            brand="Acer",
            model_series="Acer Enterprise Series-0965",
            chassis_form_factor="Ultrabook 14-inch" if 965 % 3 == 0 else "Workstation 16-inch" if 965 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (965 % 35),
            ram_standard="DDR5-5600" if 965 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 965 % 2 == 0 else 32,
            nvme_slots=2 if 965 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 965 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (965 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 965 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00966(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00966."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00966",
            brand="MSI",
            model_series="MSI Enterprise Series-0966",
            chassis_form_factor="Ultrabook 14-inch" if 966 % 3 == 0 else "Workstation 16-inch" if 966 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (966 % 35),
            ram_standard="DDR5-5600" if 966 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 966 % 2 == 0 else 32,
            nvme_slots=2 if 966 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 966 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (966 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 966 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00967(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00967."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00967",
            brand="Razer",
            model_series="Razer Enterprise Series-0967",
            chassis_form_factor="Ultrabook 14-inch" if 967 % 3 == 0 else "Workstation 16-inch" if 967 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (967 % 35),
            ram_standard="DDR5-5600" if 967 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 967 % 2 == 0 else 32,
            nvme_slots=2 if 967 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 967 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (967 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 967 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00968(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00968."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00968",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0968",
            chassis_form_factor="Ultrabook 14-inch" if 968 % 3 == 0 else "Workstation 16-inch" if 968 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (968 % 35),
            ram_standard="DDR5-5600" if 968 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 968 % 2 == 0 else 32,
            nvme_slots=2 if 968 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 968 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (968 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 968 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00969(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00969."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00969",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0969",
            chassis_form_factor="Ultrabook 14-inch" if 969 % 3 == 0 else "Workstation 16-inch" if 969 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (969 % 35),
            ram_standard="DDR5-5600" if 969 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 969 % 2 == 0 else 32,
            nvme_slots=2 if 969 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 969 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (969 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 969 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00970(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00970."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00970",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0970",
            chassis_form_factor="Ultrabook 14-inch" if 970 % 3 == 0 else "Workstation 16-inch" if 970 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (970 % 35),
            ram_standard="DDR5-5600" if 970 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 970 % 2 == 0 else 32,
            nvme_slots=2 if 970 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 970 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (970 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 970 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00971(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00971."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00971",
            brand="Dell",
            model_series="Dell Enterprise Series-0971",
            chassis_form_factor="Ultrabook 14-inch" if 971 % 3 == 0 else "Workstation 16-inch" if 971 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (971 % 35),
            ram_standard="DDR5-5600" if 971 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 971 % 2 == 0 else 32,
            nvme_slots=2 if 971 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 971 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (971 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 971 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00972(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00972."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00972",
            brand="HP",
            model_series="HP Enterprise Series-0972",
            chassis_form_factor="Ultrabook 14-inch" if 972 % 3 == 0 else "Workstation 16-inch" if 972 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (972 % 35),
            ram_standard="DDR5-5600" if 972 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 972 % 2 == 0 else 32,
            nvme_slots=2 if 972 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 972 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (972 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 972 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00973(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00973."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00973",
            brand="Apple",
            model_series="Apple Enterprise Series-0973",
            chassis_form_factor="Ultrabook 14-inch" if 973 % 3 == 0 else "Workstation 16-inch" if 973 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (973 % 35),
            ram_standard="DDR5-5600" if 973 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 973 % 2 == 0 else 32,
            nvme_slots=2 if 973 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 973 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (973 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 973 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00974(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00974."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00974",
            brand="Asus",
            model_series="Asus Enterprise Series-0974",
            chassis_form_factor="Ultrabook 14-inch" if 974 % 3 == 0 else "Workstation 16-inch" if 974 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (974 % 35),
            ram_standard="DDR5-5600" if 974 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 974 % 2 == 0 else 32,
            nvme_slots=2 if 974 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 974 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (974 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 974 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00975(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00975."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00975",
            brand="Acer",
            model_series="Acer Enterprise Series-0975",
            chassis_form_factor="Ultrabook 14-inch" if 975 % 3 == 0 else "Workstation 16-inch" if 975 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (975 % 35),
            ram_standard="DDR5-5600" if 975 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 975 % 2 == 0 else 32,
            nvme_slots=2 if 975 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 975 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (975 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 975 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00976(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00976."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00976",
            brand="MSI",
            model_series="MSI Enterprise Series-0976",
            chassis_form_factor="Ultrabook 14-inch" if 976 % 3 == 0 else "Workstation 16-inch" if 976 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (976 % 35),
            ram_standard="DDR5-5600" if 976 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 976 % 2 == 0 else 32,
            nvme_slots=2 if 976 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 976 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (976 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 976 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00977(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00977."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00977",
            brand="Razer",
            model_series="Razer Enterprise Series-0977",
            chassis_form_factor="Ultrabook 14-inch" if 977 % 3 == 0 else "Workstation 16-inch" if 977 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (977 % 35),
            ram_standard="DDR5-5600" if 977 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 977 % 2 == 0 else 32,
            nvme_slots=2 if 977 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 977 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (977 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 977 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00978(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00978."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00978",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0978",
            chassis_form_factor="Ultrabook 14-inch" if 978 % 3 == 0 else "Workstation 16-inch" if 978 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (978 % 35),
            ram_standard="DDR5-5600" if 978 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 978 % 2 == 0 else 32,
            nvme_slots=2 if 978 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 978 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (978 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 978 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00979(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00979."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00979",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0979",
            chassis_form_factor="Ultrabook 14-inch" if 979 % 3 == 0 else "Workstation 16-inch" if 979 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (979 % 35),
            ram_standard="DDR5-5600" if 979 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 979 % 2 == 0 else 32,
            nvme_slots=2 if 979 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 979 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (979 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 979 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00980(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00980."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00980",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0980",
            chassis_form_factor="Ultrabook 14-inch" if 980 % 3 == 0 else "Workstation 16-inch" if 980 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (980 % 35),
            ram_standard="DDR5-5600" if 980 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 980 % 2 == 0 else 32,
            nvme_slots=2 if 980 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 980 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (980 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 980 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00981(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00981."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00981",
            brand="Dell",
            model_series="Dell Enterprise Series-0981",
            chassis_form_factor="Ultrabook 14-inch" if 981 % 3 == 0 else "Workstation 16-inch" if 981 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (981 % 35),
            ram_standard="DDR5-5600" if 981 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 981 % 2 == 0 else 32,
            nvme_slots=2 if 981 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 981 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (981 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 981 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00982(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00982."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00982",
            brand="HP",
            model_series="HP Enterprise Series-0982",
            chassis_form_factor="Ultrabook 14-inch" if 982 % 3 == 0 else "Workstation 16-inch" if 982 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (982 % 35),
            ram_standard="DDR5-5600" if 982 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 982 % 2 == 0 else 32,
            nvme_slots=2 if 982 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 982 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (982 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 982 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00983(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00983."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00983",
            brand="Apple",
            model_series="Apple Enterprise Series-0983",
            chassis_form_factor="Ultrabook 14-inch" if 983 % 3 == 0 else "Workstation 16-inch" if 983 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (983 % 35),
            ram_standard="DDR5-5600" if 983 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 983 % 2 == 0 else 32,
            nvme_slots=2 if 983 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 983 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (983 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 983 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00984(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00984."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00984",
            brand="Asus",
            model_series="Asus Enterprise Series-0984",
            chassis_form_factor="Ultrabook 14-inch" if 984 % 3 == 0 else "Workstation 16-inch" if 984 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (984 % 35),
            ram_standard="DDR5-5600" if 984 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 984 % 2 == 0 else 32,
            nvme_slots=2 if 984 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 984 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (984 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 984 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00985(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00985."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00985",
            brand="Acer",
            model_series="Acer Enterprise Series-0985",
            chassis_form_factor="Ultrabook 14-inch" if 985 % 3 == 0 else "Workstation 16-inch" if 985 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (985 % 35),
            ram_standard="DDR5-5600" if 985 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 985 % 2 == 0 else 32,
            nvme_slots=2 if 985 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 985 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (985 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 985 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00986(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00986."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00986",
            brand="MSI",
            model_series="MSI Enterprise Series-0986",
            chassis_form_factor="Ultrabook 14-inch" if 986 % 3 == 0 else "Workstation 16-inch" if 986 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (986 % 35),
            ram_standard="DDR5-5600" if 986 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 986 % 2 == 0 else 32,
            nvme_slots=2 if 986 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 986 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (986 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 986 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00987(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00987."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00987",
            brand="Razer",
            model_series="Razer Enterprise Series-0987",
            chassis_form_factor="Ultrabook 14-inch" if 987 % 3 == 0 else "Workstation 16-inch" if 987 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (987 % 35),
            ram_standard="DDR5-5600" if 987 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 987 % 2 == 0 else 32,
            nvme_slots=2 if 987 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 987 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (987 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 987 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00988(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00988."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00988",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0988",
            chassis_form_factor="Ultrabook 14-inch" if 988 % 3 == 0 else "Workstation 16-inch" if 988 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (988 % 35),
            ram_standard="DDR5-5600" if 988 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 988 % 2 == 0 else 32,
            nvme_slots=2 if 988 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 988 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (988 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 988 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00989(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00989."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00989",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0989",
            chassis_form_factor="Ultrabook 14-inch" if 989 % 3 == 0 else "Workstation 16-inch" if 989 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (989 % 35),
            ram_standard="DDR5-5600" if 989 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 989 % 2 == 0 else 32,
            nvme_slots=2 if 989 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 989 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (989 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 989 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00990(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00990."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00990",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0990",
            chassis_form_factor="Ultrabook 14-inch" if 990 % 3 == 0 else "Workstation 16-inch" if 990 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (990 % 35),
            ram_standard="DDR5-5600" if 990 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 990 % 2 == 0 else 32,
            nvme_slots=2 if 990 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 990 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (990 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 990 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00991(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00991."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00991",
            brand="Dell",
            model_series="Dell Enterprise Series-0991",
            chassis_form_factor="Ultrabook 14-inch" if 991 % 3 == 0 else "Workstation 16-inch" if 991 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (991 % 35),
            ram_standard="DDR5-5600" if 991 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 991 % 2 == 0 else 32,
            nvme_slots=2 if 991 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 991 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (991 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 991 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00992(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00992."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00992",
            brand="HP",
            model_series="HP Enterprise Series-0992",
            chassis_form_factor="Ultrabook 14-inch" if 992 % 3 == 0 else "Workstation 16-inch" if 992 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (992 % 35),
            ram_standard="DDR5-5600" if 992 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 992 % 2 == 0 else 32,
            nvme_slots=2 if 992 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 992 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (992 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 992 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00993(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00993."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00993",
            brand="Apple",
            model_series="Apple Enterprise Series-0993",
            chassis_form_factor="Ultrabook 14-inch" if 993 % 3 == 0 else "Workstation 16-inch" if 993 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (993 % 35),
            ram_standard="DDR5-5600" if 993 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 993 % 2 == 0 else 32,
            nvme_slots=2 if 993 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 993 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (993 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 993 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00994(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00994."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00994",
            brand="Asus",
            model_series="Asus Enterprise Series-0994",
            chassis_form_factor="Ultrabook 14-inch" if 994 % 3 == 0 else "Workstation 16-inch" if 994 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (994 % 35),
            ram_standard="DDR5-5600" if 994 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 994 % 2 == 0 else 32,
            nvme_slots=2 if 994 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 994 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (994 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 994 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00995(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00995."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00995",
            brand="Acer",
            model_series="Acer Enterprise Series-0995",
            chassis_form_factor="Ultrabook 14-inch" if 995 % 3 == 0 else "Workstation 16-inch" if 995 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (995 % 35),
            ram_standard="DDR5-5600" if 995 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 995 % 2 == 0 else 32,
            nvme_slots=2 if 995 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 995 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (995 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 995 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00996(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00996."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00996",
            brand="MSI",
            model_series="MSI Enterprise Series-0996",
            chassis_form_factor="Ultrabook 14-inch" if 996 % 3 == 0 else "Workstation 16-inch" if 996 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (996 % 35),
            ram_standard="DDR5-5600" if 996 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 996 % 2 == 0 else 32,
            nvme_slots=2 if 996 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 996 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (996 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 996 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00997(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00997."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00997",
            brand="Razer",
            model_series="Razer Enterprise Series-0997",
            chassis_form_factor="Ultrabook 14-inch" if 997 % 3 == 0 else "Workstation 16-inch" if 997 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (997 % 35),
            ram_standard="DDR5-5600" if 997 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 997 % 2 == 0 else 32,
            nvme_slots=2 if 997 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 997 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (997 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 997 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00998(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00998."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00998",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0998",
            chassis_form_factor="Ultrabook 14-inch" if 998 % 3 == 0 else "Workstation 16-inch" if 998 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (998 % 35),
            ram_standard="DDR5-5600" if 998 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 998 % 2 == 0 else 32,
            nvme_slots=2 if 998 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 998 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (998 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 998 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00999(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00999."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00999",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0999",
            chassis_form_factor="Ultrabook 14-inch" if 999 % 3 == 0 else "Workstation 16-inch" if 999 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (999 % 35),
            ram_standard="DDR5-5600" if 999 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 999 % 2 == 0 else 32,
            nvme_slots=2 if 999 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 999 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (999 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 999 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_01000(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-01000."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-01000",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-1000",
            chassis_form_factor="Ultrabook 14-inch" if 1000 % 3 == 0 else "Workstation 16-inch" if 1000 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (1000 % 35),
            ram_standard="DDR5-5600" if 1000 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 1000 % 2 == 0 else 32,
            nvme_slots=2 if 1000 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 1000 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (1000 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 1000 % 2 == 0 else "1-Year Depot Warranty",
        )
