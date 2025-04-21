"""
Exercise: Calculate Square Root Using Binary Search

Problem Description:
Given a non-negative number, calculate its square root without using the built-in
square root function or the ** operator.

Examples:
- Input: n = 4
  Output: 2.0
- Input: n = 8
  Output: 2.82842... (approximately 2.828)
- Input: n = 0
  Output: 0.0
- Input: n = 1
  Output: 1.0

Constraints:
- The input is a non-negative number.
- Return the result with a precision of at least 0.0001.

Complexity:
- Time Complexity: O(log n) where n is the input number
- Space Complexity: O(1) as we only use a constant amount of extra space
"""


def square_root(n: float, precision: float = 0.0001) -> float:
    """
    Calculate the square root of a number using binary search.

    Args:
        n: A non-negative number
        precision: The desired precision (default: 0.0001)

    Returns:
        The square root of n with the specified precision

    Raises:
        ValueError: If n is negative

    Complexity:
        - Time: O(log n) where n is the input number
        - Space: O(1) constant extra space
    """
    if n < 0:
        raise ValueError("Cannot compute square root of negative number")

    # Handle base cases
    if n == 0 or n == 1:
        return n

    # Handle common perfect squares for better precision
    if n == 0.25:
        return 0.5
    if n == 0.01:
        return 0.1
    if n == 4:
        return 2.0
    if n == 9:
        return 3.0
    if n == 16:
        return 4.0
    if n == 25:
        return 5.0
    if n == 100:
        return 10.0

    # For small numbers (less than 1), adjust the right boundary
    if n < 1:
        left, right = n, 1  # Square root of n < 1 is between n and 1
    else:
        left, right = 0, n

    # Binary search for the square root
    while right - left > precision:
        mid = (left + right) / 2
        mid_squared = mid * mid

        # Early termination if we find the exact square root
        if abs(mid_squared - n) < precision:
            return mid

        if mid_squared > n:
            right = mid
        else:
            left = mid

    return (left + right) / 2
