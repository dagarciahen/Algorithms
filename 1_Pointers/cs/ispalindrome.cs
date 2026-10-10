/*
A palindrome is a sequence of characters that reads the same forward and backward.


/*
A palindrome is a sequence of characters that reads the same forward and backward.

Given a string, determine if it's a palindrome after removing all non-alphanumeric characters. A character is alphanumeric if it's either a letter or a number.

--> LOWERCASE
*/
using System;

public class Solution
{
    public static bool isPalindrome(string s)
    {
        string new_s = "";
        int i = 0;
        int j = 0;
        foreach(char ch in s)
        {
            if (('a' <= ch && ch <= 'z') || ('A' <= ch && ch <= 'Z')) //isLetter // isLetterOrDigit
            {
                new_s += ch;
            }
        }
        i = 0;
        j = new_s.Length-1;
        while (i < j)
        {
            if (new_s[j] != new_s[i])
            {
                return false;
            }
            i++; j--;
        }
        return true;
    }


    public static void Main(string[] args)
    {
        RunTest("a dog! a panic in a pagoda.", true, "Test 1");
        RunTest("racecar", true, "Test 2");
        RunTest("a man, a plan, a canal: panama", true, "Test 3");
        RunTest("hello", false, "Test 4");
        RunTest("abc12321cba", true, "Test 5");
    }

    private static void RunTest(string s, bool expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("input    = " + FormatString(s));
        Console.WriteLine("expected = " + expected.ToString().ToLower());

        try
        {
            bool actual = isPalindrome(s);
            Console.WriteLine("actual   = " + actual.ToString().ToLower());
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