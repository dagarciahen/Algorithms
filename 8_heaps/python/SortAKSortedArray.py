"""
Sort a K-Sorted Array
Medium

Given an integer array where each element is at most k positions away from its
sorted position, sort the array in a non-decreasing order.

Example:
Input: nums = [5, 1, 9, 4, 7, 10], k = 2
Output: [1, 4, 5, 7, 9, 10]
"""


def sort_k_sorted_array(nums, k):
    raise NotImplementedError()


def run_test(nums, k, expected, test_name):
    print(test_name)
    print("nums     = " + str(nums))
    print("k        = " + str(k))
    print("expected = " + str(expected))

    try:
        actual = sort_k_sorted_array(nums, k)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([5, 1, 9, 4, 7, 10], 2, [1, 4, 5, 7, 9, 10], "Test 1")
    run_test([3, 2, 1], 2, [1, 2, 3], "Test 2")
    run_test([1], 0, [1], "Test 3")
    run_test([6, 5, 3, 2, 8, 10, 9], 3, [2, 3, 5, 6, 8, 9, 10], "Test 4")
    run_test([10, 9, 8, 7, 4, 70, 60, 50], 4, [4, 7, 8, 9, 10, 50, 60, 70], "Test 5")
