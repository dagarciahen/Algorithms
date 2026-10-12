/*
Find the Target in a Rotated Sorted Array

A rotated sorted array is an array of numbers sorted in ascending order,
in which a portion of the array is moved from the beginning to the end.

For example, a possible rotation of [1, 2, 3, 4, 5] is [3, 4, 5, 1, 2],
where the first two numbers are moved to the end.

Given a rotated sorted array of unique numbers, return the index of a
target value. If the target value is not present, return -1.

Example:
Input: nums = [8, 9, 1, 2, 3, 4, 5, 6, 7], target = 1
Output: 2
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

int SearchRotatedSortedArray(const vector<int>& nums, int target)
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
        int actual = SearchRotatedSortedArray(nums, target);
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
    RunTest({8, 9, 1, 2, 3, 4, 5, 6, 7}, 1, 2, "Test 1");
    RunTest({4, 5, 6, 7, 0, 1, 2}, 0, 4, "Test 2");
    RunTest({4, 5, 6, 7, 0, 1, 2}, 3, -1, "Test 3");
    RunTest({1}, 1, 0, "Test 4");
    RunTest({6, 7, 8, 1, 2, 3, 4, 5}, 5, 7, "Test 5");
    return 0;
}
