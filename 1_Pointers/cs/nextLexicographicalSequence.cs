/*
Given a string of lowercase English letters, rearrange the characters to form a new string representing the next
 immediate sequence in lexicographical (alphabetical) order. If the given string is already last in lexicographical 
 order among all possible arrangements, return the arrangement that's first in lexicographical order.
Input = "abcd"
Output: "abdc"
*/

using System;
using System.Linq;

public class Solution
{
    public static string nextLexicoGraphicalSeq(string s)
    {
        char[] wordsList = s.ToCharArray();

        int j = wordsList.Length -1;
        int pivot = 0;
        while (j >0 && wordsList[j-1] >= wordsList[j])
        {
            j --;
        }
        if ( j == 0)
        {
            Array.Reverse(wordsList);
            return String.Join("", wordsList);
        }
        pivot = j-1;
        j = wordsList.Length -1;
        while (wordsList[pivot] > wordsList[j])
        {
            j--;
        }
        (wordsList[pivot], wordsList[j]) = (wordsList[j], wordsList[pivot]);
        Array.Reverse(wordsList, pivot, wordsList.Length-pivot-1);
        return String.Join("", wordsList);

			
		}
    public static void Main(string[] args)
    {
        RunTest("abcd", "abdc", "Test 1");
        RunTest("dcba", "abcd", "Test 2");
        RunTest("abdc", "acbd", "Test 3");
        RunTest("aabb", "abab", "Test 4");
        RunTest("z", "z", "Test 5");
    }

    private static void RunTest(string input, string expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("input    = " + FormatString(input));
        Console.WriteLine("expected = " + FormatString(expected));

        try
        {
            string actual = nextLexicoGraphicalSeq(input);
            Console.WriteLine("actual   = " + FormatString(actual));
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