import unittest

from src.dashboard_subscriber import generate_alerts


class TestAlerts(unittest.TestCase):

    def test_spa_overheating_alert(self):

        data = {
            "temperature": 110,
            "chlorine": 2
        }

        alerts = generate_alerts(
            "spa_sensor",
            data
        )

        self.assertTrue(
            any(
                "Overheating" in alert
                for alert in alerts
            )
        )

    def test_pool_ph_alert(self):

        data = {
            "temperature": 75,
            "ph": 6.5
        }

        alerts = generate_alerts(
            "pool_sensor",
            data
        )

        self.assertTrue(
            any(
                "pH" in alert
                for alert in alerts
            )
        )


if __name__ == "__main__":
    unittest.main()