from django.test import TestCase
from repairs.services.battery_telemetry import BatteryTelemetryEngine


class BatteryTelemetryTestCase(TestCase):
    def test_battery_analysis(self):
        res = BatteryTelemetryEngine.analyze_battery_health(5000, 4500, 120)
        self.assertEqual(res["health_pct"], 90.0)
        self.assertEqual(res["status"], "EXCELLENT")
