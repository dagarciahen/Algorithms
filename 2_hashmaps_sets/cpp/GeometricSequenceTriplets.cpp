/*
A geometric sequence triplet is a sequence of three numbers where each successive number
is obtained by multiplying the preceding number by a constant called the common ratio.

Given an array of integers and a common ratio r, find the number of triplets of indexes
(i, j, k) such that i < j < k and the values form a geometric sequence.

Example:
Input: nums = [2, 1, 2, 4, 8, 8], r = 2
Output: 5
Explanation:
Triplet [2, 4, 8] occurs at indexes (0, 3, 4), (0, 3, 5), (2, 3, 4), (2, 3, 5).
Triplet [1, 2, 4] occurs at indexes (1, 2, 3).
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

long long countGeometricTriplets(const vector<int>& nums, int r)
{
    throw runtime_error("Not implemented");
}

void RunTest(const vector<int>& nums, int r, long long expected, const string& testName)
{
    cout << testName << '\n';
    cout << "nums     = [";
    for (size_t i = 0; i < nums.size(); i++)
    {
        if (i > 0) cout << ", ";
        cout << nums[i];
    }
    cout << "]\n";
    cout << "r        = " << r << '\n';
    cout << "expected = " << expected << '\n';

    try
    {
        long long actual = countGeometricTriplets(nums, r);
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
    RunTest({2, 1, 2, 4, 8, 8}, 2, 5, "Test 1");
    RunTest({1, 2, 2, 4}, 2, 2, "Test 2");
    RunTest({1, 3, 9, 9, 27, 81}, 3, 6, "Test 3");
    RunTest({1, 5, 5, 25, 125}, 5, 4, "Test 4");
    RunTest({1, 2, 3, 4}, 2, 0, "Test 5");
    return 0;
}
