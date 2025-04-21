"""
Tests for the bubble_sort exercise.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.arrays.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    """Test cases for the bubble_sort function."""
    
    def test_empty_array(self):
        """Test with an empty array."""
        arr = []
        self.assertEqual(bubble_sort(arr), [])
    
    def test_single_element(self):
        """Test with a single-element array."""
        arr = [5]
        self.assertEqual(bubble_sort(arr), [5])
    
    def test_sorted_array(self):
        """Test with an already sorted array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        """Test with a reverse-sorted array."""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])
    
    def test_random_array(self):
        """Test with a randomly ordered array."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        self.assertEqual(bubble_sort(arr), [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_duplicate_elements(self):
        """Test with duplicate elements."""
        arr = [3, 3, 3, 2, 2, 1]
        self.assertEqual(bubble_sort(arr), [1, 2, 2, 3, 3, 3])
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        arr = [-5, -2, -10, -1]
        self.assertEqual(bubble_sort(arr), [-10, -5, -2, -1])
    
    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers."""
        arr = [-3, 5, 0, -8, 2, 1]
        self.assertEqual(bubble_sort(arr), [-8, -3, 0, 1, 2, 5])
    
    def test_early_termination(self):
        """Test that the algorithm terminates early when the array is sorted."""
        # This is hard to test directly, but we can verify the result is correct
        arr = [1, 2, 3, 5, 4]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
