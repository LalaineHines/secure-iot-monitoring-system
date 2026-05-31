import unittest

from src.sensor_data import generate_spa_data


class TestSpaSensor(unittest.TestCase):

    def test_spa_data_contains_required_fields(self):

        data = generate_spa_data()

        self.assertIn("device", data)
        self.assertIn("temperature", data)
        self.assertIn("chlorine", data)
        self.assertIn("timestamp", data)

    def test_temperature_range(self):

        data = generate_spa_data()

        self.assertGreaterEqual(
            data["temperature"],
            95
        )

        self.assertLessEqual(
            data["temperature"],
            105
        )

    def test_chlorine_range(self):

        data = generate_spa_data()

        self.assertGreaterEqual(
            data["chlorine"],
            1
        )

        self.assertLessEqual(
            data["chlorine"],
            4
        )


if __name__ == "__main__":
    unittest.main()