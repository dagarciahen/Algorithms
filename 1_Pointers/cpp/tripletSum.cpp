/*
Triplet Sum

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i, j, and k are distinct and nums[i] + nums[j] + nums[k] == 0.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
*/

#include <algorithm>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

vector<vector<int>> tripletSum(const vector<int>& nums)
{
    throw runtime_error("Not implemented");
}

vector<vector<int>> Normalize(vector<vector<int>> triplets)
{
    for (vector<int>& triplet : triplets)
    {
        sort(triplet.begin(), triplet.end());
    }
    sort(triplets.begin(), triplets.end());
    return triplets;
}

string FormatTriplets(const vector<vector<int>>& triplets)
{
    string result = "[";
    for (size_t i = 0; i < triplets.size(); i++)
    {
        if (i > 0)
        {
            result += ", ";
        }
        result += "[";
        for (size_t j = 0; j < triplets[i].size(); j++)
        {
            if (j > 0)
            {
                result += ", ";
            }
            result += to_string(triplets[i][j]);
        }
        result += "]";
    }
    result += "]";
    return result;
}

void RunTest(const vector<int>& nums, const vector<vector<int>>& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "expected = " << FormatTriplets(expected) << '\n';

    try
    {
        vector<vector<int>> actual = tripletSum(nums);
        cout << "actual   = " << FormatTriplets(actual) << '\n';
        cout << "pass     = " << (Normalize(actual) == Normalize(expected) ? "true" : "false") << '\n';
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented" << '\n';
    }

    cout << '\n';
}

int main()
{
    RunTest({-1, 0, 1, 2, -1, -4}, {{-1, -1, 2}, {-1, 0, 1}}, "Test 1");
    RunTest({0, 0, 0}, {{0, 0, 0}}, "Test 2");
    RunTest({1, 2, 3}, {}, "Test 3");
    RunTest({-2, 0, 1, 1, 2}, {{-2, 0, 2}, {-2, 1, 1}}, "Test 4");
    RunTest({-3, -1, 0, 1, 2, -1, -4}, {{-3, 1, 2}, {-1, -1, 2}, {-1, 0, 1}}, "Test 5");
    return 0;
}