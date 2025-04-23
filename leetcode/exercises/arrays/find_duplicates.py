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

Advantages:
- Demonstrates space-time tradeoff with two different implementations
- Hash set approach provides optimal O(n) time complexity
- Sorting approach requires less memory when sorting in place
- Common interview problem that tests understanding of data structures
- Practical application in data validation and integrity checking
- Can be extended to find all duplicates or count occurrences
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
    sorted_arr = sorted(arr) # O(n log n)

    # Check adjacent elements in the sorted array
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == sorted_arr[i - 1]:
            return True

    return False


def has_duplicates_hashset(arr: List[int]) -> bool:
    """
    Check if an array contains duplicates using a hash set.

    About Hashsets

        1. Uniqueness: A hash set only stores unique values. If you try to add a duplicate, it won't change the set.
        2. Fast Operations: The most important operations (add, remove, lookup) are typically O(1) on average, meaning they take constant time regardless of the size of the set.
        3. Unordered: Elements in a hash set are not stored in any particular order.
        4. Hash Function: Internally, it uses a hash function to convert each element to a unique index in an array, allowing for fast lookups.

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
