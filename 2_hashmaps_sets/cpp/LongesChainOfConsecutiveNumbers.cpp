/*
Find the longest chain of consecutive numbers in an array.
Two numbers are consecutive if they have a difference of 1.

Example:
Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
Output: 4
Explanation: The longest chain of consecutive numbers is 5, 6, 7, 8.
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

int longestConsecutiveChain(const vector<int>& nums)
{
    throw runtime_error("Not implemented");
}

void RunTest(const vector<int>& nums, int expected, const string& testName)
{
    cout << testName << '\n';
    cout << "nums     = [";
    for (size_t i = 0; i < nums.size(); i++)
    {
        if (i > 0) cout << ", ";
        cout << nums[i];
    }
    cout << "]\n";
    cout << "expected = " << expected << '\n';

    try
    {
        int actual = longestConsecutiveChain(nums);
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
    RunTest({1, 6, 2, 5, 8, 7, 10, 3}, 4, "Test 1");
    RunTest({100, 4, 200, 1, 3, 2}, 4, "Test 2");
    RunTest({0, 3, 7, 2, 5, 8, 4, 6, 0, 1}, 9, "Test 3");
    RunTest({10, 30, 20}, 1, "Test 4");
    RunTest({}, 0, "Test 5");
    return 0;
}
