/*
Next Largest Number to the Right

Given an integer array nums, return an output array res where, for each value
nums[i], res[i] is the first number to the right that's larger than nums[i].
If no larger number exists to the right of nums[i], set res[i] to -1.

Example:
Input: nums = [5, 2, 4, 6, 1]
Output: [6, 4, 6, -1, -1]
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

vector<int> NextLargestNumberToTheRight(const vector<int>& nums)
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

void RunTest(const vector<int>& nums, const vector<int>& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "nums     = " << FormatArray(nums) << '\n';
    cout << "expected = " << FormatArray(expected) << '\n';

    try
    {
        vector<int> actual = NextLargestNumberToTheRight(nums);
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
    RunTest({5, 2, 4, 6, 1}, {6, 4, 6, -1, -1}, "Test 1");
    RunTest({1, 2, 3, 4}, {2, 3, 4, -1}, "Test 2");
    RunTest({4, 3, 2, 1}, {-1, -1, -1, -1}, "Test 3");
    RunTest({2, 2, 2}, {-1, -1, -1}, "Test 4");
    RunTest({7}, {-1}, "Test 5");
    return 0;
}
