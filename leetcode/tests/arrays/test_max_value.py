"""
Tests for the max_value exercise.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.arrays.max_value import find_max_value

class TestMaxValue(unittest.TestCase):
    """Test cases for the find_max_value function."""

    def test_positive_numbers(self):
        """Test with a list of positive numbers."""
        self.assertEqual(find_max_value([1, 3, 2, 5, 4]), 5)
        self.assertEqual(find_max_value([10, 20, 30, 40, 50]), 50)
        self.assertEqual(find_max_value([7]), 7)

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(find_max_value([-1, -5, -2, -10]), -1)
        self.assertEqual(find_max_value([-100, -200, -50, -300]), -50)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers."""
        self.assertEqual(find_max_value([-10, 5, 0, -3, 8]), 8)
        self.assertEqual(find_max_value([-5, -10, 0, -15]), 0)

    def test_floats(self):
        """Test with a list of floating-point numbers."""
        self.assertEqual(find_max_value([1.5, 2.5, 3.5, 2.0]), 3.5)
        self.assertEqual(find_max_value([-1.5, -2.5, -0.5]), -0.5)

    def test_empty_list(self):
        """Test with an empty list, should raise ValueError."""
        with self.assertRaises(ValueError):
            find_max_value([])

    def test_duplicate_values(self):
        """Test with a list containing duplicate values."""
        self.assertEqual(find_max_value([5, 5, 5, 5]), 5)
        self.assertEqual(find_max_value([1, 5, 5, 3, 5]), 5)

if __name__ == "__main__":
    unittest.main()
