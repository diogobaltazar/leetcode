"""
Tests for the merge_sort exercise.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.arrays.merge_sort import merge_sort, merge

class TestMergeSort(unittest.TestCase):
    """Test cases for the merge_sort function."""
    
    def test_empty_array(self):
        """Test with an empty array."""
        self.assertEqual(merge_sort([]), [])
    
    def test_single_element(self):
        """Test with a single-element array."""
        self.assertEqual(merge_sort([5]), [5])
    
    def test_sorted_array(self):
        """Test with an already sorted array."""
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        """Test with a reverse-sorted array."""
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_random_array(self):
        """Test with a randomly ordered array."""
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_duplicate_elements(self):
        """Test with duplicate elements."""
        self.assertEqual(merge_sort([3, 3, 3, 2, 2, 1]), [1, 2, 2, 3, 3, 3])
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(merge_sort([-5, -2, -10, -1]), [-10, -5, -2, -1])
    
    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers."""
        self.assertEqual(merge_sort([-3, 5, 0, -8, 2, 1]), [-8, -3, 0, 1, 2, 5])
    
    def test_merge_function(self):
        """Test the merge function separately."""
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge([1, 2, 3], []), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
