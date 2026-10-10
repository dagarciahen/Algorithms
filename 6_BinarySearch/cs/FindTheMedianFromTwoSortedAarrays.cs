/*
Find the Median From Two Sorted Arrays

Given two sorted integer arrays, find their median value as if they were
merged into a single sorted sequence.

Example 1:
Input: nums1 = [0, 2, 5, 6, 8], nums2 = [1, 3, 7]
Output: 4.0

Explanation:
Merging both arrays results in [0, 1, 2, 3, 5, 6, 7, 8], which has a median
of (3 + 5) / 2 = 4.0.

Example 2:
Input: nums1 = [0, 2, 5, 6, 8], nums2 = [1, 3, 7, 9]
Output: 5.0

Explanation:
Merging both arrays results in [0, 1, 2, 3, 5, 6, 7, 8, 9], which has a median of 5.

Constraints:
At least one of the input arrays will contain an element.
*/

using System;

public class Solution
{
    public static double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 0, 2, 5, 6, 8 }, new int[] { 1, 3, 7 }, 4.0, "Test 1");
        RunTest(new int[] { 0, 2, 5, 6, 8 }, new int[] { 1, 3, 7, 9 }, 5.0, "Test 2");
        RunTest(new int[] { 1, 2 }, new int[] { 3, 4 }, 2.5, "Test 3");
        RunTest(new int[] { }, new int[] { 7 }, 7.0, "Test 4");
        RunTest(new int[] { 2 }, new int[] { }, 2.0, "Test 5");
    }

    private static void RunTest(int[] nums1, int[] nums2, double expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("nums1    = " + FormatArray(nums1));
        Console.WriteLine("nums2    = " + FormatArray(nums2));
        Console.WriteLine("expected = " + expected);

        try
        {
            double actual = FindMedianSortedArrays(nums1, nums2);
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