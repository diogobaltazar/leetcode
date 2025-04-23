"""
Exercise: Check if two strings are anagrams.

Problem Description:
Given two strings, determine if they are anagrams of each other.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Examples:
- Input: s1 = "listen", s2 = "silent"
  Output: True
- Input: s1 = "hello", s2 = "world"
  Output: False
- Input: s1 = "anagram", s2 = "nagaram"
  Output: True
- Input: s1 = "rat", s2 = "car"
  Output: False
- Input: s1 = "", s2 = ""
  Output: True

Constraints:
- The strings consist of lowercase English letters.
- The comparison should be case-sensitive.

Complexity:
- Time Complexity: O(n) where n is the length of the input strings
- Space Complexity: O(1) as we only use a fixed-size counter (26 lowercase letters)

Advantages:
- Linear time complexity O(n) is optimal for this problem
- Early termination when lengths differ or invalid characters are found
- Demonstrates hash map usage for character counting
- Shows space-time tradeoff between hash map and sorting approaches
- Common interview question that tests string manipulation skills
- Practical applications in word games, cryptography, and text analysis
"""
from typing import Dict


def are_anagrams(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if the strings are anagrams, False otherwise

    Complexity:
        - Time: O(n) where n is the length of the input strings
        - Space: O(k) where k is the size of the character set
          (effectively O(1) for English alphabet)
    """
    # Quick check: if lengths are different, they can't be anagrams
    if len(s1) != len(s2):
        return False

    # Method 1: Using a character counter
    char_count: Dict[str, int] = {}

    # Count occurrences of each character in the first string
    for char in s1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Decrement counts for each character in the second string
    for char in s2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        # Don't remove the key, just check if all values are 0 at the end

    # If all counts are zero, the strings are anagrams
    return all(count == 0 for count in char_count.values())

    # Method 2: Using sorted strings (commented out)
    # return sorted(s1) == sorted(s2)  # Time: O(n log n), Space: O(n)
