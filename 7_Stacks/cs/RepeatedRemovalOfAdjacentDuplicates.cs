/*
Repeated Removal of Adjacent Duplicates

Given a string, continually perform the following operation:
remove a pair of adjacent duplicates from the string.
Continue performing this operation until the string no longer contains
pairs of adjacent duplicates. Return the final string.

Example 1:
Input: s = "aacabba"
Output: "c"

Example 2:
Input: s = "aaa"
Output: "a"
*/

using System;

public class Solution
{
    public static string RemoveAdjacentDuplicates(string s)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest("aacabba", "c", "Test 1");
        RunTest("aaa", "a", "Test 2");
        RunTest("abba", "", "Test 3");
        RunTest("azxxzy", "ay", "Test 4");
        RunTest("abc", "abc", "Test 5");
    }

    private static void RunTest(string s, string expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("s        = " + FormatString(s));
        Console.WriteLine("expected = " + FormatString(expected));

        try
        {
            string actual = RemoveAdjacentDuplicates(s);
            Console.WriteLine("actual   = " + FormatString(actual));
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