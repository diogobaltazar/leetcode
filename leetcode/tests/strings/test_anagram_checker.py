"""
Tests for the anagram_checker exercise.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from exercises.strings.anagram_checker import are_anagrams

class TestAnagramChecker(unittest.TestCase):
    """Test cases for the are_anagrams function."""

    def test_valid_anagrams(self):
        """Test with valid anagrams."""
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertTrue(are_anagrams("anagram", "nagaram"))
        self.assertTrue(are_anagrams("triangle", "integral"))
        self.assertTrue(are_anagrams("debit card", "bad credit"))

    def test_invalid_anagrams(self):
        """Test with strings that are not anagrams."""
        self.assertFalse(are_anagrams("hello", "world"))
        self.assertFalse(are_anagrams("rat", "car"))
        self.assertFalse(are_anagrams("abc", "def"))

    def test_different_lengths(self):
        """Test with strings of different lengths."""
        self.assertFalse(are_anagrams("abc", "abcd"))
        self.assertFalse(are_anagrams("longer", "short"))

    def test_same_letters_different_counts(self):
        """Test with strings that have the same letters but different counts."""
        # These are actually anagrams (both have 2 'a's and 1 'b')
        # self.assertFalse(are_anagrams("aab", "aba"))
        # Corrected test cases
        self.assertFalse(are_anagrams("aab", "ab"))
        self.assertFalse(are_anagrams("hello", "helo"))

    def test_empty_strings(self):
        """Test with empty strings."""
        self.assertTrue(are_anagrams("", ""))

    def test_single_character(self):
        """Test with single-character strings."""
        self.assertTrue(are_anagrams("a", "a"))
        self.assertFalse(are_anagrams("a", "b"))

    def test_case_sensitivity(self):
        """Test that the function is case-sensitive."""
        self.assertFalse(are_anagrams("Ab", "ab"))
        self.assertFalse(are_anagrams("listen", "Silent"))

    def test_special_characters(self):
        """Test with strings containing special characters and spaces."""
        self.assertTrue(are_anagrams("a!b@c#", "c#b@a!"))
        self.assertTrue(are_anagrams("race car", "car race"))

    def test_repeated_characters(self):
        """Test with strings containing repeated characters."""
        self.assertTrue(are_anagrams("aaabbb", "ababab"))
        self.assertFalse(are_anagrams("aaabbb", "aabbbc"))

if __name__ == "__main__":
    unittest.main()
