/* 
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0 . The solution must not contain duplicate triplets (e.g., [1, 2, 3] and [2, 3, 1] are considered duplicates). If no such triplets are found, return an empty array.

Each triplet can be arranged in any order, and the output can be returned in any order.
*/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
	public static void Main(string[] args)
	{
		int[] nums = {0, -1, 2, -3, 1};
		List<List<int>> result = TripletSum(nums);

		foreach ( var triplet in result)
		{
			Console.WriteLine($"[{string.Join(",", triplet)}]");
		}
	}
	public static List<List<int>> TripletSum(int[] nums)
	{
		if (nums == null || nums.Length == 0)
		{
			return new List<List<int>>();
		}
		int n = nums.Length;
		Array.Sort(nums);
		List<List<int>> Triplets = new List<List<int>>();
		
		for (int i = 0; i < n; i++)
		{
			int target = -nums[i];
			if (nums[i] > 0) {break;}
			if (i > 0 && nums[i] == nums[i-1])
			{
				continue;
			}
			int j = i +1;
			int k = n -1;
			while (j < k)
			{
				int val = nums[j] + nums[k];
				if ( val < target)
				{j++;}
				else if ( val > target)
				{
					k--;
				}
				else
				{
					List<int> triplet = new List<int>{nums[i], nums[j], nums[k]};
					Triplets.Add(triplet);
					j++;
					while (j < k)
					{
						if ( nums[j] == nums[j-1])
						{
							j++;
						}
					}
				}
			}
		}
		return Triplets;
	}
}




			
