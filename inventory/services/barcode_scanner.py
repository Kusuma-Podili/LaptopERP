"""
Hardware Barcode & QR Code Scanning Engine for LaptopERP.
Validates Code128, DataMatrix, and QR payloads, parsing unit serial numbers and bin codes.
"""

import re
from typing import Optional, Dict
from inventory.models import LaptopUnit
from warehouse.models import Bin


class BarcodeScanningEngine:
    @staticmethod
    def parse_scanned_barcode(raw_code: str) -> Dict[str, any]:
        cleaned = raw_code.strip()
        
        # Check if Serial Number
        if cleaned.startswith('SN-') or cleaned.startswith('BC-SN-'):
            sn = cleaned.replace('BC-', '')
            unit = LaptopUnit.objects.filter(serial_number__iexact=sn).select_related('laptop_model').first()
            if unit:
                return {
                    'type': 'SERIAL_UNIT',
                    'found': True,
                    'serial_number': unit.serial_number,
                    'model_name': unit.laptop_model.model_name,
                    'status': unit.get_status_display(),
                    'location': unit.current_location,
                }
            return {'type': 'SERIAL_UNIT', 'found': False, 'raw_code': cleaned}

        # Check if Warehouse Bin Code
        if re.match(r'^[A-Z]\d{2}-R\d{2}-S\d{2}-B\d{2}$', cleaned):
            bin_obj = Bin.objects.filter(bin_code__iexact=cleaned).select_related('zone', 'zone__warehouse').first()
            if bin_obj:
                return {
                    'type': 'WAREHOUSE_BIN',
                    'found': True,
                    'bin_code': bin_obj.bin_code,
                    'warehouse': bin_obj.zone.warehouse.name,
                    'zone': bin_obj.zone.name,
                }
            return {'type': 'WAREHOUSE_BIN', 'found': False, 'raw_code': cleaned}

        return {'type': 'UNKNOWN', 'found': False, 'raw_code': cleaned}
