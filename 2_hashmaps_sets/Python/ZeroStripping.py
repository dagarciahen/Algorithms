"""
For each zero in an m x n matrix, set its entire row and column to zero in place.

Input: matrix = [[1,2,3,4,5],[6,0,6,9,10],[11,12,13,14,15],[16,17,18,19,0]]
Output: [[1,0,3,4,0],[0,0,0,0,0],[11,0,13,14,0],[0,0,0,0,0]]
"""


def set_zeroes(matrix):
    row_with_zeros = set()
    col_with_zeros = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_with_zeros.add(i); col_with_zeros.add(j)
    i = 0; j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row_with_zeros or j in col_with_zeros:
                matrix[i][j] = 0
    return matrix

"""
runtime complexity is o(mxn) as the matrix is fully read it two times
O(mn) +O(mn) = O(mxn)
the space complexity is the sets i am using as helpers, row_with_zeros cna store until m rows,
col_with_zeros until n cols so M+N o(m+n)
"""

def set_zeros_better_solution(matrix):
    if not matrix or not matrix[0]: return
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = False
    for c in range(n):
        if matrix[0][c] == 0: first_row_has_zero = True; break
    first_col_has_zero = False
    for r in range(m):
        if matrix[r][0] == 0:
            first_col_has_zero = 0
            break
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0
    for r in range(1, m):
        for c in range(1, n):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    if first_row_has_zero:
        for c in range(n):
            matrix[0][n] = 0
    if first_col_has_zero:
        for r in range(n):
            matrix[r][0] = 0
    return matrix

"""
complexity- still o(mn) first check to first row and col is o(m) and o(n) m+n then we perform two passes on the matrix,
o(mn) and iterastes again to set values m and then n
space complexity -> o(1) we only used the markers first col and first row no extra space ds
"""



def copy_matrix(matrix):
    return [row[:] for row in matrix]


def print_matrix(matrix):
    for row in matrix:
        print(row)


def are_equal(left, right):
    return left == right


def run_test(matrix, expected, test_name):
    print(test_name)
    print("input:")
    print_matrix(matrix)
    print("expected:")
    print_matrix(expected)

    try:
        actual = copy_matrix(matrix)
        set_zeroes(actual)
        print("actual:")
        print_matrix(actual)
        print("pass     = " + str(are_equal(actual, expected)))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test(
        [[1, 2, 3, 4, 5], [6, 0, 6, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 0]],
        [[1, 0, 3, 4, 0], [0, 0, 0, 0, 0], [11, 0, 13, 14, 0], [0, 0, 0, 0, 0]],
        "Test 1",
    )
    run_test(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "Test 2",
    )
    run_test(
        [[0, 1], [2, 3]],
        [[0, 0], [0, 3]],
        "Test 3",
    )
    run_test(
        [[1, 2, 0], [4, 5, 6], [7, 8, 9]],
        [[0, 0, 0], [4, 5, 0], [7, 8, 0]],
        "Test 4",
    )
    run_test(
        [[1, 0, 3], [0, 5, 6], [7, 8, 9]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 9]],
        "Test 5",
    )
