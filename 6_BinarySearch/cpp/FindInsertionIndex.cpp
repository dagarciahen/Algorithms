/*
Find the Insertion Index

You are given a sorted array that contains unique values, along with an integer target.

If the array contains the target value, return its index.
Otherwise, return the insertion index. This is the index where the target would be
if it were inserted in order, maintaining the sorted sequence of the array.

Example 1:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 4
Output: 2

Example 2:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 6
Output: 4

Explanation:
6 would be inserted at index 4 to be positioned between 5 and 7:
[1, 2, 4, 5, 6, 7, 8, 9]
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

int FindInsertionIndex(const vector<int>& nums, int target)
{
    throw runtime_error("Not implemented");
}

string FormatArray(const vector<int>& values)
{
    string result = "[";
    for (size_t i = 0; i < values.size(); i++)
    {
        if (i > 0) result += ", ";
        result += to_string(values[i]);
    }
    result += "]";
    return result;
}

void RunTest(const vector<int>& nums, int target, int expected, const string& testName)
{
    cout << testName << '\n';
    cout << "nums     = " << FormatArray(nums) << '\n';
    cout << "target   = " << target << '\n';
    cout << "expected = " << expected << '\n';

    try
    {
        int actual = FindInsertionIndex(nums, target);
        cout << "actual   = " << actual << '\n';
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
    RunTest({1, 2, 4, 5, 7, 8, 9}, 4, 2, "Test 1");
    RunTest({1, 2, 4, 5, 7, 8, 9}, 6, 4, "Test 2");
    RunTest({1, 3, 5, 7}, 0, 0, "Test 3");
    RunTest({1, 3, 5, 7}, 10, 4, "Test 4");
    RunTest({}, 3, 0, "Test 5");
    return 0;
}
