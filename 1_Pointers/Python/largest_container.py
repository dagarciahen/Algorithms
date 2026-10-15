"""
Largest Container

You are given an array of non-negative integers where each value represents
the height of a vertical line. Return the maximum amount of water a container
formed by any two lines can hold.

Example:
Input: heights = [2, 7, 8, 4, 7, 6]
Output: 24
"""

from typing import List


def largest_container(heights: List[int]) -> int:
    left = 0
    right = len(heights)-1
    water = 0
    while (left < right):
        new_water = calculate_water(left, right, heights)
        if (left <= right):
            left += 1
        else:
            right -=1
        water = max(new_water, water)
    return water


def calculate_water(i, j, heights):
    width = j -i
    height = min(heights[i], heights[j])
    area = width*height
    return area
            
        


def run_test(heights: List[int], expected: int, test_name: str) -> None:
    print(test_name)
    print("heights  = " + str(heights))
    print("expected = " + str(expected))

    try:
        actual = largest_container(heights)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([2, 7, 8, 4, 7, 6], 24, "Test 1")
    run_test([1, 1], 1, "Test 2")
    run_test([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, "Test 3")
    run_test([4, 3, 2, 1, 4], 16, "Test 4")
    run_test([1, 2, 1], 2, "Test 5")
    runt_test([2,3,4,5,18,17,6,2,4,8,1], 40 "test 6")





