"""
Here you are, neatly wrapped in markdown silk:

# 88. Merge Sorted Array

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

---

## Example 1

**Input:** `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`
**Output:** `[1,2,2,3,5,6]`
**Explanation:** The arrays we are merging are `[1,2,3]` and `[2,5,6]`.
The result of the merge is `[1,2,2,3,5,6]` with the underlined elements coming from `nums1`.

---

## Example 2

**Input:** `nums1 = [1], m = 1, nums2 = [], n = 0`
**Output:** `[1]`
**Explanation:** The arrays we are merging are `[1]` and `[]`.
The result of the merge is `[1]`.

---

## Example 3

**Input:** `nums1 = [0], m = 0, nums2 = [1], n = 1`
**Output:** `[1]`
**Explanation:** The arrays we are merging are `[]` and `[1]`.
The result of the merge is `[1]`.
Note that because `m = 0`, there are no elements in `nums1`. The `0` is only there to ensure the merge result can fit in `nums1`.

---

## Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Follow up

Can you come up with an algorithm that runs in O(m + n) time?Can you come up with an algorithm that runs in O(m + n) time?
"""
from typing import List


def merge_sorted(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    if not nums2:
        return nums1
    last_index = m - 1
    nums2_index = 0
    index = 0
    while index < n + m:
        if nums2[nums2_index] <= nums1[index]:
            _shift_one(nums1, index, last_index)
            nums1[index] = nums2[nums2_index]
            last_index += 1
            nums2_index += 1
            index += 2
        elif nums2[nums2_index] > nums1[index] and nums1[index] == 0:
            nums1[index:m+n] = nums2[nums2_index:n]
        else:
            index += 1
    return nums1

def _shift_one(nums, index, last_index):
    """inserts element in array at index  and shifts right the existing elements from index"""
    offset = 0
    for _ in range(last_index + 1 - index):
        nums[last_index + 1 - offset] = nums[last_index - offset]
        offset += 1
    nums[index] = 0


def _parse_case(raw: str):
    import argparse
    import ast

    try:
        value = ast.literal_eval(raw)
    except (SyntaxError, ValueError) as exc:
        raise argparse.ArgumentTypeError(
            "Case must be a tuple: ([nums1], m, [nums2], n)"
        ) from exc

    if not (isinstance(value, tuple) and len(value) == 4):
        raise argparse.ArgumentTypeError(
            "Each case must be a tuple of (nums1, m, nums2, n)"
        )

    nums1, m, nums2, n = value
    if not (isinstance(nums1, list) and isinstance(nums2, list)):
        raise argparse.ArgumentTypeError("nums1 and nums2 must be lists")
    if not all(isinstance(item, int) for item in nums1 + nums2):
        raise argparse.ArgumentTypeError("nums1 and nums2 must contain integers only")
    if not (isinstance(m, int) and isinstance(n, int)):
        raise argparse.ArgumentTypeError("m and n must be integers")

    return value


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Merge sorted arrays in-place inside nums1",
    )
    parser.add_argument(
        "cases",
        nargs="*",
        type=_parse_case,
        metavar="CASE",
        help="Tuples like ([1,2,3,0,0,0], 3, [2,5,6], 3)",
    )
    args = parser.parse_args()

    cases = args.cases or [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        ([1], 1, [], 0),
        ([0], 0, [1], 1),
    ]

    for nums1, m, nums2, n in cases:
        nums1_copy = nums1[:]
        result = merge_sorted(nums1_copy, m, nums2[:], n)
        print(f"nums1={nums1}, m={m}, nums2={nums2}, n={n} -> {result}")


if __name__ == "__main__":
    main()
