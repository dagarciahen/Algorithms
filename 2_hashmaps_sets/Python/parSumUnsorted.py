"""
Given an array of integers, return the indexes of any two numbers that add up to a target.
The order of the indexes in the result does not matter. If no pair is found, return an empty array.

Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
"""


def pair_sum_unsorted(nums, target):
    hashMap = {}
    for i in range(len(nums)):
        complementary = target - nums[i]
        if complementary in hashMap and hashMap[complementary] != i:
            return [i, hashMap[complementary]]
        hashMap[nums[i]] = i
    return []

def are_equal(actual, nums, target):
    if len(actual) == 0: return True
    if len(actual) != 2: return False
    return nums[actual[0]] + nums[actual[1]] == target


def run_test(nums, target, expected, test_name):
    print(test_name)
    print("nums     = " + str(nums))
    print("target   = " + str(target))
    print("expected = " + str(expected))

    try:
        actual = pair_sum_unsorted(nums, target)
        print("actual   = " + str(actual))
        print("pass     = " + str(are_equal(actual, nums, target)))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([-1, 3, 4, 2], 3, [0, 2], "Test 1")
    run_test([2, 7, 11, 15], 9, [0, 1], "Test 2")
    run_test([3, 3], 6, [0, 1], "Test 3")
    run_test([1, 2, 3, 4], 8, [], "Test 4")
    run_test([0, -2, 5, 9, -7], 2, [2, 4], "Test 5")



"""
DONT WATCH ME YET
best_Solution:
def():
    hashMap = {}
    for i in range(len(nums)):
        complementary = target - nums[i]
        if complementary in hashMap and hashMap[complementary] != i:
            return [i, hashMap[complementary]]
        hashMap[nums[i]] = i
    return []
"""







