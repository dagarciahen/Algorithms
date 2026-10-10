/*
Cutting Wood

You are given an array representing the heights of trees, and an integer k
representing the total length of wood that needs to be cut.

For this task, a woodcutting machine is set to a certain height, H.
The machine cuts off the top part of all trees taller than H, while trees
shorter than H remain untouched. Determine the highest possible setting of
the woodcutter so that it cuts at least k meters of wood.

Assume the woodcutter cannot be set higher than the height of the tallest
tree in the array.

Example:
Input: heights = [2, 6, 3, 8], k = 7
Output: 3
*/

using System;

public class Solution
{
    public static int CuttingWood(int[] heights, int k)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 2, 6, 3, 8 }, 7, 3, "Test 1");
        RunTest(new int[] { 5, 7, 9 }, 4, 5, "Test 2");
        RunTest(new int[] { 10, 10, 10 }, 6, 8, "Test 3");
        RunTest(new int[] { 1, 2, 3, 4 }, 0, 4, "Test 4");
        RunTest(new int[] { 4, 12, 7, 10 }, 11, 5, "Test 5");
    }

    private static void RunTest(int[] heights, int k, int expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("heights  = " + FormatArray(heights));
        Console.WriteLine("k        = " + k);
        Console.WriteLine("expected = " + expected);

        try
        {
            int actual = CuttingWood(heights, k);
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