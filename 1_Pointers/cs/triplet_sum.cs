/* 
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . 
The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.

Input: nums = [0, -1, 2, -3, 1]
Output: [[-3, 1, 2], [-1, 0, 1]]
*/
//13:49eaASA
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
	public static List<List<int>> TripletSum(int[] nums)
	{
		Array.Sort(nums);
		//a+b +c = 0
		//a = -b-c;
		
		List<List<int>> Triplets = new();
		for(int i; i < nums.Length-1; i++)
		{
			int num = nums[i];

			if (num < 0)
			{
				continue;
			}
			if (i > 0 && nums[i] == nums[i-1]) {continue;}
			int target = -nums[i];
			int j = i +1;
			int k = nums.Length-1;
			while (j < k)
			{
				int val = nums[j] + nums[k];
				if (val < target)
				{
					j++;
				}
				else if (val > target)
				{
					k--;
				}
				else
				{
					if ((j < k) && (nums[j] == nums[j-1]))
					{
						continue;
					}
					List<int> triplet = new List<int>{nums[i], nums[j], nums[k]};
					Triplets.Append(triplet);
				}
			}
		}
		return Triplets;
		
	}

    public static void Main(string[] args)
    {
        RunTest(
            new int[] { 0, -1, 2, -3, 1 },
            new List<List<int>>
            {
                new List<int> { -3, 1, 2 },
                new List<int> { -1, 0, 1 }
            },
            "Test 1");

        RunTest(
            new int[] { -1, 0, 1, 2, -1, -4 },
            new List<List<int>>
            {
                new List<int> { -1, -1, 2 },
                new List<int> { -1, 0, 1 }
            },
            "Test 2");

        RunTest(
            new int[] { 0, 0, 0 },
            new List<List<int>>
            {
                new List<int> { 0, 0, 0 }
            },
            "Test 3");

        RunTest(
            new int[] { 1, 2, 3, 4 },
            new List<List<int>>(),
            "Test 4");

        RunTest(
            new int[] { -2, 0, 1, 1, 2 },
            new List<List<int>>
            {
                new List<int> { -2, 0, 2 },
                new List<int> { -2, 1, 1 }
            },
            "Test 5");
    }


    private static void RunTest(int[] nums, List<List<int>> expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("nums     = " + FormatArray(nums));
        Console.WriteLine("expected = " + FormatTriplets(expected));

        try
        {
            List<List<int>> actual = TripletSum(nums);
            Console.WriteLine("actual   = " + FormatTriplets(actual));
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

    private static string FormatTriplets(List<List<int>> triplets)
    {
        if (triplets == null)
        {
            return "null";
        }

        return "[" + string.Join(", ", triplets.Select(t => "[" + string.Join(", ", t) + "]")) + "]";
    }
}
