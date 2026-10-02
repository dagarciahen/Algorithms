"Given an array of integers, modify the array in place to move all zeros to the end while maintaining the relative order of non-zero elements."

from typing import List

def shift_zeros_to_end(nums: List[int]) -> None:
    n = len(nums)
    
    left = 0

    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
    return nums





if __name__ == "__main__":
    nums = [0,1,0,3,2]
    print(shift_zeros_to_end(nums))

