/*
Longest Substring With Unique Characters

Given a string, determine the length of its longest substring
that consists only of unique characters.

Example:
Input: s = "abcba"
Output: 3

Explanation:
Substring "abc" is the longest substring of length 3 that contains
unique characters. "cba" also fits this description.
*/

#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

int LongestUniqueSubstring(const string& s)
{
    throw runtime_error("Not implemented");
}

string FormatString(const string& value)
{
    return "\"" + value + "\"";
}

void RunTest(const string& s, int expected, const string& testName)
{
    cout << testName << '\n';
    cout << "s        = " << FormatString(s) << '\n';
    cout << "expected = " << expected << '\n';

    try
    {
        int actual = LongestUniqueSubstring(s);
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
    RunTest("abcba", 3, "Test 1");
    RunTest("aaaaa", 1, "Test 2");
    RunTest("abcdef", 6, "Test 3");
    RunTest("", 0, "Test 4");
    RunTest("pwwkew", 3, "Test 5");
    return 0;
}
