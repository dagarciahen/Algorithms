/*
You are given an array of numbers, each representing the height of a vertical line on a graph. A container can be formed with any pair of these lines, along with the x-axis of the graph. 
    Return the amount of water which the largest container can hold.

*/
using System;
using System.Linq;
using System.Collections.Generic;
public class Solution
{
    public static void Main(string[] args)
    {
        List<int> heights = new List<int>{ 7, 8, 3, 7, 6};
        int result = LargestContainer(heights);
        Console.WriteLine(result);
    }
    public static int LargestContainer(List<int> heights)
    {
        if (heights == null || heights.Count() == 0) {return 0;}
        int n = heights.Count();
        
        int water = 0;

        int i = 0;
        int j = n-1;
        while (i < j)
        {
            int new_water = CalculateWater(heights, i, j);
            water = Math.Max(water, new_water);
            if (heights[i] > heights[j])
            {
                j--;
            }
            else if (heights[i] <= heights[j])
            {
                i++;
            }
        
        }
        return water;
    }
    public static int CalculateWater(List<int> heights, int i, int j)
    {
        int area = Math.Min(heights[i], heights[j])*(j-i);
        return area;
        
    }
}