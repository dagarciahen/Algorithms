/*
Given an array of integers, return the indexes of any two numbers that add up to a target.
The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
*/

using System;
using System.Collections.Generic;

public class Solution
{
    public static int[] PairSumUnsorted(int[] nums, int target)
    {
        Dictionary<int, int> ValuesHash = new();

        for (int i = 0 ; i < nums.Length;i++)
        {
            int complementary = target - nums[i];
            if (ValuesHash.ContainsKey(complementary) && ValuesHash[complementary] != i)
            {
                return new int[] {i, ValuesHash[complementary]};

            }
            ValuesHash[nums[i]] = i;
        }
        return Array.Empty<int>();
    }


    public static void Main(string[] args)
    {
        RunTest(new int[] { -1, 3, 4, 2 }, 3, new int[] { 0, 2 }, "Test 1");
        RunTest(new int[] { 2, 7, 11, 15 }, 9, new int[] { 0, 1 }, "Test 2");
        RunTest(new int[] { 3, 3 }, 6, new int[] { 0, 1 }, "Test 3");
        RunTest(new int[] { 1, 2, 3, 4 }, 8, Array.Empty<int>(), "Test 4");
        RunTest(new int[] { 0, -2, 5, 9, -7 }, 2, new int[] { 2, 4 }, "Test 5");
    }

    private static void RunTest(int[] nums, int target, int[] expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("nums     = " + FormatArray(nums));
        Console.WriteLine("target   = " + target);
        Console.WriteLine("expected = " + FormatArray(expected));

        try
        {
            int[] actual = PairSumUnsorted(nums, target);
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

        if (left.Length == 0)
        {
            return true;
        }

        if (left.Length == 2)
        {
            return (left[0] == right[0] && left[1] == right[1]) ||
                   (left[0] == right[1] && left[1] == right[0]);
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