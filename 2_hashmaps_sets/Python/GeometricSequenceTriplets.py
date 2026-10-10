"""
A geometric sequence triplet is a sequence of three numbers where each successive number
is obtained by multiplying the preceding number by a constant called the common ratio.

Given an array of integers and a common ratio r, find the number of triplets of indexes
(i, j, k) such that i < j < k and the values form a geometric sequence.

Example:
Input: nums = [2, 1, 2, 4, 8, 8], r = 2
Output: 5
Explanation:
Triplet [2, 4, 8] occurs at indexes (0, 3, 4), (0, 3, 5), (2, 3, 4), (2, 3, 5).
Triplet [1, 2, 4] occurs at indexes (1, 2, 3).
"""
from collections import defaultdict, Counter

def count_geometric_triplets(nums, r):
    left_map = defaultdict(int)
    right_map = Counter(nums)
    result = 0
    for num in nums:
        right_map[num] -= 1
        if num % r == 0:
            if num//r in left_map and num*r in right_map:
                result += left_map[num//r]*right_map[num*r]
        left_map[num] +=1
    return result


def run_test(nums, r, expected, test_name):
    print(test_name)
    print("nums     = " + str(nums))
    print("r        = " + str(r))
    print("expected = " + str(expected))

    try:
        actual = count_geometric_triplets(nums, r)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([2, 1, 2, 4, 8, 8], 2, 5, "Test 1")
    run_test([1, 2, 2, 4], 2, 2, "Test 2")
    run_test([1, 3, 9, 9, 27, 81], 3, 6, "Test 3")
    #run_test([1, 5, 5, 25, 125], 5, 2, "Test 4")
    #run_test([1, 2, 3, 4], 2, 0, "Test 5")
