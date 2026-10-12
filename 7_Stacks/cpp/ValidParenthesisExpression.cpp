/*
Valid Parenthesis Expression

Given a string representing an expression of parentheses containing the characters
'(', ')', '[', ']', '{', or '}', determine if the expression forms a valid
sequence of parentheses.

A sequence of parentheses is valid if every opening parenthesis has a
corresponding closing parenthesis, and no closing parenthesis appears before
its matching opening parenthesis.

Example 1:
Input: s = "([]{})"
Output: true

Example 2:
Input: s = "([]{)}"
Output: false

Explanation:
The '(' parenthesis is closed before its nested '{' parenthesis is closed.
*/

#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

bool IsValidParenthesisExpression(const string& s)
{
    throw runtime_error("Not implemented");
}

string FormatString(const string& value)
{
    return "\"" + value + "\"";
}

void RunTest(const string& s, bool expected, const string& testName)
{
    cout << testName << '\n';
    cout << "s        = " << FormatString(s) << '\n';
    cout << "expected = " << (expected ? "true" : "false") << '\n';

    try
    {
        bool actual = IsValidParenthesisExpression(s);
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
    RunTest("([]{})", true, "Test 1");
    RunTest("([]{)}", false, "Test 2");
    RunTest("()[]{}", true, "Test 3");
    RunTest("([)]", false, "Test 4");
    RunTest("", true, "Test 5");
    return 0;
}
