"""
Exercise: Fibonacci Number Calculation

Problem Description:
Calculate the nth Fibonacci number. The Fibonacci sequence is defined as:
F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1

Examples:
- Input: n = 2
  Output: 1
- Input: n = 3
  Output: 2
- Input: n = 10
  Output: 55

Complexity:
- Time Complexity: Varies by implementation (see below)
- Space Complexity: Varies by implementation (see below)
"""


def fibonacci_recursive(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The nth Fibonacci number
        
    Complexity:
        - Time: O(2^n) - exponential time complexity
        - Space: O(n) due to the recursion stack
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dynamic(n: int) -> int:
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The nth Fibonacci number
        
    Complexity:
        - Time: O(n) - linear time complexity
        - Space: O(n) for the array storing all Fibonacci numbers
    """
    if n <= 1:
        return n
    
    # Create an array to store Fibonacci numbers
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1
    
    # Fill the array
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]


def fibonacci_optimized(n: int) -> int:
    """
    Calculate the nth Fibonacci number using an optimized iterative approach.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The nth Fibonacci number
        
    Complexity:
        - Time: O(n) - linear time complexity
        - Space: O(1) - constant space complexity
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    
    # Only store the last two numbers
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b
