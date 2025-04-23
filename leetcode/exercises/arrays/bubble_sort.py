"""
Exercise: Implement Bubble Sort

Problem Description:
Implement the bubble sort algorithm to sort an array of integers in ascending order.

Examples:
- Input: [5, 2, 4, 6, 1, 3]
  Output: [1, 2, 3, 4, 5, 6]
- Input: [5, 1, 1, 2, 0, 0]
  Output: [0, 0, 1, 1, 2, 5]
- Input: []
  Output: []

Complexity:
- Time Complexity: O(n²) where n is the length of the array
- Space Complexity: O(1) as we sort the array in place

Advantages:
- Simple to understand and implement
- In-place sorting (requires no extra space)
- Stable sort - preserves the relative order of equal elements
- Adaptive - can detect if the array is already sorted and terminate early
- Works well for small datasets or nearly sorted arrays
- Good for educational purposes to understand sorting concepts
"""
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using the bubble sort algorithm.

    Args:
        arr: An array of integers

    Returns:
        The sorted array (sorted in place)

    Complexity:
        - Time: O(n²) where n is the length of the array
        - Space: O(1) as we sort the array in place
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize if no swaps occur in a pass
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break

    return arr
