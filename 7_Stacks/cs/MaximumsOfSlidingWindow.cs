/*
Maximums of Sliding Window

There's a sliding window of size k that slides through an integer array
from left to right. Create a new array that records the largest number
found in each window as it slides through.

Example:
Input: nums = [3, 2, 4, 1, 2, 1, 1], k = 4
Output: [4, 4, 4, 2]
*/

using System;

public class Solution
{
    public static int[] MaximumsOfSlidingWindow(int[] nums, int k)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 3, 2, 4, 1, 2, 1, 1 }, 4, new int[] { 4, 4, 4, 2 }, "Test 1");
        RunTest(new int[] { 1, 3, -1, -3, 5, 3, 6, 7 }, 3, new int[] { 3, 3, 5, 5, 6, 7 }, "Test 2");
        RunTest(new int[] { 1 }, 1, new int[] { 1 }, "Test 3");
        RunTest(new int[] { 9, 8, 7, 6 }, 2, new int[] { 9, 8, 7 }, "Test 4");
        RunTest(new int[] { 4, 4, 4, 4 }, 3, new int[] { 4, 4 }, "Test 5");
    }

    private static void RunTest(int[] nums, int k, int[] expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("nums     = " + FormatArray(nums));
        Console.WriteLine("k        = " + k);
        Console.WriteLine("expected = " + FormatArray(expected));

        try
        {
            int[] actual = MaximumsOfSlidingWindow(nums, k);
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