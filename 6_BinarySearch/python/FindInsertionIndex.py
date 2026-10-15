"""
Find the Insertion Index

You are given a sorted array that contains unique values, along with an integer target.

If the array contains the target value, return its index.
Otherwise, return the insertion index. This is the index where the target would be
if it were inserted in order, maintaining the sorted sequence of the array.

Example 1:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 4
Output: 2

Example 2:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 6
Output: 4
"""


def find_insertion_index(nums, target):
    i = 0
    j = len(nums)
    while i < j:
        m = i + (j-i)//2
        if nums[m] < target:
            i = m+1
        else:
            j = m
    return i


def run_test(nums, target, expected, test_name):
    print(test_name)
    print("nums     = " + str(nums))
    print("target   = " + str(target))
    print("expected = " + str(expected))

    try:
        actual = find_insertion_index(nums, target)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 2, 4, 5, 7, 8, 9], 4, 2, "Test 1")
    run_test([1, 2, 4, 5, 7, 8, 9], 6, 4, "Test 2")
    run_test([1, 3, 5, 7], 0, 0, "Test 3")
    run_test([1, 3, 5, 7], 10, 4, "Test 4")
    run_test([], 3, 0, "Test 5")
