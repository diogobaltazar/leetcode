"""
Tests for the power exercise.
"""
import unittest
import sys
import os
# Use Python's built-in pow function
import builtins

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.math.power import power

class TestPower(unittest.TestCase):
    """Test cases for the power function."""

    def test_positive_exponents(self):
        """Test with positive exponents."""
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(3, 3), 27)
        self.assertEqual(power(5, 4), 625)
        self.assertEqual(power(10, 3), 1000)

    def test_zero_exponent(self):
        """Test with exponent of zero."""
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 0), 1)  # Mathematically undefined, but commonly defined as 1
        self.assertEqual(power(-10, 0), 1)

    def test_negative_exponents(self):
        """Test with negative exponents."""
        self.assertAlmostEqual(power(2, -2), 0.25)
        self.assertAlmostEqual(power(10, -1), 0.1)
        self.assertAlmostEqual(power(4, -2), 0.0625)

    def test_base_cases(self):
        """Test with base cases."""
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(1, 100), 1)
        self.assertEqual(power(-1, 2), 1)
        self.assertEqual(power(-1, 3), -1)

    def test_fractional_base(self):
        """Test with fractional base."""
        self.assertAlmostEqual(power(0.5, 2), 0.25)
        self.assertAlmostEqual(power(2.5, 2), 6.25)

    def test_large_exponents(self):
        """Test with large exponents to verify logarithmic performance."""
        # Compare with Python's built-in power function for large exponents
        self.assertAlmostEqual(power(1.001, 1000), builtins.pow(1.001, 1000), places=5)
        self.assertEqual(power(2, 20), 1048576)

if __name__ == "__main__":
    unittest.main()
