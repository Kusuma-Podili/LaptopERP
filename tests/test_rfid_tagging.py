from django.test import TestCase
from inventory.services.rfid_tagging import RFIDAssetTaggingService


class RFIDTaggingTestCase(TestCase):
    def test_epc_tag_generation(self):
        res = RFIDAssetTaggingService.encode_epc_tag("SN-LEN-T14-1001", "HQ01")
        self.assertTrue(res["is_encoded"])
        self.assertEqual(len(res["epc_tag_hex"]), 24)

    def test_tag_verification(self):
        valid = RFIDAssetTaggingService.verify_tag_integrity("E28048513031534E4C454E54")
        self.assertTrue(valid)
