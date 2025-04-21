"""
Exercise: Implement Merge Sort

Problem Description:
Implement the merge sort algorithm to sort an array of integers in ascending order.

Examples:
- Input: [5, 2, 4, 6, 1, 3]
  Output: [1, 2, 3, 4, 5, 6]
- Input: [5, 1, 1, 2, 0, 0]
  Output: [0, 0, 1, 1, 2, 5]
- Input: []
  Output: []

Complexity:
- Time Complexity: O(n log n) where n is the length of the array
- Space Complexity: O(n) for the temporary arrays used during merging
"""
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using the merge sort algorithm.
    
    Args:
        arr: An array of integers
        
    Returns:
        A new sorted array
        
    Complexity:
        - Time: O(n log n) where n is the length of the array
        - Space: O(n) for the temporary arrays used during merging
    """
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursion creates O(log n) levels
    right = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        left: First sorted array
        right: Second sorted array
        
    Returns:
        A new sorted array containing all elements from both input arrays
        
    Complexity:
        - Time: O(n) where n is the total number of elements in both arrays
        - Space: O(n) for the result array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
