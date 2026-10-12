/*
For each zero in an m x n matrix, set its entire row and column to zero in place.

Input: matrix = [[1,2,3,4,5],[6,0,6,9,10],[11,12,13,14,15],[16,17,18,19,0]]
Output: [[1,0,3,4,0],[0,0,0,0,0],[11,0,13,14,0],[0,0,0,0,0]]
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

void setZeroes(vector<vector<int>>& matrix)
{
    throw runtime_error("Not implemented");
}

vector<vector<int>> CopyMatrix(const vector<vector<int>>& matrix)
{
    return matrix;
}

bool AreEqual(const vector<vector<int>>& left, const vector<vector<int>>& right)
{
    return left == right;
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

void RunTest(const vector<vector<int>>& matrix, const vector<vector<int>>& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "input:\n";
    PrintMatrix(matrix);
    cout << "expected:\n";
    PrintMatrix(expected);

    try
    {
        vector<vector<int>> actual = CopyMatrix(matrix);
        setZeroes(actual);
        cout << "actual:\n";
        PrintMatrix(actual);
        cout << "pass     = " << (AreEqual(actual, expected) ? "true" : "false") << '\n';
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented" << '\n';
    }

    cout << '\n';
}

int main()
{
    RunTest({{1, 2, 3, 4, 5}, {6, 0, 6, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 0}},
            {{1, 0, 3, 4, 0}, {0, 0, 0, 0, 0}, {11, 0, 13, 14, 0}, {0, 0, 0, 0, 0}}, "Test 1");
    RunTest({{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, "Test 2");
    RunTest({{0, 1}, {2, 3}}, {{0, 0}, {0, 3}}, "Test 3");
    RunTest({{1, 2, 0}, {4, 5, 6}, {7, 8, 9}}, {{0, 0, 0}, {4, 5, 0}, {7, 8, 0}}, "Test 4");
    RunTest({{1, 0, 3}, {0, 5, 6}, {7, 8, 9}}, {{0, 0, 0}, {0, 0, 0}, {0, 0, 9}}, "Test 5");
    return 0;
}
