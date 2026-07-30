using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
	public static void Main(string[] args)
	{
		List<int> nums = new List<int>{0, 1, 0, 3,2};
		shiftZerosToEnd(nums);
		Console.WriteLine("[" + string.Join(",", nums) + "]");

	}
	public static void shiftZerosToEnd(List<int> nums)
	{
		if (nums.Count() == 0 || nums == null)
		{
			return;
		}
		int n = nums.Count();

		int i = 0;
		for (int j = 0; j < n; j++)
		{
			if (nums[j] != 0)
			{
				(nums[i], nums[j]) = (nums[j], nums[i]);
				i++;
			}
		}
	}
}

