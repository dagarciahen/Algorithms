"""
First and Last Occurrences of a Number

Given an array of integers sorted in non-decreasing order, return the first
and last indexes of a target number. If the target is not found, return [-1, -1].

Example:
Input: nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], target = 4
Output: [3, 5]
"""


def find_first_and_last_occurrence(nums, target):
    raise NotImplementedError()


def run_test(nums, target, expected, test_name):
    print(test_name)
    print("nums     = " + str(nums))
    print("target   = " + str(target))
    print("expected = " + str(expected))

    try:
        actual = find_first_and_last_occurrence(nums, target)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], 4, [3, 5], "Test 1")
    run_test([1, 1, 1, 1, 1], 1, [0, 4], "Test 2")
    run_test([1, 2, 3, 5, 6, 7], 4, [-1, -1], "Test 3")
    run_test([2], 2, [0, 0], "Test 4")
    run_test([], 3, [-1, -1], "Test 5")
