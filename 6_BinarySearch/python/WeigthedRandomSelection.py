"""
Weighted Random Selection

Given an array of items, each with a corresponding weight, implement a function
that randomly selects an item from the array, where the probability of selecting
any item is proportional to its weight.

Return the index of the selected item.

Constraints:
The weights array contains at least one element.
"""

import random
def weighted_random_selection(weights):
    runningsum = 0
    prefix_sum = []
    for w in weights:
        runningsum += w 
        prefix_sum.append(runningsum)

    left = 0
    right = len(prefix_sum)
    val = random.randint(1, prefix_sum[-1])
    while left < right:
        m = left + (right -left)//2
        if weights[m] == val:
            return m
        elif weights[m] < val:
            left = m +1 
        else:
            right = m
    return left 

    


def run_test(weights, test_name):
    print(test_name)
    print("weights   = " + str(weights))
    print("expected  = a valid index between 0 and " + str(len(weights) - 1))

    try:
        actual = weighted_random_selection(weights)
        print("actual    = " + str(actual))
        print("pass      = " + str(0 <= actual < len(weights)))
    except NotImplementedError:
        print("actual    = not implemented")

    print()


if __name__ == "__main__":
    run_test([3, 1, 2, 4], "Test 1")
    run_test([1], "Test 2")
    run_test([10, 10, 10], "Test 3")
    run_test([5, 100], "Test 4")
    run_test([2, 4, 6, 8, 10], "Test 5")
