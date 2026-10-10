/*
Evaluate Expression

Given a string representing a mathematical expression containing integers,
parentheses, addition, and subtraction operators, evaluate and return the result
of the expression.

Example:
Input: s = "18-(7+(2-4))"
Output: 13
*/

using System;

public class Solution
{
    public static int EvaluateExpression(string s)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest("18-(7+(2-4))", 13, "Test 1");
        RunTest("1 + 2 - 3", 0, "Test 2");
        RunTest("(10-(2+3))", 5, "Test 3");
        RunTest("7", 7, "Test 4");
        RunTest("20-(3-(2-1))", 18, "Test 5");
    }

    private static void RunTest(string s, int expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("s        = " + FormatString(s));
        Console.WriteLine("expected = " + expected);

        try
        {
            int actual = EvaluateExpression(s);
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