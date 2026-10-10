/*
Find the Insertion Index

You are given a sorted array that contains unique values, along with an integer target.

If the array contains the target value, return its index.
Otherwise, return the insertion index. This is the index where the target would be
if it were inserted in order, maintaining the sorted sequence of the array.

Example 1:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 4
Output: 2

Example 2:
Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 6
Output: 4

Explanation:
6 would be inserted at index 4 to be positioned between 5 and 7:
[1, 2, 4, 5, 6, 7, 8, 9]
*/

using System;

public class Solution
{
    public static int FindInsertionIndex(int[] nums, int target)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 1, 2, 4, 5, 7, 8, 9 }, 4, 2, "Test 1");
        RunTest(new int[] { 1, 2, 4, 5, 7, 8, 9 }, 6, 4, "Test 2");
        RunTest(new int[] { 1, 3, 5, 7 }, 0, 0, "Test 3");
        RunTest(new int[] { 1, 3, 5, 7 }, 10, 4, "Test 4");
        RunTest(new int[] { }, 3, 0, "Test 5");
    }

    private static void RunTest(int[] nums, int target, int expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("nums     = " + FormatArray(nums));
        Console.WriteLine("target   = " + target);
        Console.WriteLine("expected = " + expected);

        try
        {
            int actual = FindInsertionIndex(nums, target);
            Console.WriteLine("actual   = " + actual);
            Console.WriteLine("pass     = " + (actual == expected));
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
}