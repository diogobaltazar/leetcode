"""
Tests for the median_sorted_arrays exercise.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.arrays.median_sorted_arrays import find_median_sorted_arrays, find_median_sorted_arrays_simple

class TestMedianSortedArrays(unittest.TestCase):
    """Test cases for the find_median_sorted_arrays function."""

    def test_example_cases(self):
        """Test with the example cases from the problem description."""
        self.assertEqual(find_median_sorted_arrays([1, 3], [2]), 2.0)
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(find_median_sorted_arrays([], [1]), 1.0)
        self.assertEqual(find_median_sorted_arrays([2], []), 2.0)

    def test_odd_length_result(self):
        """Test with arrays that result in an odd total length."""
        self.assertEqual(find_median_sorted_arrays([1, 3, 5], [2, 4]), 3.0)
        self.assertEqual(find_median_sorted_arrays([1, 2], [3]), 2.0)
        self.assertEqual(find_median_sorted_arrays([5], [1, 2, 3, 4, 6, 7]), 4.0)

    def test_even_length_result(self):
        """Test with arrays that result in an even total length."""
        self.assertEqual(find_median_sorted_arrays([1, 2, 3], [4, 5, 6]), 3.5)
        self.assertEqual(find_median_sorted_arrays([1, 3], [2, 4]), 2.5)
        self.assertEqual(find_median_sorted_arrays([1, 2], [1, 2]), 1.5)

    def test_empty_arrays(self):
        """Test with one empty array."""
        self.assertEqual(find_median_sorted_arrays([], [1, 2, 3]), 2.0)
        self.assertEqual(find_median_sorted_arrays([1, 2, 3, 4], []), 2.5)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(find_median_sorted_arrays([-5, -3, -1], [-2, 0, 2]), -1.5)
        self.assertEqual(find_median_sorted_arrays([-1], [-3, -2]), -2.0)

    def test_duplicate_values(self):
        """Test with duplicate values across arrays."""
        self.assertEqual(find_median_sorted_arrays([1, 1, 3, 3], [1, 1, 3, 3]), 2.0)
        self.assertEqual(find_median_sorted_arrays([2, 2, 2], [2, 2, 2]), 2.0)

    def test_large_difference(self):
        """Test with arrays that have a large difference in values."""
        self.assertEqual(find_median_sorted_arrays([1, 2, 3], [100, 101, 102]), 51.5)
        self.assertEqual(find_median_sorted_arrays([-100, -99], [100, 101]), 0.5)

    def test_simple_implementation(self):
        """Test the simple implementation for comparison."""
        test_cases = [
            ([1, 3], [2]),
            ([1, 2], [3, 4]),
            ([], [1]),
            ([2], []),
            ([1, 3, 5], [2, 4]),
            ([1, 2, 3], [4, 5, 6])
        ]

        for nums1, nums2 in test_cases:
            self.assertEqual(
                find_median_sorted_arrays(nums1, nums2),
                find_median_sorted_arrays_simple(nums1, nums2),
                f"Results differ for {nums1} and {nums2}"
            )

    def test_edge_cases(self):
        """Test edge cases with very different array sizes."""
        self.assertEqual(find_median_sorted_arrays([1], [2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)
        self.assertEqual(find_median_sorted_arrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 8.0)

if __name__ == "__main__":
    unittest.main()
