/*
Maximums of Sliding Window

There's a sliding window of size k that slides through an integer array
from left to right. Create a new array that records the largest number
found in each window as it slides through.

Example:
Input: nums = [3, 2, 4, 1, 2, 1, 1], k = 4
Output: [4, 4, 4, 2]
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

vector<int> MaximumsOfSlidingWindow(const vector<int>& nums, int k)
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

void RunTest(const vector<int>& nums, int k, const vector<int>& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "nums     = " << FormatArray(nums) << '\n';
    cout << "k        = " << k << '\n';
    cout << "expected = " << FormatArray(expected) << '\n';

    try
    {
        vector<int> actual = MaximumsOfSlidingWindow(nums, k);
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
    RunTest({3, 2, 4, 1, 2, 1, 1}, 4, {4, 4, 4, 2}, "Test 1");
    RunTest({1, 3, -1, -3, 5, 3, 6, 7}, 3, {3, 3, 5, 5, 6, 7}, "Test 2");
    RunTest({1}, 1, {1}, "Test 3");
    RunTest({9, 8, 7, 6}, 2, {9, 8, 7}, "Test 4");
    RunTest({4, 4, 4, 4}, 3, {4, 4}, "Test 5");
    return 0;
}
