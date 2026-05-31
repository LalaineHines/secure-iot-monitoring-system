import unittest

from src.sensor_data import generate_pool_data


class TestPoolSensor(unittest.TestCase):

    def test_pool_data_contains_required_fields(self):

        data = generate_pool_data()

        self.assertIn("device", data)
        self.assertIn("temperature", data)
        self.assertIn("ph", data)
        self.assertIn("timestamp", data)

    def test_pool_temperature_range(self):

        data = generate_pool_data()

        self.assertGreaterEqual(
            data["temperature"],
            70
        )

        self.assertLessEqual(
            data["temperature"],
            85
        )

    def test_pool_ph_range(self):

        data = generate_pool_data()

        self.assertGreaterEqual(
            data["ph"],
            7.0
        )

        self.assertLessEqual(
            data["ph"],
            7.8
        )


if __name__ == "__main__":
    unittest.main()