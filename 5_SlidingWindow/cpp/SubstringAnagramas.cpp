/*
Substring Anagrams

Given two strings, s and t, both consisting of lowercase English letters,
return the number of substrings in s that are anagrams of t.

An anagram is a word or phrase formed by rearranging the letters of another
word or phrase, using all the original letters exactly once.

Example:
Input: s = "caabab", t = "aba"
Output: 2

Explanation:
There is an anagram of t starting at index 1 and another starting at index 2.
*/

#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

int CountSubstringAnagrams(const string& s, const string& t)
{
    throw runtime_error("Not implemented");
}

string FormatString(const string& value)
{
    return "\"" + value + "\"";
}

void RunTest(const string& s, const string& t, int expected, const string& testName)
{
    cout << testName << '\n';
    cout << "s        = " << FormatString(s) << '\n';
    cout << "t        = " << FormatString(t) << '\n';
    cout << "expected = " << expected << '\n';

    try
    {
        int actual = CountSubstringAnagrams(s, t);
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
    RunTest("caabab", "aba", 2, "Test 1");
    RunTest("abab", "ab", 3, "Test 2");
    RunTest("aaaaa", "aa", 4, "Test 3");
    RunTest("abcdef", "gh", 0, "Test 4");
    RunTest("abc", "abcd", 0, "Test 5");
    return 0;
}
