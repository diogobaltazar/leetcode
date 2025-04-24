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

Advantages:
- Guaranteed O(n log n) performance in all cases (unlike quicksort)
- Stable sort - preserves the relative order of equal elements
- Well-suited for external sorting of large datasets that don't fit in memory
- Naturally parallelizable due to its divide-and-conquer approach
- Predictable performance regardless of input data patterns

Mnemonic:

merge_sort
- 1 base cases [], [a]
- 2 mid
- 3 left, right = merge_sort left :mid, merge_sort right mid:
- 4 return merge left right

merge
- 1 i, j, result
- 2 iter i, j < len left, len right
    - 3 IF left i < right j: result append left i, i++ ELSE result append right j, j++
- 4 result extend left i: right j:
- 5 return result

Practice: 10
Minutes: 46
"""
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using the merge sort algorithm (improves over quicksort)

    Args:
        arr: An array of integers

    Returns:
        A new sorted array

    Complexity:
        - Time: O(n log n) where n is the length of the array
        - Space: O(n log n) for the temporary arrays used during merging

        n/2^k = 1
        n = 2^k
        k = log₂(n)
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

    - [2], [1, 4] -> [1, 2, 4]
    - [1, 4], [2] -> [1, 2, 4]
    - [2], [1] -> [1, 2]
    - while exhausts the i, j indixes and sorts in result
    - whatever is left is added to the result is guaranteed to be sorted

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

    # Add any remaining elements (exclusive OR left OR right)
    result.extend(left[i:])
    result.extend(right[j:])

    return result
