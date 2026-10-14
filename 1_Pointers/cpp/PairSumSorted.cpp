/*
Pair Sum - Sorted

Given a sorted array of integers and a target value, return the indexes of the
two numbers whose sum equals the target. If no such pair exists, return an
empty array.

Example:
Input: nums = [1, 2, 3, 4, 6], target = 6
Output: [1, 3]
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

vector<int> pairSumSorted(const vector<int>& nums, int target)
{
    throw runtime_error("Not implemented");
}

string FormatArray(const vector<int>& values)
{
    string result = "[";
    for (size_t i = 0; i < values.size(); i++)
    {
        if (i > 0)
        {
            result += ", ";
        }
        result += to_string(values[i]);
    }
    result += "]";
    return result;
}

void RunTest(const vector<int>& nums, int target, const vector<int>& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "nums     = " << FormatArray(nums) << '\n';
    cout << "target   = " << target << '\n';
    cout << "expected = " << FormatArray(expected) << '\n';

    try
    {
        vector<int> actual = pairSumSorted(nums, target);
        cout << "actual   = " << FormatArray(actual) << '\n';
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
    RunTest({1, 2, 3, 4, 6}, 6, {1, 3}, "Test 1");
    RunTest({2, 3, 4, 7}, 7, {0, 2}, "Test 2");
    RunTest({1, 2}, 3, {0, 1}, "Test 3");
    RunTest({1, 2, 3}, 10, {}, "Test 4");
    RunTest({-5, -2, 0, 3, 8}, 1, {1, 3}, "Test 5");
    return 0;
}