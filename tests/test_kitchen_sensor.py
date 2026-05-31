import unittest

from src.sensor_data import generate_kitchen_data


class TestKitchenSensor(unittest.TestCase):

    def test_kitchen_data_contains_required_fields(self):

        data = generate_kitchen_data()

        self.assertIn("device", data)
        self.assertIn("temperature", data)
        self.assertIn("humidity", data)
        self.assertIn("timestamp", data)

    def test_temperature_range(self):

        data = generate_kitchen_data()

        self.assertGreaterEqual(
            data["temperature"],
            35
        )

        self.assertLessEqual(
            data["temperature"],
            50
        )

    def test_humidity_range(self):

        data = generate_kitchen_data()

        self.assertGreaterEqual(
            data["humidity"],
            40
        )

        self.assertLessEqual(
            data["humidity"],
            75
        )


if __name__ == "__main__":
    unittest.main()