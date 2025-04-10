import unittest
from capacity_calculator import calculate_room_capacity

class TestRoomCapacity(unittest.TestCase):
    def test_basic_capacity(self):
        self.assertEqual(calculate_room_capacity(10, 10), 66)

    def test_custom_spacing(self):
        self.assertEqual(calculate_room_capacity(10, 10, 2), 50)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_room_capacity(-5, 10)

        with self.assertRaises(ValueError):
            calculate_room_capacity(10, -5)

        with self.assertRaises(ValueError):
            calculate_room_capacity(10, 10, -1)

if __name__ == "__main__":
    unittest.main()
