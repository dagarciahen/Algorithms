/*
You are given an array of numbers, each representing the height of a vertical line on a graph. A container can be formed with any pair of these lines, along with the x-axis of the graph. 
    Return the amount of water which the largest container can hold.

Input: heights = [2, 7, 8, 3, 7, 6]
Output: 24

*/
using System;
using System.Collections.Generic;

public class Solution
{
    public static int LargestContainer(List<int> heights)
    {
        int i = 0;
        int len = heights.Count;
        int j = len-1;
        int water = 0;
        
        while (i < j)
        {
            int new_water = calculateWater(heights, i, j);
            if (heights[i] <= heights[j])
            {
                i++;
            } else {j--;}
            water = new_water > water ? new_water : water;


        }
        return water;
    }
    private static int calculateWater(List<int> heights, int i, int j)
    {
        int width = j - i;
        int height = Math.Min(heights[i], heights[j]);
        int area = width*height;
        return area;
    }

    public static void Main(string[] args)
    {
        RunTest(new List<int> { 2, 7, 8, 3, 7, 6 }, 24, "Test 1");
        RunTest(new List<int> { 1, 1 }, 1, "Test 2");
        RunTest(new List<int> { 1, 8, 6, 2, 5, 4, 8, 3, 7 }, 49, "Test 3");
        RunTest(new List<int> { 4, 3, 2, 1, 4 }, 16, "Test 4");
        RunTest(new List<int> { 1, 2, 1 }, 2, "Test 5");
    }

    private static void RunTest(List<int> heights, int expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("heights  = " + FormatList(heights));
        Console.WriteLine("expected = " + expected);

        try
        {
            int actual = LargestContainer(new List<int>(heights));
            Console.WriteLine("actual   = " + actual);
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static string FormatList(List<int> values)
    {
        if (values == null)
        {
            return "null";
        }

        return "[" + string.Join(", ", values) + "]";
    }
}