"""Move all zeros in an array to the end while preserving the order of non-zero elements.
[0,1,0]
[1,0,0]
"""

from typing import List


def shift_zeros_to_end(nums: List[int]) -> None:
    left = 0
    right = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1


def run_test(nums: List[int], expected: List[int], test_name: str) -> None:
    print(test_name)
    print("nums     = " + str(nums))
    print("expected = " + str(expected))

    try:
        working = nums[:]
        shift_zeros_to_end(working)
        print("actual   = " + str(working))
        print("pass     = " + str(working == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([0, 1, 0, 3, 2], [1, 3, 2, 0, 0], "Test 1")
    run_test([0, 0, 1], [1, 0, 0], "Test 2")
    run_test([1, 2, 3], [1, 2, 3], "Test 3")
    run_test([0, 0, 0], [0, 0, 0], "Test 4")
    run_test([4, 0, 5, 0, 0, 3, 0, 1], [4, 5, 3, 1, 0, 0, 0, 0], "Test 5")

