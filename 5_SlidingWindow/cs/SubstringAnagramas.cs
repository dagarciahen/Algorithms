/*
Substring Anagrams

Given two strings, s and t, both consisting of lowercase English letters,
return the number of substrings in s that are anagrams of t.

An anagram is a word or phrase formed by rearranging the letters of another
word or phrase, using all the original letters exactly once.

Example:
Input: s = "caabab", t = "aba"
Output: 2

Explanation:
There is an anagram of t starting at index 1 and another starting at index 2.
*/

using System;

public class Solution
{
    public static int CountSubstringAnagrams(string s, string t)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest("caabab", "aba", 2, "Test 1");
        RunTest("abab", "ab", 3, "Test 2");
        RunTest("aaaaa", "aa", 4, "Test 3");
        RunTest("abcdef", "gh", 0, "Test 4");
        RunTest("abc", "abcd", 0, "Test 5");
    }

    private static void RunTest(string s, string t, int expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("s        = " + FormatString(s));
        Console.WriteLine("t        = " + FormatString(t));
        Console.WriteLine("expected = " + expected);

        try
        {
            int actual = CountSubstringAnagrams(s, t);
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