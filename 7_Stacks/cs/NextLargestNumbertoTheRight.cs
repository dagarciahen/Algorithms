/*
Next Largest Number to the Right

Given an integer array nums, return an output array res where, for each value
nums[i], res[i] is the first number to the right that's larger than nums[i].
If no larger number exists to the right of nums[i], set res[i] to -1.

Example:
Input: nums = [5, 2, 4, 6, 1]
Output: [6, 4, 6, -1, -1]
*/

using System;

public class Solution
{
    public static int[] NextLargestNumberToTheRight(int[] nums)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 5, 2, 4, 6, 1 }, new int[] { 6, 4, 6, -1, -1 }, "Test 1");
        RunTest(new int[] { 1, 2, 3, 4 }, new int[] { 2, 3, 4, -1 }, "Test 2");
        RunTest(new int[] { 4, 3, 2, 1 }, new int[] { -1, -1, -1, -1 }, "Test 3");
        RunTest(new int[] { 2, 2, 2 }, new int[] { -1, -1, -1 }, "Test 4");
        RunTest(new int[] { 7 }, new int[] { -1 }, "Test 5");
    }

    private static void RunTest(int[] nums, int[] expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("nums     = " + FormatArray(nums));
        Console.WriteLine("expected = " + FormatArray(expected));

        try
        {
            int[] actual = NextLargestNumberToTheRight(nums);
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