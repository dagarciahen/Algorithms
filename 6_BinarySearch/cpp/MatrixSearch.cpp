/*
Matrix Search

Determine if a target value exists in a matrix.
Each row of the matrix is sorted in non-decreasing order, and the first value
of each row is greater than or equal to the last value of the previous row.

Example:
matrix = [[2, 3, 4, 6], [7, 10, 11, 17], [20, 21, 24, 33]]
target = 21
Output: true
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

bool MatrixSearch(const vector<vector<int>>& matrix, int target)
{
    throw runtime_error("Not implemented");
}

void PrintMatrix(const vector<vector<int>>& matrix)
{
    for (const vector<int>& row : matrix)
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

void RunTest(const vector<vector<int>>& matrix, int target, bool expected, const string& testName)
{
    cout << testName << '\n';
    cout << "matrix:" << '\n';
    PrintMatrix(matrix);
    cout << "target   = " << target << '\n';
    cout << "expected = " << (expected ? "true" : "false") << '\n';

    try
    {
        bool actual = MatrixSearch(matrix, target);
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
    RunTest({{2, 3, 4, 6}, {7, 10, 11, 17}, {20, 21, 24, 33}}, 21, true, "Test 1");
    RunTest({{1, 3, 5}, {7, 9, 11}, {13, 15, 17}}, 8, false, "Test 2");
    RunTest({{5}}, 5, true, "Test 3");
    RunTest({{1, 2, 3, 4}}, 4, true, "Test 4");
    RunTest({{1, 2, 3}, {3, 4, 5}, {6, 7, 8}}, 9, false, "Test 5");
    return 0;
}
