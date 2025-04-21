"""
Tests for the permutations exercise.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.arrays.permutations import all_permutations

class TestPermutations(unittest.TestCase):
    """Test cases for the all_permutations function."""
    
    def test_empty_array(self):
        """Test with an empty array."""
        self.assertEqual(all_permutations([]), [[]])
    
    def test_single_element(self):
        """Test with a single-element array."""
        self.assertEqual(all_permutations([1]), [[1]])
    
    def test_two_elements(self):
        """Test with a two-element array."""
        result = all_permutations([1, 2])
        self.assertEqual(len(result), 2)
        self.assertIn([1, 2], result)
        self.assertIn([2, 1], result)
    
    def test_three_elements(self):
        """Test with a three-element array."""
        result = all_permutations([1, 2, 3])
        self.assertEqual(len(result), 6)  # 3! = 6
        self.assertIn([1, 2, 3], result)
        self.assertIn([1, 3, 2], result)
        self.assertIn([2, 1, 3], result)
        self.assertIn([2, 3, 1], result)
        self.assertIn([3, 1, 2], result)
        self.assertIn([3, 2, 1], result)
    
    def test_with_duplicates(self):
        """Test with duplicate elements (should still generate all permutations)."""
        result = all_permutations([1, 1, 2])
        # With duplicates, we'll get duplicate permutations
        # But the function should still generate 3! = 6 permutations
        self.assertEqual(len(result), 6)
    
    def test_factorial_growth(self):
        """Test that the number of permutations grows factorially."""
        self.assertEqual(len(all_permutations([])), 1)  # 0! = 1
        self.assertEqual(len(all_permutations([1])), 1)  # 1! = 1
        self.assertEqual(len(all_permutations([1, 2])), 2)  # 2! = 2
        self.assertEqual(len(all_permutations([1, 2, 3])), 6)  # 3! = 6
        self.assertEqual(len(all_permutations([1, 2, 3, 4])), 24)  # 4! = 24

if __name__ == "__main__":
    unittest.main()
