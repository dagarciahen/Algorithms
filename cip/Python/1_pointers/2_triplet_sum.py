import sys
from typing import List
nums = list(map(int, sys.stdin.readline().split()))
print(nums)

def triplet_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = []
    n = len(nums)
    for i in range(n):
        triplet = []
        #a + b+ c = 0 --> a = -c -b (b +c = -a)if a = 0 --> no triplets
        a = nums[i] 
        target = -a
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i +1
        k = n-1
        while j < k:
            val = nums[j] + nums[k]
            
            if val < target:
                j += 1 
            elif val > target: 
                k-=1
            else:
                triplet = [a, nums[j], nums[k]]
                triplets.append(triplet)
                j += 1
                while j < k  and nums[j] == nums[j-1]:
                    j += 1
            
    return triplets

print(triplet_sum(nums))

        

