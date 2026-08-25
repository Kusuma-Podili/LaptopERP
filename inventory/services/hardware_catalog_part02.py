"""
Enterprise Hardware Model Database - Part 02.
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

class HardwareCatalogDatabasePart02:
    """Hardware inventory profile definitions part 02."""

    @classmethod
    def get_hardware_profile_00201(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00201."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00201",
            brand="Dell",
            model_series="Dell Enterprise Series-0201",
            chassis_form_factor="Ultrabook 14-inch" if 201 % 3 == 0 else "Workstation 16-inch" if 201 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (201 % 35),
            ram_standard="DDR5-5600" if 201 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 201 % 2 == 0 else 32,
            nvme_slots=2 if 201 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 201 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (201 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 201 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00202(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00202."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00202",
            brand="HP",
            model_series="HP Enterprise Series-0202",
            chassis_form_factor="Ultrabook 14-inch" if 202 % 3 == 0 else "Workstation 16-inch" if 202 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (202 % 35),
            ram_standard="DDR5-5600" if 202 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 202 % 2 == 0 else 32,
            nvme_slots=2 if 202 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 202 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (202 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 202 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00203(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00203."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00203",
            brand="Apple",
            model_series="Apple Enterprise Series-0203",
            chassis_form_factor="Ultrabook 14-inch" if 203 % 3 == 0 else "Workstation 16-inch" if 203 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (203 % 35),
            ram_standard="DDR5-5600" if 203 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 203 % 2 == 0 else 32,
            nvme_slots=2 if 203 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 203 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (203 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 203 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00204(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00204."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00204",
            brand="Asus",
            model_series="Asus Enterprise Series-0204",
            chassis_form_factor="Ultrabook 14-inch" if 204 % 3 == 0 else "Workstation 16-inch" if 204 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (204 % 35),
            ram_standard="DDR5-5600" if 204 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 204 % 2 == 0 else 32,
            nvme_slots=2 if 204 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 204 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (204 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 204 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00205(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00205."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00205",
            brand="Acer",
            model_series="Acer Enterprise Series-0205",
            chassis_form_factor="Ultrabook 14-inch" if 205 % 3 == 0 else "Workstation 16-inch" if 205 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (205 % 35),
            ram_standard="DDR5-5600" if 205 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 205 % 2 == 0 else 32,
            nvme_slots=2 if 205 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 205 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (205 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 205 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00206(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00206."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00206",
            brand="MSI",
            model_series="MSI Enterprise Series-0206",
            chassis_form_factor="Ultrabook 14-inch" if 206 % 3 == 0 else "Workstation 16-inch" if 206 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (206 % 35),
            ram_standard="DDR5-5600" if 206 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 206 % 2 == 0 else 32,
            nvme_slots=2 if 206 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 206 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (206 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 206 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00207(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00207."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00207",
            brand="Razer",
            model_series="Razer Enterprise Series-0207",
            chassis_form_factor="Ultrabook 14-inch" if 207 % 3 == 0 else "Workstation 16-inch" if 207 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (207 % 35),
            ram_standard="DDR5-5600" if 207 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 207 % 2 == 0 else 32,
            nvme_slots=2 if 207 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 207 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (207 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 207 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00208(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00208."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00208",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0208",
            chassis_form_factor="Ultrabook 14-inch" if 208 % 3 == 0 else "Workstation 16-inch" if 208 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (208 % 35),
            ram_standard="DDR5-5600" if 208 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 208 % 2 == 0 else 32,
            nvme_slots=2 if 208 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 208 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (208 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 208 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00209(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00209."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00209",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0209",
            chassis_form_factor="Ultrabook 14-inch" if 209 % 3 == 0 else "Workstation 16-inch" if 209 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (209 % 35),
            ram_standard="DDR5-5600" if 209 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 209 % 2 == 0 else 32,
            nvme_slots=2 if 209 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 209 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (209 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 209 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00210(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00210."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00210",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0210",
            chassis_form_factor="Ultrabook 14-inch" if 210 % 3 == 0 else "Workstation 16-inch" if 210 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (210 % 35),
            ram_standard="DDR5-5600" if 210 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 210 % 2 == 0 else 32,
            nvme_slots=2 if 210 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 210 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (210 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 210 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00211(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00211."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00211",
            brand="Dell",
            model_series="Dell Enterprise Series-0211",
            chassis_form_factor="Ultrabook 14-inch" if 211 % 3 == 0 else "Workstation 16-inch" if 211 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (211 % 35),
            ram_standard="DDR5-5600" if 211 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 211 % 2 == 0 else 32,
            nvme_slots=2 if 211 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 211 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (211 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 211 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00212(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00212."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00212",
            brand="HP",
            model_series="HP Enterprise Series-0212",
            chassis_form_factor="Ultrabook 14-inch" if 212 % 3 == 0 else "Workstation 16-inch" if 212 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (212 % 35),
            ram_standard="DDR5-5600" if 212 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 212 % 2 == 0 else 32,
            nvme_slots=2 if 212 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 212 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (212 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 212 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00213(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00213."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00213",
            brand="Apple",
            model_series="Apple Enterprise Series-0213",
            chassis_form_factor="Ultrabook 14-inch" if 213 % 3 == 0 else "Workstation 16-inch" if 213 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (213 % 35),
            ram_standard="DDR5-5600" if 213 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 213 % 2 == 0 else 32,
            nvme_slots=2 if 213 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 213 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (213 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 213 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00214(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00214."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00214",
            brand="Asus",
            model_series="Asus Enterprise Series-0214",
            chassis_form_factor="Ultrabook 14-inch" if 214 % 3 == 0 else "Workstation 16-inch" if 214 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (214 % 35),
            ram_standard="DDR5-5600" if 214 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 214 % 2 == 0 else 32,
            nvme_slots=2 if 214 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 214 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (214 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 214 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00215(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00215."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00215",
            brand="Acer",
            model_series="Acer Enterprise Series-0215",
            chassis_form_factor="Ultrabook 14-inch" if 215 % 3 == 0 else "Workstation 16-inch" if 215 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (215 % 35),
            ram_standard="DDR5-5600" if 215 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 215 % 2 == 0 else 32,
            nvme_slots=2 if 215 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 215 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (215 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 215 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00216(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00216."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00216",
            brand="MSI",
            model_series="MSI Enterprise Series-0216",
            chassis_form_factor="Ultrabook 14-inch" if 216 % 3 == 0 else "Workstation 16-inch" if 216 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (216 % 35),
            ram_standard="DDR5-5600" if 216 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 216 % 2 == 0 else 32,
            nvme_slots=2 if 216 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 216 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (216 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 216 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00217(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00217."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00217",
            brand="Razer",
            model_series="Razer Enterprise Series-0217",
            chassis_form_factor="Ultrabook 14-inch" if 217 % 3 == 0 else "Workstation 16-inch" if 217 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (217 % 35),
            ram_standard="DDR5-5600" if 217 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 217 % 2 == 0 else 32,
            nvme_slots=2 if 217 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 217 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (217 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 217 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00218(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00218."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00218",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0218",
            chassis_form_factor="Ultrabook 14-inch" if 218 % 3 == 0 else "Workstation 16-inch" if 218 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (218 % 35),
            ram_standard="DDR5-5600" if 218 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 218 % 2 == 0 else 32,
            nvme_slots=2 if 218 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 218 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (218 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 218 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00219(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00219."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00219",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0219",
            chassis_form_factor="Ultrabook 14-inch" if 219 % 3 == 0 else "Workstation 16-inch" if 219 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (219 % 35),
            ram_standard="DDR5-5600" if 219 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 219 % 2 == 0 else 32,
            nvme_slots=2 if 219 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 219 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (219 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 219 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00220(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00220."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00220",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0220",
            chassis_form_factor="Ultrabook 14-inch" if 220 % 3 == 0 else "Workstation 16-inch" if 220 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (220 % 35),
            ram_standard="DDR5-5600" if 220 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 220 % 2 == 0 else 32,
            nvme_slots=2 if 220 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 220 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (220 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 220 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00221(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00221."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00221",
            brand="Dell",
            model_series="Dell Enterprise Series-0221",
            chassis_form_factor="Ultrabook 14-inch" if 221 % 3 == 0 else "Workstation 16-inch" if 221 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (221 % 35),
            ram_standard="DDR5-5600" if 221 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 221 % 2 == 0 else 32,
            nvme_slots=2 if 221 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 221 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (221 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 221 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00222(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00222."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00222",
            brand="HP",
            model_series="HP Enterprise Series-0222",
            chassis_form_factor="Ultrabook 14-inch" if 222 % 3 == 0 else "Workstation 16-inch" if 222 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (222 % 35),
            ram_standard="DDR5-5600" if 222 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 222 % 2 == 0 else 32,
            nvme_slots=2 if 222 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 222 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (222 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 222 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00223(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00223."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00223",
            brand="Apple",
            model_series="Apple Enterprise Series-0223",
            chassis_form_factor="Ultrabook 14-inch" if 223 % 3 == 0 else "Workstation 16-inch" if 223 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (223 % 35),
            ram_standard="DDR5-5600" if 223 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 223 % 2 == 0 else 32,
            nvme_slots=2 if 223 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 223 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (223 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 223 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00224(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00224."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00224",
            brand="Asus",
            model_series="Asus Enterprise Series-0224",
            chassis_form_factor="Ultrabook 14-inch" if 224 % 3 == 0 else "Workstation 16-inch" if 224 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (224 % 35),
            ram_standard="DDR5-5600" if 224 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 224 % 2 == 0 else 32,
            nvme_slots=2 if 224 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 224 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (224 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 224 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00225(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00225."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00225",
            brand="Acer",
            model_series="Acer Enterprise Series-0225",
            chassis_form_factor="Ultrabook 14-inch" if 225 % 3 == 0 else "Workstation 16-inch" if 225 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (225 % 35),
            ram_standard="DDR5-5600" if 225 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 225 % 2 == 0 else 32,
            nvme_slots=2 if 225 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 225 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (225 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 225 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00226(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00226."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00226",
            brand="MSI",
            model_series="MSI Enterprise Series-0226",
            chassis_form_factor="Ultrabook 14-inch" if 226 % 3 == 0 else "Workstation 16-inch" if 226 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (226 % 35),
            ram_standard="DDR5-5600" if 226 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 226 % 2 == 0 else 32,
            nvme_slots=2 if 226 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 226 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (226 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 226 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00227(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00227."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00227",
            brand="Razer",
            model_series="Razer Enterprise Series-0227",
            chassis_form_factor="Ultrabook 14-inch" if 227 % 3 == 0 else "Workstation 16-inch" if 227 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (227 % 35),
            ram_standard="DDR5-5600" if 227 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 227 % 2 == 0 else 32,
            nvme_slots=2 if 227 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 227 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (227 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 227 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00228(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00228."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00228",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0228",
            chassis_form_factor="Ultrabook 14-inch" if 228 % 3 == 0 else "Workstation 16-inch" if 228 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (228 % 35),
            ram_standard="DDR5-5600" if 228 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 228 % 2 == 0 else 32,
            nvme_slots=2 if 228 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 228 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (228 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 228 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00229(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00229."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00229",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0229",
            chassis_form_factor="Ultrabook 14-inch" if 229 % 3 == 0 else "Workstation 16-inch" if 229 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (229 % 35),
            ram_standard="DDR5-5600" if 229 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 229 % 2 == 0 else 32,
            nvme_slots=2 if 229 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 229 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (229 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 229 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00230(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00230."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00230",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0230",
            chassis_form_factor="Ultrabook 14-inch" if 230 % 3 == 0 else "Workstation 16-inch" if 230 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (230 % 35),
            ram_standard="DDR5-5600" if 230 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 230 % 2 == 0 else 32,
            nvme_slots=2 if 230 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 230 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (230 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 230 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00231(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00231."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00231",
            brand="Dell",
            model_series="Dell Enterprise Series-0231",
            chassis_form_factor="Ultrabook 14-inch" if 231 % 3 == 0 else "Workstation 16-inch" if 231 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (231 % 35),
            ram_standard="DDR5-5600" if 231 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 231 % 2 == 0 else 32,
            nvme_slots=2 if 231 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 231 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (231 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 231 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00232(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00232."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00232",
            brand="HP",
            model_series="HP Enterprise Series-0232",
            chassis_form_factor="Ultrabook 14-inch" if 232 % 3 == 0 else "Workstation 16-inch" if 232 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (232 % 35),
            ram_standard="DDR5-5600" if 232 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 232 % 2 == 0 else 32,
            nvme_slots=2 if 232 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 232 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (232 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 232 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00233(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00233."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00233",
            brand="Apple",
            model_series="Apple Enterprise Series-0233",
            chassis_form_factor="Ultrabook 14-inch" if 233 % 3 == 0 else "Workstation 16-inch" if 233 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (233 % 35),
            ram_standard="DDR5-5600" if 233 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 233 % 2 == 0 else 32,
            nvme_slots=2 if 233 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 233 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (233 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 233 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00234(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00234."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00234",
            brand="Asus",
            model_series="Asus Enterprise Series-0234",
            chassis_form_factor="Ultrabook 14-inch" if 234 % 3 == 0 else "Workstation 16-inch" if 234 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (234 % 35),
            ram_standard="DDR5-5600" if 234 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 234 % 2 == 0 else 32,
            nvme_slots=2 if 234 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 234 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (234 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 234 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00235(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00235."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00235",
            brand="Acer",
            model_series="Acer Enterprise Series-0235",
            chassis_form_factor="Ultrabook 14-inch" if 235 % 3 == 0 else "Workstation 16-inch" if 235 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (235 % 35),
            ram_standard="DDR5-5600" if 235 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 235 % 2 == 0 else 32,
            nvme_slots=2 if 235 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 235 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (235 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 235 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00236(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00236."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00236",
            brand="MSI",
            model_series="MSI Enterprise Series-0236",
            chassis_form_factor="Ultrabook 14-inch" if 236 % 3 == 0 else "Workstation 16-inch" if 236 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (236 % 35),
            ram_standard="DDR5-5600" if 236 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 236 % 2 == 0 else 32,
            nvme_slots=2 if 236 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 236 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (236 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 236 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00237(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00237."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00237",
            brand="Razer",
            model_series="Razer Enterprise Series-0237",
            chassis_form_factor="Ultrabook 14-inch" if 237 % 3 == 0 else "Workstation 16-inch" if 237 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (237 % 35),
            ram_standard="DDR5-5600" if 237 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 237 % 2 == 0 else 32,
            nvme_slots=2 if 237 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 237 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (237 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 237 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00238(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00238."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00238",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0238",
            chassis_form_factor="Ultrabook 14-inch" if 238 % 3 == 0 else "Workstation 16-inch" if 238 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (238 % 35),
            ram_standard="DDR5-5600" if 238 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 238 % 2 == 0 else 32,
            nvme_slots=2 if 238 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 238 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (238 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 238 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00239(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00239."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00239",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0239",
            chassis_form_factor="Ultrabook 14-inch" if 239 % 3 == 0 else "Workstation 16-inch" if 239 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (239 % 35),
            ram_standard="DDR5-5600" if 239 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 239 % 2 == 0 else 32,
            nvme_slots=2 if 239 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 239 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (239 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 239 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00240(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00240."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00240",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0240",
            chassis_form_factor="Ultrabook 14-inch" if 240 % 3 == 0 else "Workstation 16-inch" if 240 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (240 % 35),
            ram_standard="DDR5-5600" if 240 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 240 % 2 == 0 else 32,
            nvme_slots=2 if 240 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 240 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (240 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 240 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00241(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00241."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00241",
            brand="Dell",
            model_series="Dell Enterprise Series-0241",
            chassis_form_factor="Ultrabook 14-inch" if 241 % 3 == 0 else "Workstation 16-inch" if 241 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (241 % 35),
            ram_standard="DDR5-5600" if 241 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 241 % 2 == 0 else 32,
            nvme_slots=2 if 241 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 241 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (241 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 241 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00242(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00242."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00242",
            brand="HP",
            model_series="HP Enterprise Series-0242",
            chassis_form_factor="Ultrabook 14-inch" if 242 % 3 == 0 else "Workstation 16-inch" if 242 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (242 % 35),
            ram_standard="DDR5-5600" if 242 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 242 % 2 == 0 else 32,
            nvme_slots=2 if 242 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 242 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (242 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 242 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00243(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00243."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00243",
            brand="Apple",
            model_series="Apple Enterprise Series-0243",
            chassis_form_factor="Ultrabook 14-inch" if 243 % 3 == 0 else "Workstation 16-inch" if 243 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (243 % 35),
            ram_standard="DDR5-5600" if 243 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 243 % 2 == 0 else 32,
            nvme_slots=2 if 243 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 243 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (243 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 243 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00244(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00244."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00244",
            brand="Asus",
            model_series="Asus Enterprise Series-0244",
            chassis_form_factor="Ultrabook 14-inch" if 244 % 3 == 0 else "Workstation 16-inch" if 244 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (244 % 35),
            ram_standard="DDR5-5600" if 244 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 244 % 2 == 0 else 32,
            nvme_slots=2 if 244 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 244 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (244 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 244 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00245(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00245."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00245",
            brand="Acer",
            model_series="Acer Enterprise Series-0245",
            chassis_form_factor="Ultrabook 14-inch" if 245 % 3 == 0 else "Workstation 16-inch" if 245 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (245 % 35),
            ram_standard="DDR5-5600" if 245 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 245 % 2 == 0 else 32,
            nvme_slots=2 if 245 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 245 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (245 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 245 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00246(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00246."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00246",
            brand="MSI",
            model_series="MSI Enterprise Series-0246",
            chassis_form_factor="Ultrabook 14-inch" if 246 % 3 == 0 else "Workstation 16-inch" if 246 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (246 % 35),
            ram_standard="DDR5-5600" if 246 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 246 % 2 == 0 else 32,
            nvme_slots=2 if 246 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 246 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (246 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 246 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00247(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00247."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00247",
            brand="Razer",
            model_series="Razer Enterprise Series-0247",
            chassis_form_factor="Ultrabook 14-inch" if 247 % 3 == 0 else "Workstation 16-inch" if 247 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (247 % 35),
            ram_standard="DDR5-5600" if 247 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 247 % 2 == 0 else 32,
            nvme_slots=2 if 247 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 247 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (247 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 247 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00248(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00248."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00248",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0248",
            chassis_form_factor="Ultrabook 14-inch" if 248 % 3 == 0 else "Workstation 16-inch" if 248 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (248 % 35),
            ram_standard="DDR5-5600" if 248 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 248 % 2 == 0 else 32,
            nvme_slots=2 if 248 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 248 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (248 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 248 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00249(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00249."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00249",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0249",
            chassis_form_factor="Ultrabook 14-inch" if 249 % 3 == 0 else "Workstation 16-inch" if 249 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (249 % 35),
            ram_standard="DDR5-5600" if 249 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 249 % 2 == 0 else 32,
            nvme_slots=2 if 249 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 249 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (249 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 249 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00250(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00250."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00250",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0250",
            chassis_form_factor="Ultrabook 14-inch" if 250 % 3 == 0 else "Workstation 16-inch" if 250 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (250 % 35),
            ram_standard="DDR5-5600" if 250 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 250 % 2 == 0 else 32,
            nvme_slots=2 if 250 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 250 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (250 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 250 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00251(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00251."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00251",
            brand="Dell",
            model_series="Dell Enterprise Series-0251",
            chassis_form_factor="Ultrabook 14-inch" if 251 % 3 == 0 else "Workstation 16-inch" if 251 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (251 % 35),
            ram_standard="DDR5-5600" if 251 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 251 % 2 == 0 else 32,
            nvme_slots=2 if 251 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 251 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (251 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 251 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00252(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00252."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00252",
            brand="HP",
            model_series="HP Enterprise Series-0252",
            chassis_form_factor="Ultrabook 14-inch" if 252 % 3 == 0 else "Workstation 16-inch" if 252 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (252 % 35),
            ram_standard="DDR5-5600" if 252 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 252 % 2 == 0 else 32,
            nvme_slots=2 if 252 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 252 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (252 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 252 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00253(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00253."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00253",
            brand="Apple",
            model_series="Apple Enterprise Series-0253",
            chassis_form_factor="Ultrabook 14-inch" if 253 % 3 == 0 else "Workstation 16-inch" if 253 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (253 % 35),
            ram_standard="DDR5-5600" if 253 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 253 % 2 == 0 else 32,
            nvme_slots=2 if 253 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 253 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (253 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 253 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00254(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00254."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00254",
            brand="Asus",
            model_series="Asus Enterprise Series-0254",
            chassis_form_factor="Ultrabook 14-inch" if 254 % 3 == 0 else "Workstation 16-inch" if 254 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (254 % 35),
            ram_standard="DDR5-5600" if 254 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 254 % 2 == 0 else 32,
            nvme_slots=2 if 254 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 254 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (254 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 254 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00255(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00255."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00255",
            brand="Acer",
            model_series="Acer Enterprise Series-0255",
            chassis_form_factor="Ultrabook 14-inch" if 255 % 3 == 0 else "Workstation 16-inch" if 255 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (255 % 35),
            ram_standard="DDR5-5600" if 255 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 255 % 2 == 0 else 32,
            nvme_slots=2 if 255 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 255 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (255 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 255 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00256(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00256."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00256",
            brand="MSI",
            model_series="MSI Enterprise Series-0256",
            chassis_form_factor="Ultrabook 14-inch" if 256 % 3 == 0 else "Workstation 16-inch" if 256 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (256 % 35),
            ram_standard="DDR5-5600" if 256 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 256 % 2 == 0 else 32,
            nvme_slots=2 if 256 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 256 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (256 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 256 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00257(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00257."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00257",
            brand="Razer",
            model_series="Razer Enterprise Series-0257",
            chassis_form_factor="Ultrabook 14-inch" if 257 % 3 == 0 else "Workstation 16-inch" if 257 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (257 % 35),
            ram_standard="DDR5-5600" if 257 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 257 % 2 == 0 else 32,
            nvme_slots=2 if 257 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 257 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (257 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 257 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00258(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00258."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00258",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0258",
            chassis_form_factor="Ultrabook 14-inch" if 258 % 3 == 0 else "Workstation 16-inch" if 258 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (258 % 35),
            ram_standard="DDR5-5600" if 258 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 258 % 2 == 0 else 32,
            nvme_slots=2 if 258 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 258 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (258 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 258 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00259(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00259."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00259",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0259",
            chassis_form_factor="Ultrabook 14-inch" if 259 % 3 == 0 else "Workstation 16-inch" if 259 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (259 % 35),
            ram_standard="DDR5-5600" if 259 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 259 % 2 == 0 else 32,
            nvme_slots=2 if 259 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 259 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (259 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 259 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00260(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00260."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00260",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0260",
            chassis_form_factor="Ultrabook 14-inch" if 260 % 3 == 0 else "Workstation 16-inch" if 260 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (260 % 35),
            ram_standard="DDR5-5600" if 260 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 260 % 2 == 0 else 32,
            nvme_slots=2 if 260 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 260 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (260 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 260 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00261(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00261."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00261",
            brand="Dell",
            model_series="Dell Enterprise Series-0261",
            chassis_form_factor="Ultrabook 14-inch" if 261 % 3 == 0 else "Workstation 16-inch" if 261 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (261 % 35),
            ram_standard="DDR5-5600" if 261 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 261 % 2 == 0 else 32,
            nvme_slots=2 if 261 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 261 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (261 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 261 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00262(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00262."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00262",
            brand="HP",
            model_series="HP Enterprise Series-0262",
            chassis_form_factor="Ultrabook 14-inch" if 262 % 3 == 0 else "Workstation 16-inch" if 262 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (262 % 35),
            ram_standard="DDR5-5600" if 262 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 262 % 2 == 0 else 32,
            nvme_slots=2 if 262 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 262 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (262 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 262 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00263(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00263."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00263",
            brand="Apple",
            model_series="Apple Enterprise Series-0263",
            chassis_form_factor="Ultrabook 14-inch" if 263 % 3 == 0 else "Workstation 16-inch" if 263 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (263 % 35),
            ram_standard="DDR5-5600" if 263 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 263 % 2 == 0 else 32,
            nvme_slots=2 if 263 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 263 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (263 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 263 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00264(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00264."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00264",
            brand="Asus",
            model_series="Asus Enterprise Series-0264",
            chassis_form_factor="Ultrabook 14-inch" if 264 % 3 == 0 else "Workstation 16-inch" if 264 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (264 % 35),
            ram_standard="DDR5-5600" if 264 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 264 % 2 == 0 else 32,
            nvme_slots=2 if 264 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 264 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (264 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 264 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00265(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00265."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00265",
            brand="Acer",
            model_series="Acer Enterprise Series-0265",
            chassis_form_factor="Ultrabook 14-inch" if 265 % 3 == 0 else "Workstation 16-inch" if 265 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (265 % 35),
            ram_standard="DDR5-5600" if 265 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 265 % 2 == 0 else 32,
            nvme_slots=2 if 265 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 265 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (265 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 265 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00266(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00266."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00266",
            brand="MSI",
            model_series="MSI Enterprise Series-0266",
            chassis_form_factor="Ultrabook 14-inch" if 266 % 3 == 0 else "Workstation 16-inch" if 266 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (266 % 35),
            ram_standard="DDR5-5600" if 266 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 266 % 2 == 0 else 32,
            nvme_slots=2 if 266 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 266 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (266 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 266 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00267(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00267."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00267",
            brand="Razer",
            model_series="Razer Enterprise Series-0267",
            chassis_form_factor="Ultrabook 14-inch" if 267 % 3 == 0 else "Workstation 16-inch" if 267 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (267 % 35),
            ram_standard="DDR5-5600" if 267 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 267 % 2 == 0 else 32,
            nvme_slots=2 if 267 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 267 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (267 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 267 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00268(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00268."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00268",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0268",
            chassis_form_factor="Ultrabook 14-inch" if 268 % 3 == 0 else "Workstation 16-inch" if 268 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (268 % 35),
            ram_standard="DDR5-5600" if 268 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 268 % 2 == 0 else 32,
            nvme_slots=2 if 268 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 268 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (268 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 268 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00269(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00269."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00269",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0269",
            chassis_form_factor="Ultrabook 14-inch" if 269 % 3 == 0 else "Workstation 16-inch" if 269 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (269 % 35),
            ram_standard="DDR5-5600" if 269 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 269 % 2 == 0 else 32,
            nvme_slots=2 if 269 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 269 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (269 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 269 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00270(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00270."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00270",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0270",
            chassis_form_factor="Ultrabook 14-inch" if 270 % 3 == 0 else "Workstation 16-inch" if 270 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (270 % 35),
            ram_standard="DDR5-5600" if 270 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 270 % 2 == 0 else 32,
            nvme_slots=2 if 270 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 270 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (270 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 270 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00271(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00271."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00271",
            brand="Dell",
            model_series="Dell Enterprise Series-0271",
            chassis_form_factor="Ultrabook 14-inch" if 271 % 3 == 0 else "Workstation 16-inch" if 271 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (271 % 35),
            ram_standard="DDR5-5600" if 271 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 271 % 2 == 0 else 32,
            nvme_slots=2 if 271 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 271 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (271 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 271 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00272(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00272."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00272",
            brand="HP",
            model_series="HP Enterprise Series-0272",
            chassis_form_factor="Ultrabook 14-inch" if 272 % 3 == 0 else "Workstation 16-inch" if 272 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (272 % 35),
            ram_standard="DDR5-5600" if 272 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 272 % 2 == 0 else 32,
            nvme_slots=2 if 272 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 272 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (272 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 272 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00273(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00273."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00273",
            brand="Apple",
            model_series="Apple Enterprise Series-0273",
            chassis_form_factor="Ultrabook 14-inch" if 273 % 3 == 0 else "Workstation 16-inch" if 273 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (273 % 35),
            ram_standard="DDR5-5600" if 273 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 273 % 2 == 0 else 32,
            nvme_slots=2 if 273 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 273 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (273 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 273 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00274(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00274."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00274",
            brand="Asus",
            model_series="Asus Enterprise Series-0274",
            chassis_form_factor="Ultrabook 14-inch" if 274 % 3 == 0 else "Workstation 16-inch" if 274 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (274 % 35),
            ram_standard="DDR5-5600" if 274 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 274 % 2 == 0 else 32,
            nvme_slots=2 if 274 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 274 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (274 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 274 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00275(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00275."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00275",
            brand="Acer",
            model_series="Acer Enterprise Series-0275",
            chassis_form_factor="Ultrabook 14-inch" if 275 % 3 == 0 else "Workstation 16-inch" if 275 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (275 % 35),
            ram_standard="DDR5-5600" if 275 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 275 % 2 == 0 else 32,
            nvme_slots=2 if 275 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 275 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (275 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 275 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00276(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00276."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00276",
            brand="MSI",
            model_series="MSI Enterprise Series-0276",
            chassis_form_factor="Ultrabook 14-inch" if 276 % 3 == 0 else "Workstation 16-inch" if 276 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (276 % 35),
            ram_standard="DDR5-5600" if 276 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 276 % 2 == 0 else 32,
            nvme_slots=2 if 276 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 276 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (276 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 276 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00277(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00277."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00277",
            brand="Razer",
            model_series="Razer Enterprise Series-0277",
            chassis_form_factor="Ultrabook 14-inch" if 277 % 3 == 0 else "Workstation 16-inch" if 277 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (277 % 35),
            ram_standard="DDR5-5600" if 277 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 277 % 2 == 0 else 32,
            nvme_slots=2 if 277 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 277 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (277 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 277 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00278(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00278."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00278",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0278",
            chassis_form_factor="Ultrabook 14-inch" if 278 % 3 == 0 else "Workstation 16-inch" if 278 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (278 % 35),
            ram_standard="DDR5-5600" if 278 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 278 % 2 == 0 else 32,
            nvme_slots=2 if 278 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 278 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (278 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 278 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00279(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00279."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00279",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0279",
            chassis_form_factor="Ultrabook 14-inch" if 279 % 3 == 0 else "Workstation 16-inch" if 279 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (279 % 35),
            ram_standard="DDR5-5600" if 279 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 279 % 2 == 0 else 32,
            nvme_slots=2 if 279 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 279 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (279 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 279 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00280(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00280."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00280",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0280",
            chassis_form_factor="Ultrabook 14-inch" if 280 % 3 == 0 else "Workstation 16-inch" if 280 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (280 % 35),
            ram_standard="DDR5-5600" if 280 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 280 % 2 == 0 else 32,
            nvme_slots=2 if 280 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 280 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (280 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 280 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00281(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00281."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00281",
            brand="Dell",
            model_series="Dell Enterprise Series-0281",
            chassis_form_factor="Ultrabook 14-inch" if 281 % 3 == 0 else "Workstation 16-inch" if 281 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (281 % 35),
            ram_standard="DDR5-5600" if 281 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 281 % 2 == 0 else 32,
            nvme_slots=2 if 281 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 281 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (281 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 281 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00282(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00282."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00282",
            brand="HP",
            model_series="HP Enterprise Series-0282",
            chassis_form_factor="Ultrabook 14-inch" if 282 % 3 == 0 else "Workstation 16-inch" if 282 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (282 % 35),
            ram_standard="DDR5-5600" if 282 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 282 % 2 == 0 else 32,
            nvme_slots=2 if 282 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 282 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (282 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 282 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00283(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00283."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00283",
            brand="Apple",
            model_series="Apple Enterprise Series-0283",
            chassis_form_factor="Ultrabook 14-inch" if 283 % 3 == 0 else "Workstation 16-inch" if 283 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (283 % 35),
            ram_standard="DDR5-5600" if 283 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 283 % 2 == 0 else 32,
            nvme_slots=2 if 283 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 283 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (283 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 283 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00284(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00284."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00284",
            brand="Asus",
            model_series="Asus Enterprise Series-0284",
            chassis_form_factor="Ultrabook 14-inch" if 284 % 3 == 0 else "Workstation 16-inch" if 284 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (284 % 35),
            ram_standard="DDR5-5600" if 284 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 284 % 2 == 0 else 32,
            nvme_slots=2 if 284 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 284 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (284 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 284 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00285(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00285."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00285",
            brand="Acer",
            model_series="Acer Enterprise Series-0285",
            chassis_form_factor="Ultrabook 14-inch" if 285 % 3 == 0 else "Workstation 16-inch" if 285 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (285 % 35),
            ram_standard="DDR5-5600" if 285 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 285 % 2 == 0 else 32,
            nvme_slots=2 if 285 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 285 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (285 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 285 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00286(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00286."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00286",
            brand="MSI",
            model_series="MSI Enterprise Series-0286",
            chassis_form_factor="Ultrabook 14-inch" if 286 % 3 == 0 else "Workstation 16-inch" if 286 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (286 % 35),
            ram_standard="DDR5-5600" if 286 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 286 % 2 == 0 else 32,
            nvme_slots=2 if 286 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 286 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (286 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 286 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00287(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00287."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00287",
            brand="Razer",
            model_series="Razer Enterprise Series-0287",
            chassis_form_factor="Ultrabook 14-inch" if 287 % 3 == 0 else "Workstation 16-inch" if 287 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (287 % 35),
            ram_standard="DDR5-5600" if 287 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 287 % 2 == 0 else 32,
            nvme_slots=2 if 287 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 287 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (287 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 287 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00288(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00288."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00288",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0288",
            chassis_form_factor="Ultrabook 14-inch" if 288 % 3 == 0 else "Workstation 16-inch" if 288 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (288 % 35),
            ram_standard="DDR5-5600" if 288 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 288 % 2 == 0 else 32,
            nvme_slots=2 if 288 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 288 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (288 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 288 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00289(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00289."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00289",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0289",
            chassis_form_factor="Ultrabook 14-inch" if 289 % 3 == 0 else "Workstation 16-inch" if 289 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (289 % 35),
            ram_standard="DDR5-5600" if 289 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 289 % 2 == 0 else 32,
            nvme_slots=2 if 289 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 289 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (289 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 289 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00290(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00290."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00290",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0290",
            chassis_form_factor="Ultrabook 14-inch" if 290 % 3 == 0 else "Workstation 16-inch" if 290 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (290 % 35),
            ram_standard="DDR5-5600" if 290 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 290 % 2 == 0 else 32,
            nvme_slots=2 if 290 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 290 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (290 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 290 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00291(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00291."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00291",
            brand="Dell",
            model_series="Dell Enterprise Series-0291",
            chassis_form_factor="Ultrabook 14-inch" if 291 % 3 == 0 else "Workstation 16-inch" if 291 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (291 % 35),
            ram_standard="DDR5-5600" if 291 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 291 % 2 == 0 else 32,
            nvme_slots=2 if 291 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 291 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (291 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 291 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00292(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00292."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00292",
            brand="HP",
            model_series="HP Enterprise Series-0292",
            chassis_form_factor="Ultrabook 14-inch" if 292 % 3 == 0 else "Workstation 16-inch" if 292 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (292 % 35),
            ram_standard="DDR5-5600" if 292 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 292 % 2 == 0 else 32,
            nvme_slots=2 if 292 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 292 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (292 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 292 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00293(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00293."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00293",
            brand="Apple",
            model_series="Apple Enterprise Series-0293",
            chassis_form_factor="Ultrabook 14-inch" if 293 % 3 == 0 else "Workstation 16-inch" if 293 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (293 % 35),
            ram_standard="DDR5-5600" if 293 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 293 % 2 == 0 else 32,
            nvme_slots=2 if 293 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 293 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (293 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 293 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00294(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00294."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00294",
            brand="Asus",
            model_series="Asus Enterprise Series-0294",
            chassis_form_factor="Ultrabook 14-inch" if 294 % 3 == 0 else "Workstation 16-inch" if 294 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (294 % 35),
            ram_standard="DDR5-5600" if 294 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 294 % 2 == 0 else 32,
            nvme_slots=2 if 294 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 294 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (294 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 294 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00295(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00295."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00295",
            brand="Acer",
            model_series="Acer Enterprise Series-0295",
            chassis_form_factor="Ultrabook 14-inch" if 295 % 3 == 0 else "Workstation 16-inch" if 295 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (295 % 35),
            ram_standard="DDR5-5600" if 295 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 295 % 2 == 0 else 32,
            nvme_slots=2 if 295 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 295 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (295 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 295 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00296(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00296."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00296",
            brand="MSI",
            model_series="MSI Enterprise Series-0296",
            chassis_form_factor="Ultrabook 14-inch" if 296 % 3 == 0 else "Workstation 16-inch" if 296 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (296 % 35),
            ram_standard="DDR5-5600" if 296 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 296 % 2 == 0 else 32,
            nvme_slots=2 if 296 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 296 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (296 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 296 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00297(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00297."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00297",
            brand="Razer",
            model_series="Razer Enterprise Series-0297",
            chassis_form_factor="Ultrabook 14-inch" if 297 % 3 == 0 else "Workstation 16-inch" if 297 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (297 % 35),
            ram_standard="DDR5-5600" if 297 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 297 % 2 == 0 else 32,
            nvme_slots=2 if 297 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 297 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (297 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 297 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00298(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00298."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00298",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0298",
            chassis_form_factor="Ultrabook 14-inch" if 298 % 3 == 0 else "Workstation 16-inch" if 298 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (298 % 35),
            ram_standard="DDR5-5600" if 298 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 298 % 2 == 0 else 32,
            nvme_slots=2 if 298 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 298 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (298 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 298 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00299(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00299."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00299",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0299",
            chassis_form_factor="Ultrabook 14-inch" if 299 % 3 == 0 else "Workstation 16-inch" if 299 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (299 % 35),
            ram_standard="DDR5-5600" if 299 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 299 % 2 == 0 else 32,
            nvme_slots=2 if 299 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 299 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (299 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 299 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00300(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00300."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00300",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0300",
            chassis_form_factor="Ultrabook 14-inch" if 300 % 3 == 0 else "Workstation 16-inch" if 300 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (300 % 35),
            ram_standard="DDR5-5600" if 300 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 300 % 2 == 0 else 32,
            nvme_slots=2 if 300 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 300 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (300 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 300 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00301(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00301."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00301",
            brand="Dell",
            model_series="Dell Enterprise Series-0301",
            chassis_form_factor="Ultrabook 14-inch" if 301 % 3 == 0 else "Workstation 16-inch" if 301 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (301 % 35),
            ram_standard="DDR5-5600" if 301 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 301 % 2 == 0 else 32,
            nvme_slots=2 if 301 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 301 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (301 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 301 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00302(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00302."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00302",
            brand="HP",
            model_series="HP Enterprise Series-0302",
            chassis_form_factor="Ultrabook 14-inch" if 302 % 3 == 0 else "Workstation 16-inch" if 302 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (302 % 35),
            ram_standard="DDR5-5600" if 302 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 302 % 2 == 0 else 32,
            nvme_slots=2 if 302 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 302 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (302 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 302 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00303(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00303."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00303",
            brand="Apple",
            model_series="Apple Enterprise Series-0303",
            chassis_form_factor="Ultrabook 14-inch" if 303 % 3 == 0 else "Workstation 16-inch" if 303 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (303 % 35),
            ram_standard="DDR5-5600" if 303 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 303 % 2 == 0 else 32,
            nvme_slots=2 if 303 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 303 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (303 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 303 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00304(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00304."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00304",
            brand="Asus",
            model_series="Asus Enterprise Series-0304",
            chassis_form_factor="Ultrabook 14-inch" if 304 % 3 == 0 else "Workstation 16-inch" if 304 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (304 % 35),
            ram_standard="DDR5-5600" if 304 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 304 % 2 == 0 else 32,
            nvme_slots=2 if 304 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 304 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (304 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 304 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00305(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00305."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00305",
            brand="Acer",
            model_series="Acer Enterprise Series-0305",
            chassis_form_factor="Ultrabook 14-inch" if 305 % 3 == 0 else "Workstation 16-inch" if 305 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (305 % 35),
            ram_standard="DDR5-5600" if 305 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 305 % 2 == 0 else 32,
            nvme_slots=2 if 305 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 305 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (305 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 305 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00306(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00306."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00306",
            brand="MSI",
            model_series="MSI Enterprise Series-0306",
            chassis_form_factor="Ultrabook 14-inch" if 306 % 3 == 0 else "Workstation 16-inch" if 306 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (306 % 35),
            ram_standard="DDR5-5600" if 306 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 306 % 2 == 0 else 32,
            nvme_slots=2 if 306 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 306 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (306 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 306 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00307(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00307."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00307",
            brand="Razer",
            model_series="Razer Enterprise Series-0307",
            chassis_form_factor="Ultrabook 14-inch" if 307 % 3 == 0 else "Workstation 16-inch" if 307 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (307 % 35),
            ram_standard="DDR5-5600" if 307 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 307 % 2 == 0 else 32,
            nvme_slots=2 if 307 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 307 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (307 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 307 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00308(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00308."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00308",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0308",
            chassis_form_factor="Ultrabook 14-inch" if 308 % 3 == 0 else "Workstation 16-inch" if 308 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (308 % 35),
            ram_standard="DDR5-5600" if 308 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 308 % 2 == 0 else 32,
            nvme_slots=2 if 308 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 308 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (308 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 308 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00309(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00309."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00309",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0309",
            chassis_form_factor="Ultrabook 14-inch" if 309 % 3 == 0 else "Workstation 16-inch" if 309 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (309 % 35),
            ram_standard="DDR5-5600" if 309 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 309 % 2 == 0 else 32,
            nvme_slots=2 if 309 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 309 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (309 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 309 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00310(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00310."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00310",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0310",
            chassis_form_factor="Ultrabook 14-inch" if 310 % 3 == 0 else "Workstation 16-inch" if 310 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (310 % 35),
            ram_standard="DDR5-5600" if 310 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 310 % 2 == 0 else 32,
            nvme_slots=2 if 310 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 310 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (310 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 310 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00311(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00311."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00311",
            brand="Dell",
            model_series="Dell Enterprise Series-0311",
            chassis_form_factor="Ultrabook 14-inch" if 311 % 3 == 0 else "Workstation 16-inch" if 311 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (311 % 35),
            ram_standard="DDR5-5600" if 311 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 311 % 2 == 0 else 32,
            nvme_slots=2 if 311 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 311 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (311 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 311 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00312(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00312."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00312",
            brand="HP",
            model_series="HP Enterprise Series-0312",
            chassis_form_factor="Ultrabook 14-inch" if 312 % 3 == 0 else "Workstation 16-inch" if 312 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (312 % 35),
            ram_standard="DDR5-5600" if 312 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 312 % 2 == 0 else 32,
            nvme_slots=2 if 312 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 312 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (312 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 312 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00313(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00313."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00313",
            brand="Apple",
            model_series="Apple Enterprise Series-0313",
            chassis_form_factor="Ultrabook 14-inch" if 313 % 3 == 0 else "Workstation 16-inch" if 313 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (313 % 35),
            ram_standard="DDR5-5600" if 313 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 313 % 2 == 0 else 32,
            nvme_slots=2 if 313 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 313 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (313 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 313 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00314(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00314."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00314",
            brand="Asus",
            model_series="Asus Enterprise Series-0314",
            chassis_form_factor="Ultrabook 14-inch" if 314 % 3 == 0 else "Workstation 16-inch" if 314 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (314 % 35),
            ram_standard="DDR5-5600" if 314 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 314 % 2 == 0 else 32,
            nvme_slots=2 if 314 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 314 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (314 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 314 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00315(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00315."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00315",
            brand="Acer",
            model_series="Acer Enterprise Series-0315",
            chassis_form_factor="Ultrabook 14-inch" if 315 % 3 == 0 else "Workstation 16-inch" if 315 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (315 % 35),
            ram_standard="DDR5-5600" if 315 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 315 % 2 == 0 else 32,
            nvme_slots=2 if 315 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 315 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (315 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 315 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00316(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00316."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00316",
            brand="MSI",
            model_series="MSI Enterprise Series-0316",
            chassis_form_factor="Ultrabook 14-inch" if 316 % 3 == 0 else "Workstation 16-inch" if 316 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (316 % 35),
            ram_standard="DDR5-5600" if 316 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 316 % 2 == 0 else 32,
            nvme_slots=2 if 316 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 316 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (316 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 316 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00317(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00317."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00317",
            brand="Razer",
            model_series="Razer Enterprise Series-0317",
            chassis_form_factor="Ultrabook 14-inch" if 317 % 3 == 0 else "Workstation 16-inch" if 317 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (317 % 35),
            ram_standard="DDR5-5600" if 317 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 317 % 2 == 0 else 32,
            nvme_slots=2 if 317 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 317 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (317 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 317 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00318(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00318."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00318",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0318",
            chassis_form_factor="Ultrabook 14-inch" if 318 % 3 == 0 else "Workstation 16-inch" if 318 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (318 % 35),
            ram_standard="DDR5-5600" if 318 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 318 % 2 == 0 else 32,
            nvme_slots=2 if 318 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 318 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (318 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 318 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00319(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00319."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00319",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0319",
            chassis_form_factor="Ultrabook 14-inch" if 319 % 3 == 0 else "Workstation 16-inch" if 319 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (319 % 35),
            ram_standard="DDR5-5600" if 319 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 319 % 2 == 0 else 32,
            nvme_slots=2 if 319 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 319 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (319 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 319 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00320(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00320."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00320",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0320",
            chassis_form_factor="Ultrabook 14-inch" if 320 % 3 == 0 else "Workstation 16-inch" if 320 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (320 % 35),
            ram_standard="DDR5-5600" if 320 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 320 % 2 == 0 else 32,
            nvme_slots=2 if 320 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 320 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (320 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 320 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00321(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00321."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00321",
            brand="Dell",
            model_series="Dell Enterprise Series-0321",
            chassis_form_factor="Ultrabook 14-inch" if 321 % 3 == 0 else "Workstation 16-inch" if 321 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (321 % 35),
            ram_standard="DDR5-5600" if 321 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 321 % 2 == 0 else 32,
            nvme_slots=2 if 321 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 321 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (321 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 321 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00322(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00322."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00322",
            brand="HP",
            model_series="HP Enterprise Series-0322",
            chassis_form_factor="Ultrabook 14-inch" if 322 % 3 == 0 else "Workstation 16-inch" if 322 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (322 % 35),
            ram_standard="DDR5-5600" if 322 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 322 % 2 == 0 else 32,
            nvme_slots=2 if 322 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 322 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (322 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 322 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00323(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00323."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00323",
            brand="Apple",
            model_series="Apple Enterprise Series-0323",
            chassis_form_factor="Ultrabook 14-inch" if 323 % 3 == 0 else "Workstation 16-inch" if 323 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (323 % 35),
            ram_standard="DDR5-5600" if 323 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 323 % 2 == 0 else 32,
            nvme_slots=2 if 323 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 323 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (323 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 323 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00324(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00324."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00324",
            brand="Asus",
            model_series="Asus Enterprise Series-0324",
            chassis_form_factor="Ultrabook 14-inch" if 324 % 3 == 0 else "Workstation 16-inch" if 324 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (324 % 35),
            ram_standard="DDR5-5600" if 324 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 324 % 2 == 0 else 32,
            nvme_slots=2 if 324 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 324 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (324 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 324 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00325(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00325."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00325",
            brand="Acer",
            model_series="Acer Enterprise Series-0325",
            chassis_form_factor="Ultrabook 14-inch" if 325 % 3 == 0 else "Workstation 16-inch" if 325 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (325 % 35),
            ram_standard="DDR5-5600" if 325 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 325 % 2 == 0 else 32,
            nvme_slots=2 if 325 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 325 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (325 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 325 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00326(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00326."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00326",
            brand="MSI",
            model_series="MSI Enterprise Series-0326",
            chassis_form_factor="Ultrabook 14-inch" if 326 % 3 == 0 else "Workstation 16-inch" if 326 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (326 % 35),
            ram_standard="DDR5-5600" if 326 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 326 % 2 == 0 else 32,
            nvme_slots=2 if 326 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 326 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (326 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 326 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00327(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00327."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00327",
            brand="Razer",
            model_series="Razer Enterprise Series-0327",
            chassis_form_factor="Ultrabook 14-inch" if 327 % 3 == 0 else "Workstation 16-inch" if 327 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (327 % 35),
            ram_standard="DDR5-5600" if 327 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 327 % 2 == 0 else 32,
            nvme_slots=2 if 327 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 327 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (327 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 327 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00328(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00328."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00328",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0328",
            chassis_form_factor="Ultrabook 14-inch" if 328 % 3 == 0 else "Workstation 16-inch" if 328 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (328 % 35),
            ram_standard="DDR5-5600" if 328 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 328 % 2 == 0 else 32,
            nvme_slots=2 if 328 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 328 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (328 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 328 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00329(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00329."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00329",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0329",
            chassis_form_factor="Ultrabook 14-inch" if 329 % 3 == 0 else "Workstation 16-inch" if 329 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (329 % 35),
            ram_standard="DDR5-5600" if 329 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 329 % 2 == 0 else 32,
            nvme_slots=2 if 329 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 329 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (329 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 329 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00330(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00330."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00330",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0330",
            chassis_form_factor="Ultrabook 14-inch" if 330 % 3 == 0 else "Workstation 16-inch" if 330 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (330 % 35),
            ram_standard="DDR5-5600" if 330 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 330 % 2 == 0 else 32,
            nvme_slots=2 if 330 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 330 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (330 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 330 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00331(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00331."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00331",
            brand="Dell",
            model_series="Dell Enterprise Series-0331",
            chassis_form_factor="Ultrabook 14-inch" if 331 % 3 == 0 else "Workstation 16-inch" if 331 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (331 % 35),
            ram_standard="DDR5-5600" if 331 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 331 % 2 == 0 else 32,
            nvme_slots=2 if 331 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 331 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (331 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 331 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00332(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00332."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00332",
            brand="HP",
            model_series="HP Enterprise Series-0332",
            chassis_form_factor="Ultrabook 14-inch" if 332 % 3 == 0 else "Workstation 16-inch" if 332 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (332 % 35),
            ram_standard="DDR5-5600" if 332 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 332 % 2 == 0 else 32,
            nvme_slots=2 if 332 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 332 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (332 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 332 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00333(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00333."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00333",
            brand="Apple",
            model_series="Apple Enterprise Series-0333",
            chassis_form_factor="Ultrabook 14-inch" if 333 % 3 == 0 else "Workstation 16-inch" if 333 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (333 % 35),
            ram_standard="DDR5-5600" if 333 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 333 % 2 == 0 else 32,
            nvme_slots=2 if 333 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 333 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (333 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 333 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00334(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00334."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00334",
            brand="Asus",
            model_series="Asus Enterprise Series-0334",
            chassis_form_factor="Ultrabook 14-inch" if 334 % 3 == 0 else "Workstation 16-inch" if 334 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (334 % 35),
            ram_standard="DDR5-5600" if 334 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 334 % 2 == 0 else 32,
            nvme_slots=2 if 334 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 334 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (334 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 334 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00335(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00335."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00335",
            brand="Acer",
            model_series="Acer Enterprise Series-0335",
            chassis_form_factor="Ultrabook 14-inch" if 335 % 3 == 0 else "Workstation 16-inch" if 335 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (335 % 35),
            ram_standard="DDR5-5600" if 335 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 335 % 2 == 0 else 32,
            nvme_slots=2 if 335 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 335 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (335 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 335 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00336(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00336."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00336",
            brand="MSI",
            model_series="MSI Enterprise Series-0336",
            chassis_form_factor="Ultrabook 14-inch" if 336 % 3 == 0 else "Workstation 16-inch" if 336 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (336 % 35),
            ram_standard="DDR5-5600" if 336 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 336 % 2 == 0 else 32,
            nvme_slots=2 if 336 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 336 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (336 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 336 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00337(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00337."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00337",
            brand="Razer",
            model_series="Razer Enterprise Series-0337",
            chassis_form_factor="Ultrabook 14-inch" if 337 % 3 == 0 else "Workstation 16-inch" if 337 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (337 % 35),
            ram_standard="DDR5-5600" if 337 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 337 % 2 == 0 else 32,
            nvme_slots=2 if 337 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 337 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (337 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 337 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00338(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00338."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00338",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0338",
            chassis_form_factor="Ultrabook 14-inch" if 338 % 3 == 0 else "Workstation 16-inch" if 338 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (338 % 35),
            ram_standard="DDR5-5600" if 338 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 338 % 2 == 0 else 32,
            nvme_slots=2 if 338 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 338 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (338 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 338 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00339(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00339."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00339",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0339",
            chassis_form_factor="Ultrabook 14-inch" if 339 % 3 == 0 else "Workstation 16-inch" if 339 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (339 % 35),
            ram_standard="DDR5-5600" if 339 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 339 % 2 == 0 else 32,
            nvme_slots=2 if 339 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 339 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (339 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 339 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00340(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00340."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00340",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0340",
            chassis_form_factor="Ultrabook 14-inch" if 340 % 3 == 0 else "Workstation 16-inch" if 340 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (340 % 35),
            ram_standard="DDR5-5600" if 340 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 340 % 2 == 0 else 32,
            nvme_slots=2 if 340 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 340 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (340 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 340 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00341(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00341."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00341",
            brand="Dell",
            model_series="Dell Enterprise Series-0341",
            chassis_form_factor="Ultrabook 14-inch" if 341 % 3 == 0 else "Workstation 16-inch" if 341 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (341 % 35),
            ram_standard="DDR5-5600" if 341 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 341 % 2 == 0 else 32,
            nvme_slots=2 if 341 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 341 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (341 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 341 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00342(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00342."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00342",
            brand="HP",
            model_series="HP Enterprise Series-0342",
            chassis_form_factor="Ultrabook 14-inch" if 342 % 3 == 0 else "Workstation 16-inch" if 342 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (342 % 35),
            ram_standard="DDR5-5600" if 342 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 342 % 2 == 0 else 32,
            nvme_slots=2 if 342 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 342 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (342 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 342 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00343(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00343."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00343",
            brand="Apple",
            model_series="Apple Enterprise Series-0343",
            chassis_form_factor="Ultrabook 14-inch" if 343 % 3 == 0 else "Workstation 16-inch" if 343 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (343 % 35),
            ram_standard="DDR5-5600" if 343 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 343 % 2 == 0 else 32,
            nvme_slots=2 if 343 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 343 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (343 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 343 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00344(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00344."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00344",
            brand="Asus",
            model_series="Asus Enterprise Series-0344",
            chassis_form_factor="Ultrabook 14-inch" if 344 % 3 == 0 else "Workstation 16-inch" if 344 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (344 % 35),
            ram_standard="DDR5-5600" if 344 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 344 % 2 == 0 else 32,
            nvme_slots=2 if 344 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 344 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (344 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 344 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00345(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00345."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00345",
            brand="Acer",
            model_series="Acer Enterprise Series-0345",
            chassis_form_factor="Ultrabook 14-inch" if 345 % 3 == 0 else "Workstation 16-inch" if 345 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (345 % 35),
            ram_standard="DDR5-5600" if 345 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 345 % 2 == 0 else 32,
            nvme_slots=2 if 345 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 345 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (345 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 345 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00346(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00346."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00346",
            brand="MSI",
            model_series="MSI Enterprise Series-0346",
            chassis_form_factor="Ultrabook 14-inch" if 346 % 3 == 0 else "Workstation 16-inch" if 346 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (346 % 35),
            ram_standard="DDR5-5600" if 346 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 346 % 2 == 0 else 32,
            nvme_slots=2 if 346 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 346 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (346 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 346 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00347(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00347."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00347",
            brand="Razer",
            model_series="Razer Enterprise Series-0347",
            chassis_form_factor="Ultrabook 14-inch" if 347 % 3 == 0 else "Workstation 16-inch" if 347 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (347 % 35),
            ram_standard="DDR5-5600" if 347 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 347 % 2 == 0 else 32,
            nvme_slots=2 if 347 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 347 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (347 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 347 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00348(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00348."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00348",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0348",
            chassis_form_factor="Ultrabook 14-inch" if 348 % 3 == 0 else "Workstation 16-inch" if 348 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (348 % 35),
            ram_standard="DDR5-5600" if 348 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 348 % 2 == 0 else 32,
            nvme_slots=2 if 348 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 348 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (348 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 348 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00349(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00349."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00349",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0349",
            chassis_form_factor="Ultrabook 14-inch" if 349 % 3 == 0 else "Workstation 16-inch" if 349 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (349 % 35),
            ram_standard="DDR5-5600" if 349 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 349 % 2 == 0 else 32,
            nvme_slots=2 if 349 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 349 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (349 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 349 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00350(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00350."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00350",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0350",
            chassis_form_factor="Ultrabook 14-inch" if 350 % 3 == 0 else "Workstation 16-inch" if 350 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (350 % 35),
            ram_standard="DDR5-5600" if 350 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 350 % 2 == 0 else 32,
            nvme_slots=2 if 350 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 350 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (350 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 350 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00351(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00351."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00351",
            brand="Dell",
            model_series="Dell Enterprise Series-0351",
            chassis_form_factor="Ultrabook 14-inch" if 351 % 3 == 0 else "Workstation 16-inch" if 351 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (351 % 35),
            ram_standard="DDR5-5600" if 351 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 351 % 2 == 0 else 32,
            nvme_slots=2 if 351 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 351 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (351 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 351 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00352(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00352."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00352",
            brand="HP",
            model_series="HP Enterprise Series-0352",
            chassis_form_factor="Ultrabook 14-inch" if 352 % 3 == 0 else "Workstation 16-inch" if 352 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (352 % 35),
            ram_standard="DDR5-5600" if 352 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 352 % 2 == 0 else 32,
            nvme_slots=2 if 352 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 352 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (352 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 352 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00353(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00353."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00353",
            brand="Apple",
            model_series="Apple Enterprise Series-0353",
            chassis_form_factor="Ultrabook 14-inch" if 353 % 3 == 0 else "Workstation 16-inch" if 353 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (353 % 35),
            ram_standard="DDR5-5600" if 353 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 353 % 2 == 0 else 32,
            nvme_slots=2 if 353 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 353 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (353 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 353 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00354(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00354."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00354",
            brand="Asus",
            model_series="Asus Enterprise Series-0354",
            chassis_form_factor="Ultrabook 14-inch" if 354 % 3 == 0 else "Workstation 16-inch" if 354 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (354 % 35),
            ram_standard="DDR5-5600" if 354 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 354 % 2 == 0 else 32,
            nvme_slots=2 if 354 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 354 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (354 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 354 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00355(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00355."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00355",
            brand="Acer",
            model_series="Acer Enterprise Series-0355",
            chassis_form_factor="Ultrabook 14-inch" if 355 % 3 == 0 else "Workstation 16-inch" if 355 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (355 % 35),
            ram_standard="DDR5-5600" if 355 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 355 % 2 == 0 else 32,
            nvme_slots=2 if 355 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 355 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (355 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 355 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00356(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00356."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00356",
            brand="MSI",
            model_series="MSI Enterprise Series-0356",
            chassis_form_factor="Ultrabook 14-inch" if 356 % 3 == 0 else "Workstation 16-inch" if 356 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (356 % 35),
            ram_standard="DDR5-5600" if 356 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 356 % 2 == 0 else 32,
            nvme_slots=2 if 356 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 356 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (356 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 356 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00357(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00357."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00357",
            brand="Razer",
            model_series="Razer Enterprise Series-0357",
            chassis_form_factor="Ultrabook 14-inch" if 357 % 3 == 0 else "Workstation 16-inch" if 357 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (357 % 35),
            ram_standard="DDR5-5600" if 357 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 357 % 2 == 0 else 32,
            nvme_slots=2 if 357 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 357 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (357 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 357 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00358(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00358."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00358",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0358",
            chassis_form_factor="Ultrabook 14-inch" if 358 % 3 == 0 else "Workstation 16-inch" if 358 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (358 % 35),
            ram_standard="DDR5-5600" if 358 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 358 % 2 == 0 else 32,
            nvme_slots=2 if 358 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 358 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (358 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 358 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00359(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00359."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00359",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0359",
            chassis_form_factor="Ultrabook 14-inch" if 359 % 3 == 0 else "Workstation 16-inch" if 359 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (359 % 35),
            ram_standard="DDR5-5600" if 359 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 359 % 2 == 0 else 32,
            nvme_slots=2 if 359 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 359 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (359 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 359 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00360(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00360."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00360",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0360",
            chassis_form_factor="Ultrabook 14-inch" if 360 % 3 == 0 else "Workstation 16-inch" if 360 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (360 % 35),
            ram_standard="DDR5-5600" if 360 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 360 % 2 == 0 else 32,
            nvme_slots=2 if 360 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 360 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (360 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 360 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00361(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00361."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00361",
            brand="Dell",
            model_series="Dell Enterprise Series-0361",
            chassis_form_factor="Ultrabook 14-inch" if 361 % 3 == 0 else "Workstation 16-inch" if 361 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (361 % 35),
            ram_standard="DDR5-5600" if 361 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 361 % 2 == 0 else 32,
            nvme_slots=2 if 361 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 361 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (361 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 361 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00362(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00362."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00362",
            brand="HP",
            model_series="HP Enterprise Series-0362",
            chassis_form_factor="Ultrabook 14-inch" if 362 % 3 == 0 else "Workstation 16-inch" if 362 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (362 % 35),
            ram_standard="DDR5-5600" if 362 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 362 % 2 == 0 else 32,
            nvme_slots=2 if 362 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 362 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (362 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 362 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00363(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00363."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00363",
            brand="Apple",
            model_series="Apple Enterprise Series-0363",
            chassis_form_factor="Ultrabook 14-inch" if 363 % 3 == 0 else "Workstation 16-inch" if 363 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (363 % 35),
            ram_standard="DDR5-5600" if 363 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 363 % 2 == 0 else 32,
            nvme_slots=2 if 363 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 363 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (363 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 363 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00364(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00364."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00364",
            brand="Asus",
            model_series="Asus Enterprise Series-0364",
            chassis_form_factor="Ultrabook 14-inch" if 364 % 3 == 0 else "Workstation 16-inch" if 364 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (364 % 35),
            ram_standard="DDR5-5600" if 364 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 364 % 2 == 0 else 32,
            nvme_slots=2 if 364 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 364 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (364 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 364 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00365(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00365."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00365",
            brand="Acer",
            model_series="Acer Enterprise Series-0365",
            chassis_form_factor="Ultrabook 14-inch" if 365 % 3 == 0 else "Workstation 16-inch" if 365 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (365 % 35),
            ram_standard="DDR5-5600" if 365 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 365 % 2 == 0 else 32,
            nvme_slots=2 if 365 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 365 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (365 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 365 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00366(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00366."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00366",
            brand="MSI",
            model_series="MSI Enterprise Series-0366",
            chassis_form_factor="Ultrabook 14-inch" if 366 % 3 == 0 else "Workstation 16-inch" if 366 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (366 % 35),
            ram_standard="DDR5-5600" if 366 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 366 % 2 == 0 else 32,
            nvme_slots=2 if 366 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 366 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (366 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 366 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00367(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00367."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00367",
            brand="Razer",
            model_series="Razer Enterprise Series-0367",
            chassis_form_factor="Ultrabook 14-inch" if 367 % 3 == 0 else "Workstation 16-inch" if 367 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (367 % 35),
            ram_standard="DDR5-5600" if 367 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 367 % 2 == 0 else 32,
            nvme_slots=2 if 367 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 367 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (367 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 367 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00368(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00368."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00368",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0368",
            chassis_form_factor="Ultrabook 14-inch" if 368 % 3 == 0 else "Workstation 16-inch" if 368 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (368 % 35),
            ram_standard="DDR5-5600" if 368 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 368 % 2 == 0 else 32,
            nvme_slots=2 if 368 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 368 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (368 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 368 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00369(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00369."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00369",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0369",
            chassis_form_factor="Ultrabook 14-inch" if 369 % 3 == 0 else "Workstation 16-inch" if 369 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (369 % 35),
            ram_standard="DDR5-5600" if 369 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 369 % 2 == 0 else 32,
            nvme_slots=2 if 369 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 369 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (369 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 369 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00370(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00370."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00370",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0370",
            chassis_form_factor="Ultrabook 14-inch" if 370 % 3 == 0 else "Workstation 16-inch" if 370 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (370 % 35),
            ram_standard="DDR5-5600" if 370 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 370 % 2 == 0 else 32,
            nvme_slots=2 if 370 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 370 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (370 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 370 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00371(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00371."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00371",
            brand="Dell",
            model_series="Dell Enterprise Series-0371",
            chassis_form_factor="Ultrabook 14-inch" if 371 % 3 == 0 else "Workstation 16-inch" if 371 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (371 % 35),
            ram_standard="DDR5-5600" if 371 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 371 % 2 == 0 else 32,
            nvme_slots=2 if 371 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 371 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (371 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 371 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00372(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00372."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00372",
            brand="HP",
            model_series="HP Enterprise Series-0372",
            chassis_form_factor="Ultrabook 14-inch" if 372 % 3 == 0 else "Workstation 16-inch" if 372 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (372 % 35),
            ram_standard="DDR5-5600" if 372 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 372 % 2 == 0 else 32,
            nvme_slots=2 if 372 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 372 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (372 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 372 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00373(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00373."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00373",
            brand="Apple",
            model_series="Apple Enterprise Series-0373",
            chassis_form_factor="Ultrabook 14-inch" if 373 % 3 == 0 else "Workstation 16-inch" if 373 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (373 % 35),
            ram_standard="DDR5-5600" if 373 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 373 % 2 == 0 else 32,
            nvme_slots=2 if 373 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 373 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (373 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 373 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00374(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00374."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00374",
            brand="Asus",
            model_series="Asus Enterprise Series-0374",
            chassis_form_factor="Ultrabook 14-inch" if 374 % 3 == 0 else "Workstation 16-inch" if 374 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (374 % 35),
            ram_standard="DDR5-5600" if 374 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 374 % 2 == 0 else 32,
            nvme_slots=2 if 374 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 374 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (374 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 374 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00375(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00375."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00375",
            brand="Acer",
            model_series="Acer Enterprise Series-0375",
            chassis_form_factor="Ultrabook 14-inch" if 375 % 3 == 0 else "Workstation 16-inch" if 375 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (375 % 35),
            ram_standard="DDR5-5600" if 375 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 375 % 2 == 0 else 32,
            nvme_slots=2 if 375 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 375 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (375 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 375 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00376(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00376."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00376",
            brand="MSI",
            model_series="MSI Enterprise Series-0376",
            chassis_form_factor="Ultrabook 14-inch" if 376 % 3 == 0 else "Workstation 16-inch" if 376 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (376 % 35),
            ram_standard="DDR5-5600" if 376 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 376 % 2 == 0 else 32,
            nvme_slots=2 if 376 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 376 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (376 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 376 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00377(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00377."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00377",
            brand="Razer",
            model_series="Razer Enterprise Series-0377",
            chassis_form_factor="Ultrabook 14-inch" if 377 % 3 == 0 else "Workstation 16-inch" if 377 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (377 % 35),
            ram_standard="DDR5-5600" if 377 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 377 % 2 == 0 else 32,
            nvme_slots=2 if 377 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 377 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (377 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 377 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00378(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00378."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00378",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0378",
            chassis_form_factor="Ultrabook 14-inch" if 378 % 3 == 0 else "Workstation 16-inch" if 378 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (378 % 35),
            ram_standard="DDR5-5600" if 378 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 378 % 2 == 0 else 32,
            nvme_slots=2 if 378 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 378 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (378 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 378 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00379(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00379."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00379",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0379",
            chassis_form_factor="Ultrabook 14-inch" if 379 % 3 == 0 else "Workstation 16-inch" if 379 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (379 % 35),
            ram_standard="DDR5-5600" if 379 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 379 % 2 == 0 else 32,
            nvme_slots=2 if 379 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 379 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (379 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 379 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00380(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00380."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00380",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0380",
            chassis_form_factor="Ultrabook 14-inch" if 380 % 3 == 0 else "Workstation 16-inch" if 380 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (380 % 35),
            ram_standard="DDR5-5600" if 380 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 380 % 2 == 0 else 32,
            nvme_slots=2 if 380 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 380 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (380 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 380 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00381(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00381."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00381",
            brand="Dell",
            model_series="Dell Enterprise Series-0381",
            chassis_form_factor="Ultrabook 14-inch" if 381 % 3 == 0 else "Workstation 16-inch" if 381 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (381 % 35),
            ram_standard="DDR5-5600" if 381 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 381 % 2 == 0 else 32,
            nvme_slots=2 if 381 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 381 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (381 % 12) * 0.1, 2),
            msrp_usd=Decimal("999.00"),
            warranty_tier="3-Year ProSupport Plus" if 381 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00382(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00382."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00382",
            brand="HP",
            model_series="HP Enterprise Series-0382",
            chassis_form_factor="Ultrabook 14-inch" if 382 % 3 == 0 else "Workstation 16-inch" if 382 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (382 % 35),
            ram_standard="DDR5-5600" if 382 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 382 % 2 == 0 else 32,
            nvme_slots=2 if 382 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 382 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (382 % 12) * 0.1, 2),
            msrp_usd=Decimal("1099.00"),
            warranty_tier="3-Year ProSupport Plus" if 382 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00383(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00383."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00383",
            brand="Apple",
            model_series="Apple Enterprise Series-0383",
            chassis_form_factor="Ultrabook 14-inch" if 383 % 3 == 0 else "Workstation 16-inch" if 383 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (383 % 35),
            ram_standard="DDR5-5600" if 383 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 383 % 2 == 0 else 32,
            nvme_slots=2 if 383 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 383 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (383 % 12) * 0.1, 2),
            msrp_usd=Decimal("1199.00"),
            warranty_tier="3-Year ProSupport Plus" if 383 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00384(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00384."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00384",
            brand="Asus",
            model_series="Asus Enterprise Series-0384",
            chassis_form_factor="Ultrabook 14-inch" if 384 % 3 == 0 else "Workstation 16-inch" if 384 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (384 % 35),
            ram_standard="DDR5-5600" if 384 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 384 % 2 == 0 else 32,
            nvme_slots=2 if 384 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 384 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (384 % 12) * 0.1, 2),
            msrp_usd=Decimal("1299.00"),
            warranty_tier="3-Year ProSupport Plus" if 384 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00385(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00385."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00385",
            brand="Acer",
            model_series="Acer Enterprise Series-0385",
            chassis_form_factor="Ultrabook 14-inch" if 385 % 3 == 0 else "Workstation 16-inch" if 385 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (385 % 35),
            ram_standard="DDR5-5600" if 385 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 385 % 2 == 0 else 32,
            nvme_slots=2 if 385 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 385 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (385 % 12) * 0.1, 2),
            msrp_usd=Decimal("1399.00"),
            warranty_tier="3-Year ProSupport Plus" if 385 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00386(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00386."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00386",
            brand="MSI",
            model_series="MSI Enterprise Series-0386",
            chassis_form_factor="Ultrabook 14-inch" if 386 % 3 == 0 else "Workstation 16-inch" if 386 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (386 % 35),
            ram_standard="DDR5-5600" if 386 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 386 % 2 == 0 else 32,
            nvme_slots=2 if 386 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 386 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (386 % 12) * 0.1, 2),
            msrp_usd=Decimal("1499.00"),
            warranty_tier="3-Year ProSupport Plus" if 386 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00387(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00387."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00387",
            brand="Razer",
            model_series="Razer Enterprise Series-0387",
            chassis_form_factor="Ultrabook 14-inch" if 387 % 3 == 0 else "Workstation 16-inch" if 387 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-10",
            tdp_watts=28 + (387 % 35),
            ram_standard="DDR5-5600" if 387 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 387 % 2 == 0 else 32,
            nvme_slots=2 if 387 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 387 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (387 % 12) * 0.1, 2),
            msrp_usd=Decimal("1599.00"),
            warranty_tier="3-Year ProSupport Plus" if 387 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00388(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00388."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00388",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0388",
            chassis_form_factor="Ultrabook 14-inch" if 388 % 3 == 0 else "Workstation 16-inch" if 388 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-11",
            tdp_watts=28 + (388 % 35),
            ram_standard="DDR5-5600" if 388 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 388 % 2 == 0 else 32,
            nvme_slots=2 if 388 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 388 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (388 % 12) * 0.1, 2),
            msrp_usd=Decimal("1699.00"),
            warranty_tier="3-Year ProSupport Plus" if 388 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00389(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00389."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00389",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0389",
            chassis_form_factor="Ultrabook 14-inch" if 389 % 3 == 0 else "Workstation 16-inch" if 389 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-12",
            tdp_watts=28 + (389 % 35),
            ram_standard="DDR5-5600" if 389 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 389 % 2 == 0 else 32,
            nvme_slots=2 if 389 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 389 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (389 % 12) * 0.1, 2),
            msrp_usd=Decimal("1799.00"),
            warranty_tier="3-Year ProSupport Plus" if 389 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00390(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00390."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00390",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0390",
            chassis_form_factor="Ultrabook 14-inch" if 390 % 3 == 0 else "Workstation 16-inch" if 390 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-13",
            tdp_watts=28 + (390 % 35),
            ram_standard="DDR5-5600" if 390 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 390 % 2 == 0 else 32,
            nvme_slots=2 if 390 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 390 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (390 % 12) * 0.1, 2),
            msrp_usd=Decimal("1899.00"),
            warranty_tier="3-Year ProSupport Plus" if 390 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00391(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-DEL-00391."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-DEL-00391",
            brand="Dell",
            model_series="Dell Enterprise Series-0391",
            chassis_form_factor="Ultrabook 14-inch" if 391 % 3 == 0 else "Workstation 16-inch" if 391 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-14",
            tdp_watts=28 + (391 % 35),
            ram_standard="DDR5-5600" if 391 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 391 % 2 == 0 else 32,
            nvme_slots=2 if 391 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 391 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (391 % 12) * 0.1, 2),
            msrp_usd=Decimal("1999.00"),
            warranty_tier="3-Year ProSupport Plus" if 391 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00392(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-HP-00392."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-HP-00392",
            brand="HP",
            model_series="HP Enterprise Series-0392",
            chassis_form_factor="Ultrabook 14-inch" if 392 % 3 == 0 else "Workstation 16-inch" if 392 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-1",
            tdp_watts=28 + (392 % 35),
            ram_standard="DDR5-5600" if 392 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 392 % 2 == 0 else 32,
            nvme_slots=2 if 392 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 392 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (392 % 12) * 0.1, 2),
            msrp_usd=Decimal("2099.00"),
            warranty_tier="3-Year ProSupport Plus" if 392 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00393(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-APP-00393."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-APP-00393",
            brand="Apple",
            model_series="Apple Enterprise Series-0393",
            chassis_form_factor="Ultrabook 14-inch" if 393 % 3 == 0 else "Workstation 16-inch" if 393 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-2",
            tdp_watts=28 + (393 % 35),
            ram_standard="DDR5-5600" if 393 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 393 % 2 == 0 else 32,
            nvme_slots=2 if 393 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 393 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (393 % 12) * 0.1, 2),
            msrp_usd=Decimal("2199.00"),
            warranty_tier="3-Year ProSupport Plus" if 393 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00394(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ASU-00394."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ASU-00394",
            brand="Asus",
            model_series="Asus Enterprise Series-0394",
            chassis_form_factor="Ultrabook 14-inch" if 394 % 3 == 0 else "Workstation 16-inch" if 394 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-3",
            tdp_watts=28 + (394 % 35),
            ram_standard="DDR5-5600" if 394 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 394 % 2 == 0 else 32,
            nvme_slots=2 if 394 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 394 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (394 % 12) * 0.1, 2),
            msrp_usd=Decimal("2299.00"),
            warranty_tier="3-Year ProSupport Plus" if 394 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00395(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-ACE-00395."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-ACE-00395",
            brand="Acer",
            model_series="Acer Enterprise Series-0395",
            chassis_form_factor="Ultrabook 14-inch" if 395 % 3 == 0 else "Workstation 16-inch" if 395 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-4",
            tdp_watts=28 + (395 % 35),
            ram_standard="DDR5-5600" if 395 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 395 % 2 == 0 else 32,
            nvme_slots=2 if 395 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 395 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (395 % 12) * 0.1, 2),
            msrp_usd=Decimal("2399.00"),
            warranty_tier="3-Year ProSupport Plus" if 395 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00396(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MSI-00396."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MSI-00396",
            brand="MSI",
            model_series="MSI Enterprise Series-0396",
            chassis_form_factor="Ultrabook 14-inch" if 396 % 3 == 0 else "Workstation 16-inch" if 396 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-5",
            tdp_watts=28 + (396 % 35),
            ram_standard="DDR5-5600" if 396 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 396 % 2 == 0 else 32,
            nvme_slots=2 if 396 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 396 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (396 % 12) * 0.1, 2),
            msrp_usd=Decimal("2499.00"),
            warranty_tier="3-Year ProSupport Plus" if 396 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00397(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-RAZ-00397."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-RAZ-00397",
            brand="Razer",
            model_series="Razer Enterprise Series-0397",
            chassis_form_factor="Ultrabook 14-inch" if 397 % 3 == 0 else "Workstation 16-inch" if 397 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-6",
            tdp_watts=28 + (397 % 35),
            ram_standard="DDR5-5600" if 397 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 397 % 2 == 0 else 32,
            nvme_slots=2 if 397 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 397 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (397 % 12) * 0.1, 2),
            msrp_usd=Decimal("2599.00"),
            warranty_tier="3-Year ProSupport Plus" if 397 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00398(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-MIC-00398."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-MIC-00398",
            brand="Microsoft",
            model_series="Microsoft Enterprise Series-0398",
            chassis_form_factor="Ultrabook 14-inch" if 398 % 3 == 0 else "Workstation 16-inch" if 398 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-7",
            tdp_watts=28 + (398 % 35),
            ram_standard="DDR5-5600" if 398 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 398 % 2 == 0 else 32,
            nvme_slots=2 if 398 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 398 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (398 % 12) * 0.1, 2),
            msrp_usd=Decimal("2699.00"),
            warranty_tier="3-Year ProSupport Plus" if 398 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00399(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-SAM-00399."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-SAM-00399",
            brand="Samsung",
            model_series="Samsung Enterprise Series-0399",
            chassis_form_factor="Ultrabook 14-inch" if 399 % 3 == 0 else "Workstation 16-inch" if 399 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-8",
            tdp_watts=28 + (399 % 35),
            ram_standard="DDR5-5600" if 399 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 399 % 2 == 0 else 32,
            nvme_slots=2 if 399 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 399 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (399 % 12) * 0.1, 2),
            msrp_usd=Decimal("2799.00"),
            warranty_tier="3-Year ProSupport Plus" if 399 % 2 == 0 else "1-Year Depot Warranty",
        )

    @classmethod
    def get_hardware_profile_00400(cls) -> LaptopHardwareCatalogItem:
        """Returns hardware specifications for SKU-LEN-00400."""
        return LaptopHardwareCatalogItem(
            sku_code="SKU-LEN-00400",
            brand="Lenovo",
            model_series="Lenovo Enterprise Series-0400",
            chassis_form_factor="Ultrabook 14-inch" if 400 % 3 == 0 else "Workstation 16-inch" if 400 % 3 == 1 else "Business 15.6-inch",
            cpu_codename=f"Intel Core Ultra 7 155H - Gen-9",
            tdp_watts=28 + (400 % 35),
            ram_standard="DDR5-5600" if 400 % 2 == 0 else "LPDDR5X-7467",
            max_ram_gb=64 if 400 % 2 == 0 else 32,
            nvme_slots=2 if 400 % 3 == 0 else 1,
            display_panel="OLED 2.8K 120Hz" if 400 % 4 == 0 else "IPS FHD+ 400nits LowPower",
            weight_kg=round(1.25 + (400 % 12) * 0.1, 2),
            msrp_usd=Decimal("899.00"),
            warranty_tier="3-Year ProSupport Plus" if 400 % 2 == 0 else "1-Year Depot Warranty",
        )
