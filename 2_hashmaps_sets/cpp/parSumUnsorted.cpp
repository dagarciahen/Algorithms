/*
Given an array of integers, return the indexes of any two numbers that add up to a target.
The order of the indexes in the result does not matter. If no pair is found, return an empty array.

Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

vector<int> pairSumUnsorted(const vector<int>& nums, int target)
{
    throw runtime_error("Not implemented");
}

bool AreEqual(const vector<int>& left, const vector<int>& right)
{
    if (left.size() != right.size())
    {
        return false;
    }

    if (left.size() == 2)
    {
        return (left[0] == right[0] && left[1] == right[1]) ||
               (left[0] == right[1] && left[1] == right[0]);
    }

    return left == right;
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
        vector<int> actual = pairSumUnsorted(nums, target);
        cout << "actual   = " << FormatArray(actual) << '\n';
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
    RunTest({-1, 3, 4, 2}, 3, {0, 2}, "Test 1");
    RunTest({2, 7, 11, 15}, 9, {0, 1}, "Test 2");
    RunTest({3, 3}, 6, {0, 1}, "Test 3");
    RunTest({1, 2, 3, 4}, 8, {}, "Test 4");
    RunTest({0, -2, 5, 9, -7}, 2, {2, 4}, "Test 5");
    return 0;
}
