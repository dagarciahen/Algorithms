"""
You are given an array of numbers, each representing the height of a vertical line on a graph. 
A container can be formed with any pair of these lines, along with the x-axis of the graph. Return the amount of water which the largest container can hold.
"""
from typing import List
def largest_container(heights: List[int]) -> int:
    n = len(heights)
    i = 0
    j = n-1
    water = 0
    while i < j:
        new_water = min(heights[i], heights[j])*(j-i)
        if new_water > water:
            water = new_water

        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
        print(i,j,water)
    return water













if __name__ == "__main__":
    heights = [2,7,8,4,7,6]
    output = largest_container(heights)
    print(output)





