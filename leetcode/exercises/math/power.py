"""
Exercise: Calculate Power Using Divide and Conquer

Problem Description:
Given a base and an exponent, calculate the power (base^exponent) efficiently.

Examples:
- Input: base = 2, exponent = 10
  Output: 1024 (2^10 = 1024)
- Input: base = 3, exponent = 3
  Output: 27 (3^3 = 27)
- Input: base = 5, exponent = 0
  Output: 1 (Any number raised to 0 is 1)
- Input: base = 2, exponent = -2
  Output: 0.25 (2^-2 = 1/4 = 0.25)

Complexity:
- Time Complexity: O(log n) where n is the exponent
- Space Complexity: O(log n) due to the recursion stack
"""


def power(base: float, exponent: int) -> float:
    """
    Calculate base raised to the power of exponent using divide and conquer.
    
    Args:
        base: The base number
        exponent: The exponent (can be positive, negative, or zero)
        
    Returns:
        The result of base^exponent
        
    Complexity:
        - Time: O(log n) where n is the absolute value of the exponent
        - Space: O(log n) due to the recursion stack
    """
    # Handle negative exponents
    if exponent < 0:
        return 1 / power(base, -exponent)
    
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    # Recursive divide and conquer
    half = power(base, exponent // 2)  # O(log n) recursive calls
    
    # If exponent is even, result is half * half
    # If exponent is odd, result is half * half * base
    if exponent % 2 == 0:
        return half * half
    else:
        return half * half * base
