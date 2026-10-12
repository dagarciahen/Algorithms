/*
First and Last Occurrences of a Number

Given an array of integers sorted in non-decreasing order, return the first
and last indexes of a target number. If the target is not found, return [-1, -1].

Example:
Input: nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], target = 4
Output: [3, 5]

Explanation:
The first and last occurrences of number 4 are indexes 3 and 5, respectively.
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

vector<int> FindFirstAndLastOccurrence(const vector<int>& nums, int target)
{
    throw runtime_error("Not implemented");
}

bool AreEqual(const vector<int>& left, const vector<int>& right)
{
    return left == right;
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

void RunTest(const vector<int>& nums, int target, const vector<int>& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "nums     = " << FormatArray(nums) << '\n';
    cout << "target   = " << target << '\n';
    cout << "expected = " << FormatArray(expected) << '\n';

    try
    {
        vector<int> actual = FindFirstAndLastOccurrence(nums, target);
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
    RunTest({1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11}, 4, {3, 5}, "Test 1");
    RunTest({1, 1, 1, 1, 1}, 1, {0, 4}, "Test 2");
    RunTest({1, 2, 3, 5, 6, 7}, 4, {-1, -1}, "Test 3");
    RunTest({2}, 2, {0, 0}, "Test 4");
    RunTest({}, 3, {-1, -1}, "Test 5");
    return 0;
}
