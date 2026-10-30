
"""
#1798 - Max Number of K-Sum Pairs
Difficulty: Medium
Topics: Array, Hash Table, Two Pointers, Sorting

You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1

Constraints:
"""

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashNums = {}
        ops = 0
        for i in range(len(nums)):
            num = nums[i]
            complement = k - num
            print(f"num={num}, comp={complement}, hash={hashNums}, ops={ops}")
            if complement in hashNums and hashNums[complement] != i:
                ops += 1
                del hashNums[complement]
            else:
                hashNums[num] = i

            print(f"num={num}, comp={complement}, hash={hashNums}, ops={ops}")
        return ops, nums

s = Solution()

print(s.maxOperations([1,2,3,4],5))
print(s.maxOperations([3,1,3,4,3],6))




