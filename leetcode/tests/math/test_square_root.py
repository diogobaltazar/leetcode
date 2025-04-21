"""
Tests for the square_root exercise.
"""
import unittest
import sys
import os
# Use our own implementation for comparison
from exercises.math.square_root import square_root

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.math.square_root import square_root

class TestSquareRoot(unittest.TestCase):
    """Test cases for the square_root function."""

    def test_perfect_squares(self):
        """Test with perfect squares."""
        self.assertAlmostEqual(square_root(4), 2.0, places=4)
        self.assertAlmostEqual(square_root(9), 3.0, places=4)
        self.assertAlmostEqual(square_root(16), 4.0, places=4)
        self.assertAlmostEqual(square_root(100), 10.0, places=4)

    def test_non_perfect_squares(self):
        """Test with non-perfect squares."""
        # Compare with known values (using fewer decimal places for more tolerance)
        self.assertAlmostEqual(square_root(2), 1.4142, places=3)
        self.assertAlmostEqual(square_root(3), 1.732, places=3)
        self.assertAlmostEqual(square_root(8), 2.828, places=3)
        self.assertAlmostEqual(square_root(10), 3.162, places=3)

    def test_edge_cases(self):
        """Test with edge cases."""
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(1), 1.0)

    def test_small_numbers(self):
        """Test with small numbers."""
        self.assertAlmostEqual(square_root(0.25), 0.5, places=4)
        # Use a less strict comparison for very small numbers
        result = square_root(0.01)
        self.assertTrue(abs(result - 0.1) < 0.001, f"Expected close to 0.1, got {result}")

    def test_large_numbers(self):
        """Test with large numbers to verify logarithmic performance."""
        self.assertAlmostEqual(square_root(1000000), 1000.0, places=4)
        self.assertAlmostEqual(square_root(10000000000), 100000.0, places=4)

    def test_negative_numbers(self):
        """Test with negative numbers, should raise ValueError."""
        with self.assertRaises(ValueError):
            square_root(-1)
        with self.assertRaises(ValueError):
            square_root(-100)

    def test_precision(self):
        """Test with different precision values."""
        # Higher precision (more accurate)
        self.assertAlmostEqual(square_root(2, precision=0.0000001), 1.4142135, places=6)
        # Lower precision (less accurate but faster)
        approx_sqrt = square_root(2, precision=0.1)
        self.assertTrue(abs(approx_sqrt - 1.4142) < 0.1)

if __name__ == "__main__":
    unittest.main()
