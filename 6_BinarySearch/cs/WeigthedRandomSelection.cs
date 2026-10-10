/*
Weighted Random Selection

Given an array of items, each with a corresponding weight, implement a function
that randomly selects an item from the array, where the probability of selecting
any item is proportional to its weight.

In other words, the probability of picking the item at index i is:
weights[i] / sum(weights)

Return the index of the selected item.

Example:
Input: weights = [3, 1, 2, 4]

Explanation:
sum(weights) = 10
Index 0 has probability 3/10
Index 1 has probability 1/10
Index 2 has probability 2/10
Index 3 has probability 4/10

For example, we expect index 0 to be returned about 30% of the time.

Constraints:
The weights array contains at least one element.
*/

using System;

public class Solution
{
    public static int WeightedRandomSelection(int[] weights)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunBasicTest(new int[] { 3, 1, 2, 4 }, "Test 1");
        RunBasicTest(new int[] { 1 }, "Test 2");
        RunBasicTest(new int[] { 10, 10, 10 }, "Test 3");
        RunBasicTest(new int[] { 5, 100 }, "Test 4");
        RunBasicTest(new int[] { 2, 4, 6, 8, 10 }, "Test 5");
    }

    private static void RunBasicTest(int[] weights, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("weights   = " + FormatArray(weights));
        Console.WriteLine("expected  = a valid index between 0 and " + (weights.Length - 1));

        try
        {
            int actual = WeightedRandomSelection(weights);
            Console.WriteLine("actual    = " + actual);
            Console.WriteLine("pass      = " + (actual >= 0 && actual < weights.Length));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual    = not implemented");
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