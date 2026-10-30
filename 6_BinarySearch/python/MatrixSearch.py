"""
Matrix Search

Determine if a target value exists in a matrix.
Each row of the matrix is sorted in non-decreasing order, and the first value
of each row is greater than or equal to the last value of the previous row.

Example:
matrix = [[2, 3, 4, 6], [7, 10, 11, 17], [20, 21, 24, 33]]
target = 21
Output: True
"""


def matrix_search(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m*n
    while left < right:
        idx  = left + (right-left)//2
        row = idx //n
        col = idx %n
        val = matrix[row][col]
        if val == target: return True
        elif val < target:
            left = idx +1 
        else:
            right = idx 
    return False




def print_matrix(matrix):
    for row in matrix:
        print(row)


def run_test(matrix, target, expected, test_name):
    print(test_name)
    print("matrix:")
    print_matrix(matrix)
    print("target   = " + str(target))
    print("expected = " + str(expected))

    try:
        actual = matrix_search(matrix, target)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([[2, 3, 4, 6], [7, 10, 11, 17], [20, 21, 24, 33]], 21, True, "Test 1")
    run_test([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 8, False, "Test 2")
    run_test([[5]], 5, True, "Test 3")
    run_test([[1, 2, 3, 4]], 4, True, "Test 4")
    run_test([[1, 2, 3], [3, 4, 5], [6, 7, 8]], 9, False, "Test 5")
