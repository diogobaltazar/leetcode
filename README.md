# LeetCode Exercises in Python

This repository contains Python implementations of various LeetCode exercises, along with comprehensive test cases.

## Project Structure

```
├── leetcode/
│   ├── exercises/           # All exercise implementations
│   │   ├── arrays/          # Array-related exercises
│   │   │   ├── max_value.py # Find maximum value in a list
│   │   │   └── ...
│   │   ├── strings/         # String-related exercises
│   │   ├── linked_lists/    # Linked list exercises
│   │   └── ...
│   ├── tests/               # Test cases for all exercises
│   │   ├── arrays/          # Tests for array exercises
│   │   │   ├── test_max_value.py
│   │   │   └── ...
│   │   ├── strings/         # Tests for string exercises
│   │   └── ...
│   ├── templates/           # Templates for new exercises and tests
│   │   ├── exercise_template.py
│   │   └── test_template.py
│   └── run_tests.py         # Test runner script
└── .vscode/                 # VS Code configuration
    └── settings.json        # Editor settings
```

## Exercises

### Arrays
1. **Max Value in an Unsorted List** (`leetcode/exercises/arrays/max_value.py`) - Find the maximum value in an unsorted list of numbers. [O(n)]
2. **Binary Search** (`leetcode/exercises/arrays/binary_search.py`) - Find the index of a target value in a sorted array using binary search. [O(log n)]
3. **Merge Sort** (`leetcode/exercises/arrays/merge_sort.py`) - Sort an array using the merge sort algorithm. [O(n log n)]
4. **Bubble Sort** (`leetcode/exercises/arrays/bubble_sort.py`) - Sort an array using the bubble sort algorithm. [O(n²)]
5. **Find Duplicates** (`leetcode/exercises/arrays/find_duplicates.py`) - Determine if an array contains any duplicate elements. [O(n) or O(n log n)]
6. **Permutations** (`leetcode/exercises/arrays/permutations.py`) - Generate all possible permutations of a list. [O(n!)]
7. **Median of Two Sorted Arrays** (`leetcode/exercises/arrays/median_sorted_arrays.py`) - Find the median of two sorted arrays. [O(log(min(m,n)))]

### Strings
1. **Anagram Checker** (`leetcode/exercises/strings/anagram_checker.py`) - Determine if two strings are anagrams of each other. [O(n)]

### Math
1. **Power Calculation** (`leetcode/exercises/math/power.py`) - Calculate base raised to a power using divide and conquer. [O(log n)]
2. **Square Root** (`leetcode/exercises/math/square_root.py`) - Calculate the square root of a number using binary search. [O(log n)]
3. **Fibonacci** (`leetcode/exercises/math/fibonacci.py`) - Calculate Fibonacci numbers with different implementations. [O(n) or O(2ⁿ)]

## Running Tests

You can run tests using the provided `run_tests.py` script:

```bash
# Run all tests
cd leetcode && python run_tests.py

# Run tests for a specific category
cd leetcode && python run_tests.py arrays

# Run tests for a specific exercise
cd leetcode && python run_tests.py arrays.max_value
```

Alternatively, you can use the standard unittest module:

```bash
# Run all tests
cd leetcode && python -m unittest discover -s tests

# Run tests for a specific category
cd leetcode && python -m unittest discover -s tests/arrays

# Run tests for a specific exercise
cd leetcode && python -m unittest tests/arrays/test_max_value.py
```

## Adding New Exercises

To add a new exercise:

1. Copy the template from `leetcode/templates/exercise_template.py` to the appropriate category directory under `leetcode/exercises/`
2. Copy the test template from `leetcode/templates/test_template.py` to the corresponding test directory
3. Implement the solution with proper documentation, type hints, and complexity analysis
4. Write comprehensive tests for all scenarios
5. Update this README.md with information about the new exercise

### Documentation Standards

All exercise implementations should include:

- Clear problem description
- Example inputs and outputs
- Time and space complexity analysis
- Detailed function docstrings
- Type hints

### Big O Notation

Big O notation describes the performance of an algorithm as the input size grows. From most efficient to least efficient:

#### O(1): Constant Time
- Operations that don't depend on input size
- Example: Accessing an array element by index

#### O(log n): Logarithmic Time
- Typically divide-and-conquer algorithms where the problem size is reduced by a factor in each step
- Common in algorithms that divide the search space in half each time
- Examples: Binary search, efficient power calculation, square root calculation

#### O(n): Linear Time
- Examining each element once
- Examples: Finding the maximum in an unsorted list, linear search

#### O(n log n): Linearithmic Time
- Efficient sorting algorithms
- Examples: Merge sort, quicksort, heapsort

#### O(n²): Quadratic Time
- Nested iterations
- Examples: Bubble sort, insertion sort, selection sort

#### O(2ⁿ): Exponential Time
- Solving problems by trying all combinations
- Examples: Recursive Fibonacci without memoization, generating all subsets

#### O(n!): Factorial Time
- Generating all permutations
- Examples: Brute force traveling salesman, generating all permutations

For code examples and implementations of these algorithms, see the exercises in this repository.

Example complexity documentation:

```python
"""
Complexity:
- Time Complexity: O(n) where n is the length of the input list
- Space Complexity: O(1) as we only use a single variable regardless of input size
"""
```

## Algorithmic Techniques

This repository demonstrates several important algorithmic techniques:

### Dynamic Programming

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It's applicable when:

1. **Overlapping Subproblems**: The same subproblems are solved multiple times
2. **Optimal Substructure**: An optimal solution can be constructed from optimal solutions of its subproblems

**Key Approaches**:
- **Memoization (Top-Down)**: Store results of subproblems in a cache to avoid redundant calculations
- **Tabulation (Bottom-Up)**: Solve all possible subproblems iteratively, starting from the smallest

**Example**: The Fibonacci implementation in `leetcode/exercises/math/fibonacci.py` demonstrates both the inefficient recursive approach [O(2ⁿ)] and the efficient dynamic programming approach [O(n)].

### Divide and Conquer

Divide and Conquer involves breaking a problem into smaller subproblems, solving them independently, and combining their results.

**Key Steps**:
1. **Divide**: Break the problem into smaller subproblems
2. **Conquer**: Solve the subproblems recursively
3. **Combine**: Merge the solutions of subproblems into a solution for the original problem

**Examples**:
- Binary Search (`leetcode/exercises/arrays/binary_search.py`) [O(log n)]
- Merge Sort (`leetcode/exercises/arrays/merge_sort.py`) [O(n log n)]
- Power Calculation (`leetcode/exercises/math/power.py`) [O(log n)]

### Greedy Algorithms

Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum.

**Characteristics**:
- Make the best choice at the moment without considering the future
- Generally efficient but don't always yield optimal solutions
- Work well for problems with "greedy choice property" and "optimal substructure"

### Backtracking

Backtracking is an algorithmic technique that incrementally builds candidates for solutions and abandons a candidate ("backtracks") as soon as it determines the candidate cannot lead to a valid solution.

**Example**: The Permutations implementation in `leetcode/exercises/arrays/permutations.py` [O(n!)] demonstrates backtracking.

### Space-Time Tradeoffs

Many algorithms demonstrate the fundamental tradeoff between time and space complexity:

**Examples**:
- Hash table for duplicate detection (`leetcode/exercises/arrays/find_duplicates.py`) trades space [O(n)] for time efficiency [O(n)]
- Optimized Fibonacci implementation (`leetcode/exercises/math/fibonacci.py`) shows how to reduce space complexity from O(n) to O(1)

## Statistical Concepts

This section provides mathematical definitions of common statistical measures that are often used in algorithm problems.

### Median

The **median** is the middle value of a dataset when arranged in ascending or descending order.

- For a dataset with an **odd number** of elements: The median is the middle element.
- For a dataset with an **even number** of elements: The median is the average of the two middle elements.

**Mathematical Definition**:
- For a sorted array `A` of length `n`:
  - If `n` is odd: `median = A[n/2]` (integer division)
  - If `n` is even: `median = (A[n/2 - 1] + A[n/2]) / 2`

**Example**:
- For `[1, 3, 5, 7, 9]`: The median is `5`
- For `[2, 4, 6, 8]`: The median is `(4 + 6) / 2 = 5`

**Implementation**: See `leetcode/exercises/arrays/median_sorted_arrays.py` for an efficient algorithm to find the median of two sorted arrays.

### Mean (Average)

The **mean** (or average) is the sum of all values divided by the number of values.

**Mathematical Definition**:
- For a dataset `A` with `n` elements: `mean = (A[0] + A[1] + ... + A[n-1]) / n`
- Using summation notation: `mean = (∑ A[i]) / n` for `i` from `0` to `n-1`

**Example**:
- For `[1, 3, 5, 7, 9]`: The mean is `(1 + 3 + 5 + 7 + 9) / 5 = 25 / 5 = 5`
- For `[2, 4, 6, 8]`: The mean is `(2 + 4 + 6 + 8) / 4 = 20 / 4 = 5`

### Mode

The **mode** is the value that appears most frequently in a dataset. A dataset may have one mode, multiple modes, or no mode.

**Mathematical Definition**:
- For a dataset `A`, the mode is the value `x` such that the frequency of `x` in `A` is greater than the frequency of any other value in `A`.

**Example**:
- For `[1, 2, 2, 3, 4]`: The mode is `2` (appears twice)
- For `[1, 1, 2, 2, 3, 3]`: The modes are `1`, `2`, and `3` (each appears twice)
- For `[1, 2, 3, 4]`: There is no mode (all values appear once)

### Range

The **range** is the difference between the maximum and minimum values in a dataset.

**Mathematical Definition**:
- For a dataset `A`: `range = max(A) - min(A)`

**Example**:
- For `[1, 3, 5, 7, 9]`: The range is `9 - 1 = 8`
- For `[2, 4, 6, 8]`: The range is `8 - 2 = 6`

## Practice Questions and Answers

This repository includes practice questions and answers to help you understand algorithm complexity and optimization techniques. The questions cover topics such as:

1. Time complexity analysis
2. Algorithm design
3. Optimization techniques
4. Space-time tradeoffs
5. Logarithmic complexity

For detailed questions and answers, see the implementations in the exercises directory. Each exercise includes comprehensive documentation and test cases that demonstrate the concepts.
