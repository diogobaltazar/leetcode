"""
Exercise: Binary Search in a Sorted Array

Problem Description:
Given a sorted array of integers and a target value, find the index of the target
in the array. If the target is not found, return -1.

Examples:
- Input: arr = [1, 2, 3, 4, 5], target = 3
  Output: 2
- Input: arr = [1, 2, 3, 4, 5], target = 6
  Output: -1
- Input: arr = [-5, -2, 0, 1, 5, 10], target = 5
  Output: 4
- Input: arr = [], target = 1
  Output: -1

Complexity:
- Time Complexity: O(log n) where n is the length of the array
- Space Complexity: O(1) as we only use a constant amount of extra space

Advantages:
- Extremely efficient for large datasets - much faster than linear search O(n)
- Reduces the search space by half in each step
- Works well for frequently accessed data (like database indices)
- Can be implemented iteratively (constant space) or recursively
- Foundation for many other algorithms and data structures
- Optimal for searching in sorted arrays
"""
from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """
    Perform binary search to find the target value in a sorted array.

    Args:
        arr: A sorted array of integers
        target: The value to search for

    Returns:
        The index of the target if found, otherwise -1

    Complexity:
        - Time: O(log n) where n is the length of the array
        - Space: O(1) constant extra space
    """
    left, right = 0, len(arr) - 1

    while left <= right:  # This loop runs O(log n) times
        mid = (left + right) // 2

        # Check if target is found
        if arr[mid] == target:
            return mid

        # Eliminate half of the search space
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found
