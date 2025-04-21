"""
Tests for the find_duplicates exercise.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.arrays.find_duplicates import has_duplicates_sorting, has_duplicates_hashset

class TestFindDuplicates(unittest.TestCase):
    """Test cases for the duplicate detection functions."""
    
    def test_no_duplicates(self):
        """Test with arrays that have no duplicates."""
        self.assertFalse(has_duplicates_sorting([]))
        self.assertFalse(has_duplicates_sorting([1]))
        self.assertFalse(has_duplicates_sorting([1, 2, 3, 4, 5]))
        
        self.assertFalse(has_duplicates_hashset([]))
        self.assertFalse(has_duplicates_hashset([1]))
        self.assertFalse(has_duplicates_hashset([1, 2, 3, 4, 5]))
    
    def test_with_duplicates(self):
        """Test with arrays that have duplicates."""
        self.assertTrue(has_duplicates_sorting([1, 1]))
        self.assertTrue(has_duplicates_sorting([1, 2, 3, 1]))
        self.assertTrue(has_duplicates_sorting([1, 2, 2, 3, 4, 5]))
        
        self.assertTrue(has_duplicates_hashset([1, 1]))
        self.assertTrue(has_duplicates_hashset([1, 2, 3, 1]))
        self.assertTrue(has_duplicates_hashset([1, 2, 2, 3, 4, 5]))
    
    def test_multiple_duplicates(self):
        """Test with arrays that have multiple duplicates."""
        self.assertTrue(has_duplicates_sorting([1, 2, 3, 1, 2, 3]))
        self.assertTrue(has_duplicates_sorting([1, 1, 1, 1]))
        
        self.assertTrue(has_duplicates_hashset([1, 2, 3, 1, 2, 3]))
        self.assertTrue(has_duplicates_hashset([1, 1, 1, 1]))
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertFalse(has_duplicates_sorting([-1, -2, -3]))
        self.assertTrue(has_duplicates_sorting([-1, -2, -1]))
        
        self.assertFalse(has_duplicates_hashset([-1, -2, -3]))
        self.assertTrue(has_duplicates_hashset([-1, -2, -1]))
    
    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers."""
        self.assertFalse(has_duplicates_sorting([-1, 0, 1]))
        self.assertTrue(has_duplicates_sorting([-1, 0, 1, -1]))
        
        self.assertFalse(has_duplicates_hashset([-1, 0, 1]))
        self.assertTrue(has_duplicates_hashset([-1, 0, 1, -1]))
    
    def test_consistency(self):
        """Test that both implementations give the same results."""
        test_cases = [
            [],
            [1],
            [1, 2, 3],
            [1, 1],
            [1, 2, 3, 1],
            [-1, -2, -3],
            [-1, -2, -1]
        ]
        
        for arr in test_cases:
            self.assertEqual(
                has_duplicates_sorting(arr[:]),  # Use a copy to avoid side effects
                has_duplicates_hashset(arr),
                f"Inconsistent results for {arr}"
            )

if __name__ == "__main__":
    unittest.main()
