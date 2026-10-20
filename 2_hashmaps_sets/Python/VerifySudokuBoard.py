"""
Given a partially completed 9x9 Sudoku board, determine if the current state of the board
adheres to the rules of the game.

Each row and column must contain unique numbers between 1 and 9, or be empty
(represented as 0).

Each of the nine 3x3 subgrids must contain unique numbers between 1 and 9, or be empty.

Note: You are asked to determine whether the current state of the board is valid
given these rules, not whether the board is solvable.
"""


def verify_sudoku_board(board):
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0: continue
            if num in row_sets[r] or num in col_sets[c] or num in subgrid_sets[r//3][c//3]:
                return False
            row_sets[r].add(num)
            col_sets[c].add(num)
            subgrid_sets[r//3][c//3].add(num)

    return True
            
"""
runtime complexity is 9x9 is o(1) space complexity is o(1) 
in general in terms of n is o(n**2) as we iterate through each cell once in the board one and perfom contanst hash set operations
The time complexity in terms of n is o(n**") due to the row,col and subgird sets each array contains n hash sets and each hasset grows a size of n

"""





def print_board(board):
    for row in board:
        print(row)


def run_test(board, expected, test_name):
    print(test_name)
    print("board:")
    print_board(board)
    print("expected = " + str(expected))

    try:
        actual = verify_sudoku_board(board)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ], True, "Test 1")
    run_test([
        [5, 3, 5, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ], False, "Test 2")
    run_test([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [5, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ], False, "Test 3")
    run_test([
        [3, 0, 6, 0, 5, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [1, 0, 2, 5, 0, 0, 3, 2, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 7, 4],
        [0, 3, 0, 0, 0, 8, 2, 5, 0],
        [0, 0, 5, 2, 0, 6, 0, 0, 0],
    ], False, "Test 4")
    run_test([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ], True, "Test 5")


"""
DONT WATCH ME
def verify_sudoku_board(board):
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for r, row in enumerate(board):
        for c, num in enumerate(row):
            if num == 0:
                continue

            if num in row_sets[r]:
                return False

            if num in col_sets[c]:
                return False

            if num in subgrid_sets[r // 3][c // 3]:
                return False

            row_sets[r].add(num)
            col_sets[c].add(num)
            subgrid_sets[r // 3][c // 3].add(num)

    return True

"""


