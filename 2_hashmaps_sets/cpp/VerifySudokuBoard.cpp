/*
Given a partially completed 9x9 Sudoku board, determine if the current state of the board
adheres to the rules of the game.

Each row and column must contain unique numbers between 1 and 9, or be empty
(represented as 0).

Each of the nine 3x3 subgrids must contain unique numbers between 1 and 9, or be empty.

Note: You are asked to determine whether the current state of the board is valid
given these rules, not whether the board is solvable.
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

bool verifySudokuBoard(const vector<vector<int>>& board)
{
    throw runtime_error("Not implemented");
}

void PrintBoard(const vector<vector<int>>& board)
{
    for (const vector<int>& row : board)
    {
        cout << "[";
        for (size_t i = 0; i < row.size(); i++)
        {
            if (i > 0) cout << ", ";
            cout << row[i];
        }
        cout << "]\n";
    }
}

void RunTest(const vector<vector<int>>& board, bool expected, const string& testName)
{
    cout << testName << '\n';
    cout << "board:\n";
    PrintBoard(board);
    cout << "expected = " << (expected ? "true" : "false") << '\n';

    try
    {
        bool actual = verifySudokuBoard(board);
        cout << "actual   = " << (actual ? "true" : "false") << '\n';
        cout << "pass     = " << (actual == expected ? "true" : "false") << '\n';
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented" << '\n';
    }

    cout << '\n';
}

int main()
{
    RunTest({
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}}, true, "Test 1");
    RunTest({
        {5, 3, 5, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}}, false, "Test 2");
    RunTest({
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {5, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}}, false, "Test 3");
    RunTest({
        {3, 0, 6, 0, 5, 8, 4, 0, 0},
        {5, 2, 0, 0, 0, 0, 0, 0, 0},
        {0, 8, 7, 0, 0, 0, 0, 3, 1},
        {1, 0, 2, 5, 0, 0, 3, 2, 0},
        {9, 0, 0, 8, 6, 3, 0, 0, 5},
        {0, 5, 0, 0, 9, 0, 6, 0, 0},
        {0, 1, 0, 0, 0, 0, 0, 7, 4},
        {0, 3, 0, 0, 0, 8, 2, 5, 0},
        {0, 0, 5, 2, 0, 6, 0, 0, 0}}, false, "Test 4");
    RunTest({
        {0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0}}, true, "Test 5");
    return 0;
}
