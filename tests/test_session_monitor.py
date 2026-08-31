from django.test import TestCase
from core.services.session_monitor import SecuritySessionMonitor


class SessionSecurityTestCase(TestCase):
    def test_local_ip_safe(self):
        res = SecuritySessionMonitor.inspect_session_fingerprint("user-1", "127.0.0.1", "127.0.0.1", "Mozilla/5.0")
        self.assertEqual(res["risk_level"], "LOW")
        self.assertFalse(res["require_2fa_prompt"])

    def test_ip_change_anomaly(self):
        res = SecuritySessionMonitor.inspect_session_fingerprint("user-1", "203.0.113.45", "198.51.100.22", "Mozilla/5.0")
        self.assertEqual(res["risk_level"], "HIGH")
        self.assertTrue(res["require_2fa_prompt"])
