/*
Longest Uniform Substring After Replacements

A uniform substring is one in which all characters are identical.
Given a string, determine the length of the longest uniform substring
that can be formed by replacing up to k characters.

Example:
Input: s = "aabcdcca", k = 2
Output: 5

Explanation:
If we can replace at most 2 characters, the longest uniform substring
we can achieve is "ccccc", obtained by replacing 'b' and 'd' with 'c'.
*/

using System;

public class Solution
{
    public static int LongestUniformSubstringAfterReplacements(string s, int k)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest("aabcdcca", 2, 5, "Test 1");
        RunTest("aaaa", 2, 4, "Test 2");
        RunTest("ababa", 1, 3, "Test 3");
        RunTest("abcde", 1, 2, "Test 4");
        RunTest("baaab", 2, 5, "Test 5");
    }

    private static void RunTest(string s, int k, int expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("s        = " + FormatString(s));
        Console.WriteLine("k        = " + k);
        Console.WriteLine("expected = " + expected);

        try
        {
            int actual = LongestUniformSubstringAfterReplacements(s, k);
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