from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    i = 0
    j = n
    
    while i < j:
        m = nums[i] + nums[j]
        if m > target:
            j = j-1
        elif m < target:
            i = i +1
        else:
            return [i,j]
    return []
