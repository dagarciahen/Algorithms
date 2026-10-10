"""
Find the Median From Two Sorted Arrays

Given two sorted integer arrays, find their median value as if they were
merged into a single sorted sequence.

Example 1:
Input: nums1 = [0, 2, 5, 6, 8], nums2 = [1, 3, 7]
Output: 4.0

Example 2:
Input: nums1 = [0, 2, 5, 6, 8], nums2 = [1, 3, 7, 9]
Output: 5.0

Constraints:
At least one of the input arrays will contain an element.
"""


def find_median_sorted_arrays(nums1, nums2):
    raise NotImplementedError()


def run_test(nums1, nums2, expected, test_name):
    print(test_name)
    print("nums1    = " + str(nums1))
    print("nums2    = " + str(nums2))
    print("expected = " + str(expected))

    try:
        actual = find_median_sorted_arrays(nums1, nums2)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([0, 2, 5, 6, 8], [1, 3, 7], 4.0, "Test 1")
    run_test([0, 2, 5, 6, 8], [1, 3, 7, 9], 5.0, "Test 2")
    run_test([1, 2], [3, 4], 2.5, "Test 3")
    run_test([], [7], 7.0, "Test 4")
    run_test([2], [], 2.0, "Test 5")
