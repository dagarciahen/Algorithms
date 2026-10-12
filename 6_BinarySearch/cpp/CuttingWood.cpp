/*
Cutting Wood

You are given an array representing the heights of trees, and an integer k
representing the total length of wood that needs to be cut.

For this task, a woodcutting machine is set to a certain height, H.
The machine cuts off the top part of all trees taller than H, while trees
shorter than H remain untouched. Determine the highest possible setting of
the woodcutter so that it cuts at least k meters of wood.

Assume the woodcutter cannot be set higher than the height of the tallest
tree in the array.

Example:
Input: heights = [2, 6, 3, 8], k = 7
Output: 3
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

int CuttingWood(const vector<int>& heights, int k)
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

void RunTest(const vector<int>& heights, int k, int expected, const string& testName)
{
    cout << testName << '\n';
    cout << "heights  = " << FormatArray(heights) << '\n';
    cout << "k        = " << k << '\n';
    cout << "expected = " << expected << '\n';

    try
    {
        int actual = CuttingWood(heights, k);
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
    RunTest({2, 6, 3, 8}, 7, 3, "Test 1");
    RunTest({5, 7, 9}, 4, 5, "Test 2");
    RunTest({10, 10, 10}, 6, 8, "Test 3");
    RunTest({1, 2, 3, 4}, 0, 4, "Test 4");
    RunTest({4, 12, 7, 10}, 11, 5, "Test 5");
    return 0;
}
