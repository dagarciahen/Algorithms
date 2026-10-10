"""
Find the longest chain of consecutive numbers in an array.
Two numbers are consecutive if they have a difference of 1.

Example:
Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
Output: 4
Explanation: The longest chain of consecutive numbers is 5, 6, 7, 8.
"""


def longest_consecutive_chain(nums):
    raise NotImplementedError()


def run_test(nums, expected, test_name):
    print(test_name)
    print("nums     = " + str(nums))
    print("expected = " + str(expected))

    try:
        actual = longest_consecutive_chain(nums)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 6, 2, 5, 8, 7, 10, 3], 4, "Test 1")
    run_test([100, 4, 200, 1, 3, 2], 4, "Test 2")
    run_test([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9, "Test 3")
    run_test([10, 30, 20], 1, "Test 4")
    run_test([], 0, "Test 5")
