/*
Largest Container

You are given an array of non-negative integers where each value represents
the height of a vertical line. Return the maximum amount of water a container
formed by any two lines can hold.

Example:
Input: heights = [2, 7, 8, 4, 7, 6]
Output: 24
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

int largestContainer(const vector<int>& heights)
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

void RunTest(const vector<int>& heights, int expected, const string& testName)
{
    cout << testName << '\n';
    cout << "heights  = " << FormatArray(heights) << '\n';
    cout << "expected = " << expected << '\n';

    try
    {
        int actual = largestContainer(heights);
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
    RunTest({2, 7, 8, 4, 7, 6}, 24, "Test 1");
    RunTest({1, 1}, 1, "Test 2");
    RunTest({1, 8, 6, 2, 5, 4, 8, 3, 7}, 49, "Test 3");
    RunTest({4, 3, 2, 1, 4}, 16, "Test 4");
    RunTest({1, 2, 1}, 2, "Test 5");
    return 0;
}