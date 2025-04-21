"""
Tests for the fibonacci exercise.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.math.fibonacci import fibonacci_recursive, fibonacci_dynamic, fibonacci_optimized

class TestFibonacci(unittest.TestCase):
    """Test cases for the fibonacci functions."""
    
    def test_base_cases(self):
        """Test with base cases (0 and 1)."""
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_dynamic(0), 0)
        self.assertEqual(fibonacci_dynamic(1), 1)
        self.assertEqual(fibonacci_optimized(0), 0)
        self.assertEqual(fibonacci_optimized(1), 1)
    
    def test_small_inputs(self):
        """Test with small inputs."""
        self.assertEqual(fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_dynamic(2), 1)
        self.assertEqual(fibonacci_dynamic(3), 2)
        self.assertEqual(fibonacci_dynamic(5), 5)
        self.assertEqual(fibonacci_optimized(2), 1)
        self.assertEqual(fibonacci_optimized(3), 2)
        self.assertEqual(fibonacci_optimized(5), 5)
    
    def test_medium_inputs(self):
        """Test with medium-sized inputs."""
        self.assertEqual(fibonacci_dynamic(10), 55)
        self.assertEqual(fibonacci_dynamic(15), 610)
        self.assertEqual(fibonacci_optimized(10), 55)
        self.assertEqual(fibonacci_optimized(15), 610)
        # Skip recursive for medium inputs as it's too slow
    
    def test_large_inputs(self):
        """Test with large inputs (only for optimized versions)."""
        self.assertEqual(fibonacci_dynamic(30), 832040)
        self.assertEqual(fibonacci_optimized(30), 832040)
        # Skip recursive for large inputs as it's too slow
    
    def test_consistency(self):
        """Test that all implementations give the same results."""
        for n in range(10):  # Test up to n=9 for recursive
            self.assertEqual(fibonacci_recursive(n), fibonacci_dynamic(n))
            self.assertEqual(fibonacci_recursive(n), fibonacci_optimized(n))

if __name__ == "__main__":
    unittest.main()
