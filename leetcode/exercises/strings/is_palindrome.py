"""
# Statement

Given a string, s, return TRUE if it is a palindrome; otherwise, return FALSE.
A phrase is considered a palindrome if it reads the same backward as forward after converting all uppercase letters to lowercase and removing any characters that are not letters or numbers. Only alphanumeric characters (letters and digits) are taken into account.

Constraints:

- 1≤ s.length ≤ 3000
- s consists only of printable ASCII characters.
"""
def is_palindrome(s: str) -> bool:
  left, right = 0, len(s) - 1

  while left < right:
      # skip all non-alphas to the left
      while left < right and not s[left].isalnum():
        left += 1

      # skip all non-alphas to the right
      while left < right and not s[right].isalnum():
        right -= 1

      # compare chars
      if s[left].lower() != s[right].lower():
        return False

      # move to the next char pair if the previous was valid
      left += 1
      right -= 1

  return True


def main() -> None:
    """Entry point for ad hoc debugging from VS Code."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Check whether one or more provided strings are palindromes",
    )
    parser.add_argument(
        "cases",
        nargs="*",
        default=["racecar"],
        help="Strings to check (defaults to ['racecar'] if none provided)",
    )
    args = parser.parse_args()

    for case in args.cases:
        print(f"{case!r}: {is_palindrome(case)}")


if __name__ == "__main__":
    main()
