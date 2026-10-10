/*
Longest Substring With Unique Characters

Given a string, determine the length of its longest substring
that consists only of unique characters.

Example:
Input: s = "abcba"
Output: 3

Explanation:
Substring "abc" is the longest substring of length 3 that contains
unique characters. "cba" also fits this description.
*/

using System;

public class Solution
{
    public static int LongestUniqueSubstring(string s)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest("abcba", 3, "Test 1");
        RunTest("aaaaa", 1, "Test 2");
        RunTest("abcdef", 6, "Test 3");
        RunTest("", 0, "Test 4");
        RunTest("pwwkew", 3, "Test 5");
    }

    private static void RunTest(string s, int expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("s        = " + FormatString(s));
        Console.WriteLine("expected = " + expected);

        try
        {
            int actual = LongestUniqueSubstring(s);
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