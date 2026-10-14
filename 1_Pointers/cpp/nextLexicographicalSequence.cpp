/*
Given a string of lowercase English letters, rearrange the characters to form a new string representing the next
immediate sequence in lexicographical (alphabetical) order. If the given string is already last in lexicographical
order among all possible arrangements, return the arrangement that's first in lexicographical order.

Example:
Input: s = "abcd"
Output: "abdc"
*/

#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

string nextLexicographicalSequence(const string& s)
{
    throw runtime_error("Not implemented");
}

string FormatString(const string& value)
{
    return "\"" + value + "\"";
}

void RunTest(const string& input, const string& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "input    = " << FormatString(input) << '\n';
    cout << "expected = " << FormatString(expected) << '\n';

    try
    {
        string actual = nextLexicographicalSequence(input);
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
    RunTest("abcd", "abdc", "Test 1");
    RunTest("dcba", "abcd", "Test 2");
    RunTest("abdc", "acbd", "Test 3");
    RunTest("aabb", "abab", "Test 4");
    RunTest("z", "z", "Test 5");
    return 0;
}
