/*
Evaluate Expression

Given a string representing a mathematical expression containing integers,
parentheses, addition, and subtraction operators, evaluate and return the result
of the expression.

Example:
Input: s = "18-(7+(2-4))"
Output: 13
*/

#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

int EvaluateExpression(const string& s)
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
        int actual = EvaluateExpression(s);
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
    RunTest("18-(7+(2-4))", 13, "Test 1");
    RunTest("1 + 2 - 3", 0, "Test 2");
    RunTest("(10-(2+3))", 5, "Test 3");
    RunTest("7", 7, "Test 4");
    RunTest("20-(3-(2-1))", 18, "Test 5");
    return 0;
}
