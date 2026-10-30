"""
Next Largest Number to the Right

Given an integer array nums, return an output array res where, for each value
nums[i], res[i] is the first number to the right that is larger than nums[i].
If no larger number exists to the right of nums[i], set res[i] to -1.

Example:
Input: nums = [5, 2, 4, 6, 1]
Output: [6, 4, 6, -1, -1]
"""


def next_largest_number_to_the_right(nums):
    res = [0]*len(nums)
    stack = []
    for i in range(len(nums)-1, -1, -1):
        while stack and nums[i] >= stack[-1]:
            stack.pop()
            res[i] = -1
        if not stack:
            res[i] = -1
        elif stack and nums[i] < stack[-1]:
            res[i] = stack[-1]
        stack.append(nums[i])
    return res


            
def run_test(nums, expected, test_name):
    print(test_name)
    print("nums     = " + str(nums))
    print("expected = " + str(expected))

    try:
        actual = next_largest_number_to_the_right(nums)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([5, 2, 4, 6, 1], [6, 4, 6, -1, -1], "Test 1")
    run_test([1, 2, 3, 4], [2, 3, 4, -1], "Test 2")
    run_test([4, 3, 2, 1], [-1, -1, -1, -1], "Test 3")
    run_test([2, 2, 2], [-1, -1, -1], "Test 4")
    run_test([7], [-1], "Test 5")
