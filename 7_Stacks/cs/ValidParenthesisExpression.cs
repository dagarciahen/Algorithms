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

using System;

public class Solution
{
    public static bool IsValidParenthesisExpression(string s)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest("([]{})", true, "Test 1");
        RunTest("([]{)}", false, "Test 2");
        RunTest("()[]{}", true, "Test 3");
        RunTest("([)]", false, "Test 4");
        RunTest("", true, "Test 5");
    }

    private static void RunTest(string s, bool expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("s        = " + FormatString(s));
        Console.WriteLine("expected = " + expected);

        try
        {
            bool actual = IsValidParenthesisExpression(s);
            Console.WriteLine("actual   = " + actual);
            Console.WriteLine("pass     = " + (actual == expected));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static string FormatString(string value)
    {
        if (value == null)
        {
            return "null";
        }

        return "\"" + value + "\"";
    }
}