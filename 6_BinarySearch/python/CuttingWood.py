"""
Cutting Wood

You are given an array representing the heights of trees, and an integer k
representing the total length of wood that needs to be cut.

For this task, a woodcutting machine is set to a certain height, H.
The machine cuts off the top part of all trees taller than H, while trees
shorter than H remain untouched. Determine the highest possible setting of
the woodcutter so that it cuts at least k meters of wood.

Assume the woodcutter cannot be set higher than the height of the tallest
 tree in the array.

Example:
Input: heights = [2, 6, 3, 8], k = 7
Output: 3
"""


def cutting_wood(heights, k):


def cut(c, k, heights):
    wood = 0
    for h in heights:
        if h >= c:
            wood += h -c
    return wood >= k

def run_test(heights, k, expected, test_name):
    print(test_name)
    print("heights  = " + str(heights))
    print("k        = " + str(k))
    print("expected = " + str(expected))

    try:
        actual = cutting_wood(heights, k)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([2, 6, 3, 8], 7, 3, "Test 1")
    run_test([5, 7, 9], 4, 5, "Test 2")
    run_test([10, 10, 10], 6, 8, "Test 3")
    run_test([1, 2, 3, 4], 0, 4, "Test 4")
    run_test([4, 12, 7, 10], 11, 6, "Test 5")
