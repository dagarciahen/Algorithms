/*
Find the Median From Two Sorted Arrays

Given two sorted integer arrays, find their median value as if they were
merged into a single sorted sequence.

Example 1:
Input: nums1 = [0, 2, 5, 6, 8], nums2 = [1, 3, 7]
Output: 4.0

Explanation:
Merging both arrays results in [0, 1, 2, 3, 5, 6, 7, 8], which has a median
of (3 + 5) / 2 = 4.0.

Example 2:
Input: nums1 = [0, 2, 5, 6, 8], nums2 = [1, 3, 7, 9]
Output: 5.0

Explanation:
Merging both arrays results in [0, 1, 2, 3, 5, 6, 7, 8, 9], which has a median of 5.

Constraints:
At least one of the input arrays will contain an element.
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

double FindMedianSortedArrays(const vector<int>& nums1, const vector<int>& nums2)
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

void RunTest(const vector<int>& nums1, const vector<int>& nums2, double expected, const string& testName)
{
    cout << testName << '\n';
    cout << "nums1    = " << FormatArray(nums1) << '\n';
    cout << "nums2    = " << FormatArray(nums2) << '\n';
    cout << "expected = " << expected << '\n';

    try
    {
        double actual = FindMedianSortedArrays(nums1, nums2);
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
    RunTest({0, 2, 5, 6, 8}, {1, 3, 7}, 4.0, "Test 1");
    RunTest({0, 2, 5, 6, 8}, {1, 3, 7, 9}, 5.0, "Test 2");
    RunTest({1, 2}, {3, 4}, 2.5, "Test 3");
    RunTest({}, {7}, 7.0, "Test 4");
    RunTest({2}, {}, 2.0, "Test 5");
    return 0;
}
