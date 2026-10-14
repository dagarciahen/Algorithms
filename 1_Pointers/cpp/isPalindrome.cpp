/*
Palindrome Check

Given a string, determine if it is a palindrome after removing all
non-alphanumeric characters and ignoring capitalization.

Example:
Input: s = "a dog! a panic in a pagoda."
Output: true
*/

#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

bool isPalindrome(const string& s)
{
    throw runtime_error("Not implemented");
}

void RunTest(const string& s, bool expected, const string& testName)
{
    cout << testName << '\n';
    cout << "s        = \"" << s << "\"\n";
    cout << "expected = " << (expected ? "true" : "false") << '\n';

    try
    {
        bool actual = isPalindrome(s);
        cout << "actual   = " << (actual ? "true" : "false") << '\n';
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
    RunTest("a dog! a panic in a pagoda.", true, "Test 1");
    RunTest("race a car", false, "Test 2");
    RunTest("A man, a plan, a canal: Panama", true, "Test 3");
    RunTest("", true, "Test 4");
    RunTest("0P", false, "Test 5");
    return 0;
}