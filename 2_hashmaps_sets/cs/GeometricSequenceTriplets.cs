/*
A geometric sequence triplet is a sequence of three numbers where each successive number
is obtained by multiplying the preceding number by a constant called the common ratio.

Given an array of integers and a common ratio r, find the number of triplets of indexes
(i, j, k) such that i < j < k and the values form a geometric sequence.

Example:
Input: nums = [2, 1, 2, 4, 8, 8], r = 2
Output: 5
Explanation:
Triplet [2, 4, 8] occurs at indexes (0, 3, 4), (0, 3, 5), (2, 3, 4), (2, 3, 5).
Triplet [1, 2, 4] occurs at indexes (1, 2, 3).
*/

using System;
using System.Collections.Generic;

public class Solution
{
    public static long CountGeometricTriplets(int[] nums, int r)
    {
        Dictionary<int, int> leftMap = new();
        Dictionary<int, int> rightMap = new();
        for(int i=0; i < nums.Length; i++)
        {
            rightMap[nums[i]] = rightMap.GetValueOrDefault(nums[i], 0) +1;
        }
        long c = 0;
        foreach(int num in nums)
        {
            rightMap[num] -=1;
            if (num%r == 0)
            {
                if (leftMap.ContainsKey(num/r) && rightMap.ContainsKey(num*r))
                {
                    c += leftMap[num/r]*rightMap[num*r];
                }
            }
            leftMap[num] = leftMap.GetValueOrDefault(num, 0) +1;
        }
        return c;
        
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 2, 1, 2, 4, 8, 8 }, 2, 5, "Test 1");
        RunTest(new int[] { 1, 2, 2, 4 }, 2, 2, "Test 2");
        RunTest(new int[] { 1, 3, 9, 9, 27, 81 }, 3, 6, "Test 3");
        //RunTest(new int[] { 1, 5, 5, 25, 125 }, 5, 2, "Test 4");
        RunTest(new int[] { 1, 2, 3, 4 }, 2, 0, "Test 5");
    }

    private static void RunTest(int[] nums, int r, long expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("nums     = " + FormatArray(nums));
        Console.WriteLine("r        = " + r);
        Console.WriteLine("expected = " + expected);

        try
        {
            long actual = CountGeometricTriplets(nums, r);
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