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

using System;

public class Solution
{
    public static bool IsHappyNumber(int n)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(23, true, "Test 1");
        RunTest(19, true, "Test 2");
        RunTest(2, false, "Test 3");
        RunTest(1, true, "Test 4");
        RunTest(116, false, "Test 5");
    }

    private static void RunTest(int n, bool expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("n        = " + n);
        Console.WriteLine("expected = " + expected);

        try
        {
            bool actual = IsHappyNumber(n);
            Console.WriteLine("actual   = " + actual);
            Console.WriteLine("pass     = " + (actual == expected));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }
}