/*
Shift Zeros To End

Given an array of integers, modify the array in place to move all zeros to the
end while maintaining the relative order of non-zero elements.
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

void shiftZerosToEnd(vector<int>& nums)
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

void RunTest(const vector<int>& input, const vector<int>& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "input    = " << FormatArray(input) << '\n';
    cout << "expected = " << FormatArray(expected) << '\n';

    try
    {
        vector<int> actual = input;
        shiftZerosToEnd(actual);
        cout << "actual   = " << FormatArray(actual) << '\n';
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
    RunTest({0, 1, 0, 3, 2}, {1, 3, 2, 0, 0}, "Test 1");
    RunTest({0, 0, 1}, {1, 0, 0}, "Test 2");
    RunTest({1, 2, 3}, {1, 2, 3}, "Test 3");
    RunTest({0, 0, 0}, {0, 0, 0}, "Test 4");
    RunTest({4, 0, 5, 0, 0, 3, 0, 1}, {4, 5, 3, 1, 0, 0, 0, 0}, "Test 5");
    return 0;
}