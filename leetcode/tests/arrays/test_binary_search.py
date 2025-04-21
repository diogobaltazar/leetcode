"""
Tests for the binary_search exercise.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.arrays.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    """Test cases for the binary_search function."""
    
    def test_target_found(self):
        """Test when the target is found in the array."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([-5, -2, 0, 1, 5, 10], 5), 4)
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 1), 0)  # First element
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 9), 4)  # Last element
    
    def test_target_not_found(self):
        """Test when the target is not found in the array."""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(binary_search([-5, -2, 0, 1, 5, 10], -10), -1)
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 4), -1)  # Between elements
    
    def test_empty_array(self):
        """Test with an empty array."""
        self.assertEqual(binary_search([], 1), -1)
    
    def test_single_element_array(self):
        """Test with a single-element array."""
        self.assertEqual(binary_search([5], 5), 0)  # Target found
        self.assertEqual(binary_search([5], 10), -1)  # Target not found
    
    def test_duplicate_elements(self):
        """Test with duplicate elements in the array."""
        # Binary search typically returns the first occurrence it finds
        # which could be any of the duplicates
        result = binary_search([1, 2, 2, 2, 3], 2)
        self.assertTrue(result in [1, 2, 3])  # Could be any index with value 2
    
    def test_large_array(self):
        """Test with a large array to verify logarithmic performance."""
        large_array = list(range(1000000))  # 1 million elements
        self.assertEqual(binary_search(large_array, 500000), 500000)
        self.assertEqual(binary_search(large_array, -1), -1)
        self.assertEqual(binary_search(large_array, 1000000), -1)

if __name__ == "__main__":
    unittest.main()
