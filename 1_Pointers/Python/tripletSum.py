"""
Triplet Sum

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i, j, and k are distinct and nums[i] + nums[j] + nums[k] == 0.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
"""

from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = []
    for i in range(len(nums)):
        #a+b+c = 0 -> -a = b+c
        if nums[i] > 0: continue
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        j = i +1
        k = len(nums)-1
        while j < k:
            val = nums[j] + nums[k]
            if val < target:
                j += 1
            elif val > target:
                k -= 1
            else:
                triplets.append([nums[i], nums[j], nums[k]])
    nums.sort() triplets = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        if nums[i] > 0:
            continue
        target = -nums[i]
        # a+b+c=0 -> -a = b+c
        j = i +1
        k = len(nums)-1
        while (j < k):
            value = nums[j] + nums[k]
            if value < target:
                j +=1
            elif value > target:
                k -=1
            else:
                triplet = [nums[i], nums[j], nums[k]]
                triplets.append(triplet)
                j +=1
                if j < k and nums[j] == nums[j-1]:
                    j +=1
    return triplets
                j +=1
                k -=1
                if j < k and nums[j] == nums[j-1]:
                    j +=1
    return triplets




        
    


def normalize(triplets: List[List[int]]) -> List[List[int]]:
    return sorted(sorted(triplet) for triplet in triplets)


def run_test(nums: List[int], expected: List[List[int]], test_name: str) -> None:
    print(test_name)
    print("nums     = " + str(nums))
    print("expected = " + str(expected))

    try:
        actual = triplet_sum(nums)
        print("actual   = " + str(actual))
        print("pass     = " + str(normalize(actual) == normalize(expected)))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]], "Test 1")
    run_test([0, 0, 0], [[0, 0, 0]], "Test 2")
    run_test([1, 2, 3], [], "Test 3")
    run_test([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]], "Test 4")
    run_test([-3, -1, 0, 1, 2, -1, -4], [[-3, 1, 2], [-1, -1, 2], [-1, 0, 1]], "Test 5")

        

