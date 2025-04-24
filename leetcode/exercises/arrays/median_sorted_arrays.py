"""
Exercise: Median of Two Sorted Arrays

Problem Description:
Given two sorted arrays nums1 and nums2 of size m and n respectively, find the median of the two sorted arrays.
The overall run time complexity should be O(log(m+n)).

Examples:
- Input: nums1 = [1, 3], nums2 = [2]
  Output: 2.0
- Input: nums1 = [1, 2], nums2 = [3, 4]
  Output: 2.5
- Input: nums1 = [], nums2 = [1]
  Output: 1.0
- Input: nums1 = [2], nums2 = []
  Output: 2.0

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m, n <= 1000
- 0 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

Complexity:
- Time Complexity: O(log(min(m,n))) where m and n are the lengths of the arrays
- Space Complexity: O(1) as we only use a constant amount of extra space

Advantages:
- Demonstrates binary search on arrays
- Efficient logarithmic time complexity
- Handles edge cases (empty arrays)
- Shows how to find a median without merging arrays
- Illustrates the concept of partitioning arrays
- Practical application in statistics and data processing

Solution mnemonic:

- 1 ensure nums1 is the smallest
- 2 x, y, low, high
- 3 while low <= high
    - 4 partition nr of elems
    - 5 partitions max, min for l, r
    - 6 if, elif, else; return (odd, even), or high=px-- or low=px++

Practice: 5

Minutes: 70
"""
from typing import List

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Find the median of two sorted arrays.

    Args:
        nums1: First sorted array
        nums2: Second sorted array

    Returns:
        The median of the two arrays

    Complexity:
        - Time: O(log(min(m,n))) where m and n are the lengths of the arrays
        - Space: O(1) constant extra space
    """
    # Ensure nums1 is the smaller array for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        # Partition the arrays
        partition_x = (low + high) // 2 # nr of elems to take from nums1
        partition_y = (x + y + 1) // 2 - partition_x # nr of elems to take from nums2

        # Get the elements around the partition
        max_x_left = float('-inf') if partition_x == 0 else nums1[partition_x - 1] # last element in left partition of nums1
        min_x_right = float('inf') if partition_x == x else nums1[partition_x] # first element in right partition of nums1

        max_y_left = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_y_right = float('inf') if partition_y == y else nums2[partition_y]

        # Check if we found the correct partition
        if max_x_left <= min_y_right and max_y_left <= min_x_right:
            # Found the right partition
            # If total length is odd, return the max of left elements
            if (x + y) % 2 != 0:
                return max(max_x_left, max_y_left)
            # If total length is even, return average of max of left and min of right
            else:
                return (max(max_x_left, max_y_left) + min(min_x_right, min_y_right)) / 2
        # Adjust the partition
        elif max_x_left > min_y_right:
            high = partition_x - 1
        else:
            low = partition_x + 1

    # If we reach here, the input arrays were not sorted
    raise ValueError("Input arrays must be sorted")


def find_median_sorted_arrays_simple(nums1: List[int], nums2: List[int]) -> float:
    """
    Find the median of two sorted arrays using a simpler but less efficient approach.
    This is provided for educational purposes to contrast with the optimal solution.

    Args:
        nums1: First sorted array
        nums2: Second sorted array

    Returns:
        The median of the two arrays

    Complexity:
        - Time: O(m+n) where m and n are the lengths of the arrays
        - Space: O(m+n) for the merged array
    """
    # Merge the arrays
    merged = []
    i = j = 0

    # Merge the two sorted arrays
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    # Find the median
    n = len(merged)
    if n % 2 == 0:
        # Even length, average of middle two elements
        return (merged[n//2 - 1] + merged[n//2]) / 2
    else:
        # Odd length, middle element
        return merged[n//2]
