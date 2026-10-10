/*

Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers 
in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]

Input: nums = [1, 1, 1], target = 2
Output: [0, 1]

*/
//3:36

using System;

public class Solution
{
    public static void Main(string[] args)
    {
        RunTest(new int[] { -5, -2, 3, 4, 6 }, 7, new int[] { 2, 3 }, "TEST1");
        //RunTest(new int[] { 1, 1, 1 }, 2, new int[] { 0, 1 }, "TEST 2");
        RunTest(new int[] { 1, 2, 3, 4, 6, 8 }, 10, new int[] { 1, 5 }, "TEST 3");
        RunTest(new int[] { 2, 5, 9, 11 }, 11, new int[] { 0, 2 }, "TEST 4");
        RunTest(new int[] { 1, 3, 5, 7 }, 20, new int[] { }, "TEST 5");
    }

    public static int[] PairSumSorted(int[] nums, int target)
    {
        int i = 0;
        int j = nums.Length-1;
        while (i < j)
        {
            int value = nums[i] + nums[j];
            if (value < target)
            {
                i++;
            } 
            else if (value > target)
            {
                j--;
                
            }
            else
            {
                return new int[]{i, j};
            }
            
        }
        return Array.Empty<int>();
    }

    private static void RunTest(int[] nums, int target, int[] expected, string testName)
    {
        int[] actual = PairSumSorted(nums, target);

        Console.WriteLine(testName);
        Console.WriteLine("nums     = " + FormatArray(nums));
        Console.WriteLine("target   = " + target);
        Console.WriteLine("expected = " + FormatArray(expected));
        Console.WriteLine("actual   = " + FormatArray(actual));
        Console.WriteLine("pass     = " + AreEqual(actual, expected));
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