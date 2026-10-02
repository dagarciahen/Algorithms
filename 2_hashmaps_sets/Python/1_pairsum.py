import sys
from typing import List

x = int(input())
nums = list(map(int, sys.stdin.readline().split()))

def pair_sum_unsorted_two_pass(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        num_map[num] = i
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]
    return []


def pair_sum_unsor_one_pass(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, x in enumerate(nums):
        if target - x in hashmap:
            return [hashmap[target -x ], i]
        hashmap[x] = i
    return []

print(pair_sum_unsorted_two_pass(nums), x)
print(pair_sum_unsorted_one_pass(nums), x)

