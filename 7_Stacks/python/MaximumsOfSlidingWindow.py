"""
Maximums of Sliding Window

There is a sliding window of size k that slides through an integer array
from left to right. Create a new array that records the largest number
found in each window as it slides through.

Example:
Input: nums = [3, 2, 4, 1, 2, 1, 1], k = 4
Output: [4, 4, 4, 2]
"""


def maximums_of_sliding_window(nums, k):
    raise NotImplementedError()


def run_test(nums, k, expected, test_name):
    print(test_name)
    print("nums     = " + str(nums))
    print("k        = " + str(k))
    print("expected = " + str(expected))

    try:
        actual = maximums_of_sliding_window(nums, k)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([3, 2, 4, 1, 2, 1, 1], 4, [4, 4, 4, 2], "Test 1")
    run_test([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7], "Test 2")
    run_test([1], 1, [1], "Test 3")
    run_test([9, 8, 7, 6], 2, [9, 8, 7], "Test 4")
    run_test([4, 4, 4, 4], 3, [4, 4], "Test 5")
