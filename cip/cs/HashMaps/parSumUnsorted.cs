// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public static void Main(string[] args)
    {
        List<int> nums = new List<int>{-1, 3, 4, 2};
        int target = 3;
        List<int> result = pairSumUnsorted(nums, target);
        Console.WriteLine($"[{string.Join(", ", result)}]");
        
    }
    public static List<int> pairSumUnsorted(List<int> nums, int target)
    {
        Dictionary<int,int> numMap = new Dictionary<int, int>();
        int i;
        for (i = 0; i < nums.Count(); i++)
        {
            numMap[nums[i]] = i;
        }
        i = 0;
        for (i = 0; i < nums.Count(); i++)
        {
            int b;
            b = target - nums[i];
            if (numMap.ContainsKey(b) && numMap[b] != i)
            {
                List<int> result = new List<int>{i, numMap[b]};
                return result;
            }
            
            
        }
        List<int> resulte = new List<int>();
        return resulte;
        
    }
}