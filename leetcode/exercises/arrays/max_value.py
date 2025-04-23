"""
Exercise: Find the maximum value in an unsorted list.

Problem Description:
Given an unsorted list of numbers, find the maximum value in the list.
If the list is empty, raise a ValueError.

Examples:
- Input: [1, 3, 2, 5, 4]
  Output: 5
- Input: [-1, -5, -2, -10]
  Output: -1
- Input: []
  Output: ValueError

Complexity:
- Time Complexity: O(n) where n is the length of the input list. This is optimal for an unsorted list as we must examine every element at least once.
- Space Complexity: O(1) as we only use a single variable regardless of input size

Advantages:
- Simple and straightforward implementation
- Memory efficient (constant space complexity)
- Single-pass algorithm (only needs to traverse the list once)
- Works on any comparable elements, not just numbers
- Can be easily modified to find minimum value or both min and max
- Handles negative numbers and any valid comparable values
"""
from typing import List, TypeVar

T = TypeVar('T', int, float)

def find_max_value(numbers: List[T]) -> T:
    """
    Find the maximum value in an unsorted list of numbers.

    Args:
        numbers: An unsorted list of numbers (integers or floats)

    Returns:
        The maximum value in the list

    Raises:
        ValueError: If the input list is empty

    Complexity:
        - Time: O(n) where n is the length of the input list. This is optimal for an unsorted list.
        - Space: O(1) constant extra space (only storing one value at a time)
    """
    if not numbers:
        raise ValueError("Cannot find maximum value in an empty list")

    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
