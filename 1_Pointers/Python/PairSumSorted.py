"""
Pair Sum - Sorted

Given a sorted array of integers and a target value, return the indexes of the
two numbers whose sum equals the target. If no such pair exists, return an
empty list.

Example:
Input: nums = [1, 2, 3, 4, 6], target = 6
Output: [1, 3]
"""

from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    i = 0
    j = len(nums)-1
    while i < j:
        val = nums[i] + nums[j]
        if (val < target):
            i += 1
        elif val > target:
            j -= 1
        else:
            return [i, j]
    return []


def run_test(nums: List[int], target: int, expected: List[int], test_name: str) -> None:
    print(test_name)
    print("nums     = " + str(nums))
    print("target   = " + str(target))
    print("expected = " + str(expected))

    try:
        actual = pair_sum_sorted(nums, target)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 2, 3, 4, 6], 6, [1, 3], "Test 1")
    run_test([2, 3, 4, 7], 7, [0, 2], "Test 2")
    run_test([1, 2], 3, [0, 1], "Test 3")
    run_test([1, 2, 3], 10, [], "Test 4")
    run_test([-5, -2, 0, 3, 8], 1, [1, 3], "Test 5")
