/*
Longest Uniform Substring After Replacements

A uniform substring is one in which all characters are identical.
Given a string, determine the length of the longest uniform substring
that can be formed by replacing up to k characters.

Example:
Input: s = "aabcdcca", k = 2
Output: 5

Explanation:
If we can replace at most 2 characters, the longest uniform substring
we can achieve is "ccccc", obtained by replacing 'b' and 'd' with 'c'.
*/

#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

int LongestUniformSubstringAfterReplacements(const string& s, int k)
{
    throw runtime_error("Not implemented");
}

string FormatString(const string& value)
{
    return "\"" + value + "\"";
}

void RunTest(const string& s, int k, int expected, const string& testName)
{
    cout << testName << '\n';
    cout << "s        = " << FormatString(s) << '\n';
    cout << "k        = " << k << '\n';
    cout << "expected = " << expected << '\n';

    try
    {
        int actual = LongestUniformSubstringAfterReplacements(s, k);
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
    RunTest("aabcdcca", 2, 5, "Test 1");
    RunTest("aaaa", 2, 4, "Test 2");
    RunTest("ababa", 1, 3, "Test 3");
    RunTest("abcde", 1, 2, "Test 4");
    RunTest("baaab", 2, 5, "Test 5");
    return 0;
}
