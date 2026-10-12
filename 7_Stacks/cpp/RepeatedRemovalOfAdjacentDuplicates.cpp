/*
Repeated Removal of Adjacent Duplicates

Given a string, continually perform the following operation:
remove a pair of adjacent duplicates from the string.
Continue performing this operation until the string no longer contains
pairs of adjacent duplicates. Return the final string.

Example 1:
Input: s = "aacabba"
Output: "c"

Example 2:
Input: s = "aaa"
Output: "a"
*/

#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

string RemoveAdjacentDuplicates(const string& s)
{
    throw runtime_error("Not implemented");
}

string FormatString(const string& value)
{
    return "\"" + value + "\"";
}

void RunTest(const string& s, const string& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "s        = " << FormatString(s) << '\n';
    cout << "expected = " << FormatString(expected) << '\n';

    try
    {
        string actual = RemoveAdjacentDuplicates(s);
        cout << "actual   = " << FormatString(actual) << '\n';
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
    RunTest("aacabba", "c", "Test 1");
    RunTest("aaa", "a", "Test 2");
    RunTest("abba", "", "Test 3");
    RunTest("azxxzy", "ay", "Test 4");
    RunTest("abc", "abc", "Test 5");
    return 0;
}
