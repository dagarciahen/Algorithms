/*
Happy Number

In number theory, a happy number is defined as a number that, when repeatedly subjected
to the process of squaring its digits and summing those squares, eventually leads to 1.
An unhappy number will never reach 1 during this process, and will get stuck in an infinite loop.

Given an integer, determine if it's a happy number.

Example:
Input: n = 23
Output: true

Explanation:
23 -> 13 -> 10 -> 1
because:
2^2 + 3^2 = 13
1^2 + 3^2 = 10
1^2 + 0^2 = 1
*/

#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

bool IsHappyNumber(int n)
{
    throw runtime_error("Not implemented");
}

void RunTest(int n, bool expected, const string& testName)
{
    cout << testName << '\n';
    cout << "n        = " << n << '\n';
    cout << "expected = " << (expected ? "true" : "false") << '\n';

    try
    {
        bool actual = IsHappyNumber(n);
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
    RunTest(23, true, "Test 1");
    RunTest(19, true, "Test 2");
    RunTest(2, false, "Test 3");
    RunTest(1, true, "Test 4");
    RunTest(116, false, "Test 5");
    return 0;
}
