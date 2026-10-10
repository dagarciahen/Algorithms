/*
Given an array of integers, move all zeros to the end while keeping the relative order
of the non-zero elements.

Input: nums = [0, 1, 0, 3, 2]
10032
Output: [1, 3, 2, 0, 0]
0103
1003
1300
*/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public static void shiftZerosToEnd(List<int> nums)
	{
		int i = 0;
		int j = 0;
		int len = nums.Count;
        for (; j < len -1; )
        {
            if (nums[j] == 0)
            {
                j++;
            } else
            {
                (nums[i], nums[j]) = (nums[j], nums[j]);
                i++;
            }
        }
	}

    public static void Main(string[] args)
    {
        RunTest(new List<int> { 0, 1, 0, 3, 2 }, new List<int> { 1, 3, 2, 0, 0 }, "Test 1");
        RunTest(new List<int> { 0, 0, 0 }, new List<int> { 0, 0, 0 }, "Test 2");
        RunTest(new List<int> { 1, 2, 3 }, new List<int> { 1, 2, 3 }, "Test 3");
        RunTest(new List<int> { 4, 0, 5, 0, 0, 6 }, new List<int> { 4, 5, 6, 0, 0, 0 }, "Test 4");
        RunTest(new List<int> { }, new List<int> { }, "Test 5");
    }

    private static void RunTest(List<int> input, List<int> expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("input    = " + FormatList(input));
        Console.WriteLine("expected = " + FormatList(expected));

        try
        {
            List<int> actual = new List<int>(input);
            shiftZerosToEnd(actual);
            Console.WriteLine("actual   = " + FormatList(actual));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static string FormatList(List<int> nums)
    {
        if (nums == null)
        {
            return "null";
        }

        return "[" + string.Join(", ", nums) + "]";
    }
}