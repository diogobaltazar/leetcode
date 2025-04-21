"""
Exercise: Generate All Permutations

Problem Description:
Generate all possible permutations of a list of distinct integers.

Examples:
- Input: [1, 2, 3]
  Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
- Input: [0, 1]
  Output: [[0, 1], [1, 0]]
- Input: [1]
  Output: [[1]]

Complexity:
- Time Complexity: O(n!) where n is the length of the input list
- Space Complexity: O(n * n!) to store all permutations
"""
from typing import List


def all_permutations(arr: List[int]) -> List[List[int]]:
    """
    Generate all possible permutations of a list.
    
    Args:
        arr: A list of distinct integers
        
    Returns:
        A list of all possible permutations
        
    Complexity:
        - Time: O(n!) where n is the length of the input list
        - Space: O(n * n!) to store all permutations
    """
    # Base case: if the list has 0 or 1 elements, there's only one permutation
    if len(arr) <= 1:
        return [arr[:]]  # Return a copy of the list
    
    result = []
    
    # Try each element as the first element
    for i in range(len(arr)):
        # Extract current element
        current = arr[i]
        
        # Generate all permutations of the remaining elements
        remaining = arr[:i] + arr[i+1:]
        
        # For each permutation of the remaining elements,
        # add the current element at the beginning
        for p in all_permutations(remaining):
            result.append([current] + p)
    
    return result
