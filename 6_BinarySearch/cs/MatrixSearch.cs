/*
Matrix Search

Determine if a target value exists in a matrix.
Each row of the matrix is sorted in non-decreasing order, and the first value
of each row is greater than or equal to the last value of the previous row.

Example:
matrix = [[2, 3, 4, 6], [7, 10, 11, 17], [20, 21, 24, 33]]
target = 21
Output: true
*/

using System;

public class Solution
{
    public static bool MatrixSearch(int[][] matrix, int target)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(
            new int[][]
            {
                new int[] { 2, 3, 4, 6 },
                new int[] { 7, 10, 11, 17 },
                new int[] { 20, 21, 24, 33 }
            },
            21,
            true,
            "Test 1"
        );

        RunTest(
            new int[][]
            {
                new int[] { 1, 3, 5 },
                new int[] { 7, 9, 11 },
                new int[] { 13, 15, 17 }
            },
            8,
            false,
            "Test 2"
        );

        RunTest(
            new int[][]
            {
                new int[] { 5 }
            },
            5,
            true,
            "Test 3"
        );

        RunTest(
            new int[][]
            {
                new int[] { 1, 2, 3, 4 }
            },
            4,
            true,
            "Test 4"
        );

        RunTest(
            new int[][]
            {
                new int[] { 1, 2, 3 },
                new int[] { 3, 4, 5 },
                new int[] { 6, 7, 8 }
            },
            9,
            false,
            "Test 5"
        );
    }

    private static void RunTest(int[][] matrix, int target, bool expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("matrix:");
        PrintMatrix(matrix);
        Console.WriteLine("target   = " + target);
        Console.WriteLine("expected = " + expected);

        try
        {
            bool actual = MatrixSearch(matrix, target);
            Console.WriteLine("actual   = " + actual);
            Console.WriteLine("pass     = " + (actual == expected));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static void PrintMatrix(int[][] matrix)
    {
        if (matrix == null)
        {
            Console.WriteLine("null");
            return;
        }

        for (int i = 0; i < matrix.Length; i++)
        {
            Console.WriteLine("[" + string.Join(", ", matrix[i]) + "]");
        }
    }
}