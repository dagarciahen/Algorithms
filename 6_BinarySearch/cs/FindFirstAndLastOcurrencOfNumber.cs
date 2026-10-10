/*
First and Last Occurrences of a Number

Given an array of integers sorted in non-decreasing order, return the first
and last indexes of a target number. If the target is not found, return [-1, -1].

Example:
Input: nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], target = 4
Output: [3, 5]

Explanation:
The first and last occurrences of number 4 are indexes 3 and 5, respectively.
*/

using System;

public class Solution
{
    public static int[] FindFirstAndLastOccurrence(int[] nums, int target)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11 }, 4, new int[] { 3, 5 }, "Test 1");
        RunTest(new int[] { 1, 1, 1, 1, 1 }, 1, new int[] { 0, 4 }, "Test 2");
        RunTest(new int[] { 1, 2, 3, 5, 6, 7 }, 4, new int[] { -1, -1 }, "Test 3");
        RunTest(new int[] { 2 }, 2, new int[] { 0, 0 }, "Test 4");
        RunTest(new int[] { }, 3, new int[] { -1, -1 }, "Test 5");
    }

    private static void RunTest(int[] nums, int target, int[] expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("nums     = " + FormatArray(nums));
        Console.WriteLine("target   = " + target);
        Console.WriteLine("expected = " + FormatArray(expected));

        try
        {
            int[] actual = FindFirstAndLastOccurrence(nums, target);
            Console.WriteLine("actual   = " + FormatArray(actual));
            Console.WriteLine("pass     = " + AreEqual(actual, expected));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static string FormatArray(int[] values)
    {
        if (values == null)
        {
            return "null";
        }

        return "[" + string.Join(", ", values) + "]";
    }

    private static bool AreEqual(int[] left, int[] right)
    {
        if (left == null || right == null)
        {
            return left == right;
        }

        if (left.Length != right.Length)
        {
            return false;
        }

        for (int i = 0; i < left.Length; i++)
        {
            if (left[i] != right[i])
            {
                return false;
            }
        }

        return true;
    }
}