/*
Find the Target in a Rotated Sorted Array

A rotated sorted array is an array of numbers sorted in ascending order,
in which a portion of the array is moved from the beginning to the end.

For example, a possible rotation of [1, 2, 3, 4, 5] is [3, 4, 5, 1, 2],
where the first two numbers are moved to the end.

Given a rotated sorted array of unique numbers, return the index of a
target value. If the target value is not present, return -1.

Example:
Input: nums = [8, 9, 1, 2, 3, 4, 5, 6, 7], target = 1
Output: 2
*/

using System;

public class Solution
{
    public static int SearchRotatedSortedArray(int[] nums, int target)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 8, 9, 1, 2, 3, 4, 5, 6, 7 }, 1, 2, "Test 1");
        RunTest(new int[] { 4, 5, 6, 7, 0, 1, 2 }, 0, 4, "Test 2");
        RunTest(new int[] { 4, 5, 6, 7, 0, 1, 2 }, 3, -1, "Test 3");
        RunTest(new int[] { 1 }, 1, 0, "Test 4");
        RunTest(new int[] { 6, 7, 8, 1, 2, 3, 4, 5 }, 5, 7, "Test 5");
    }

    private static void RunTest(int[] nums, int target, int expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("nums     = " + FormatArray(nums));
        Console.WriteLine("target   = " + target);
        Console.WriteLine("expected = " + expected);

        try
        {
            int actual = SearchRotatedSortedArray(nums, target);
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