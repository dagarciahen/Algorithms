"""
Local Maxima

A local maxima is a value greater than both its immediate neighbors.
Return the index of any local maxima in an array.

You may assume that an element is always considered to be strictly greater
than a neighbor that is outside the array.

Example:
Input: nums = [1, 4, 3, 2, 3]
Output: 1
Note: Index 4 is also acceptable.

Constraints:
No two adjacent elements in the array are equal.
"""


def find_local_maxima(nums):
    

    
def is_local_maxima(nums, index):
    if index < 0 or index >= len(nums):
        return False

    left_is_smaller = index == 0 or nums[index] > nums[index - 1]
    right_is_smaller = index == len(nums) - 1 or nums[index] > nums[index + 1]
    return left_is_smaller and right_is_smaller


def run_test(nums, expected_indices, test_name):
    print(test_name)
    print("nums             = " + str(nums))
    print("expected indices = " + str(expected_indices))

    try:
        actual = find_local_maxima(nums)
        passed = actual in expected_indices and is_local_maxima(nums, actual)
        print("actual           = " + str(actual))
        print("pass             = " + str(passed))
    except NotImplementedError:
        print("actual           = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 4, 3, 2, 3], [1, 4], "Test 1")
    run_test([1, 3, 2], [1], "Test 2")
    run_test([5, 4, 3, 2], [0], "Test 3")
    run_test([1, 2, 3, 4], [3], "Test 4")
    run_test([2, 1, 3, 5, 4], [0, 3], "Test 5")
