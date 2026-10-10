"""
Find the Target in a Rotated Sorted Array

A rotated sorted array is an array of numbers sorted in ascending order,
in which a portion of the array is moved from the beginning to the end.

Given a rotated sorted array of unique numbers, return the index of a
target value. If the target value is not present, return -1.

Example:
Input: nums = [8, 9, 1, 2, 3, 4, 5, 6, 7], target = 1
Output: 2
"""


def search_rotated_sorted_array(nums, target):
    raise NotImplementedError()


def run_test(nums, target, expected, test_name):
    print(test_name)
    print("nums     = " + str(nums))
    print("target   = " + str(target))
    print("expected = " + str(expected))

    try:
        actual = search_rotated_sorted_array(nums, target)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([8, 9, 1, 2, 3, 4, 5, 6, 7], 1, 2, "Test 1")
    run_test([4, 5, 6, 7, 0, 1, 2], 0, 4, "Test 2")
    run_test([4, 5, 6, 7, 0, 1, 2], 3, -1, "Test 3")
    run_test([1], 1, 0, "Test 4")
    run_test([6, 7, 8, 1, 2, 3, 4, 5], 5, 7, "Test 5")
