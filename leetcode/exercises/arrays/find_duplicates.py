"""
Exercise: Find Duplicates in an Array

Problem Description:
Determine if an array contains any duplicate elements.

Examples:
- Input: [1, 2, 3, 1]
  Output: True
- Input: [1, 2, 3, 4]
  Output: False
- Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
  Output: True

Complexity:
- Time Complexity: Varies by implementation (see below)
- Space Complexity: Varies by implementation (see below)
"""
from typing import List


def has_duplicates_sorting(arr: List[int]) -> bool:
    """
    Check if an array contains duplicates using sorting.
    
    Args:
        arr: An array of integers
        
    Returns:
        True if the array contains duplicates, False otherwise
        
    Complexity:
        - Time: O(n log n) for sorting
        - Space: O(1) if sorting in place (or O(n) if creating a copy)
    """
    # Make a copy to avoid modifying the original array
    sorted_arr = sorted(arr)
    
    # Check adjacent elements in the sorted array
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == sorted_arr[i - 1]:
            return True
    
    return False


def has_duplicates_hashset(arr: List[int]) -> bool:
    """
    Check if an array contains duplicates using a hash set.
    
    Args:
        arr: An array of integers
        
    Returns:
        True if the array contains duplicates, False otherwise
        
    Complexity:
        - Time: O(n) where n is the length of the array
        - Space: O(n) for the hash set
    """
    seen = set()
    
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    
    return False
