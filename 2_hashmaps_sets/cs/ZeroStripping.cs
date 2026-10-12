/*
For each zero in an m x n matrix, set its entire row and column to zero in place.

Input: matrix = [[1,2,3,4,5],[6,0,6,9,10],[11,12,13,14,15],[16,17,18,19,0]]
Output: [[1,0,3,4,0],[0,0,0,0,0],[11,0,13,14,0],[0,0,0,0,0]]
*/

using System;
using System.Linq;

public class Solution
{
    public static int[][] SetZeroes(int[][] matrix)
    {
        bool firstRowWithZeros = false;
        int m = matrix.Length;
        int n = matrix[0].Length;
        for(int i= 0; i < n; i++)
        {
            if (matrix[0][i] == 0)
            {
                firstRowWithZeros = true;
                break;
            }
            
        }
        bool firstColWithZeros = false;
        for (int i = 0; i <m; i++)
        {
            if (matrix[i][0] == 0)
            {
                firstColWithZeros = true;
                break;
            }
        }
        //mark
        for (int i = 1; i< m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }

            }
        }
        //ztripping
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j <n; j++)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
        }
        if (firstRowWithZeros)
        {
            for (int i = 0; i < n; i++)
            {
                matrix[0][i] = 0;
            }
        }
        if (firstColWithZeros)
        Array.ForEach(Enumerable.Range(0, m).ToArray(), i=> matrix[i][0] =0);

        return matrix;

    }




    public static void Main(string[] args)
    {
        RunTest(
            new int[][]
            {
                new int[] { 1, 2, 3, 4, 5 },
                new int[] { 6, 0, 6, 9, 10 },
                new int[] { 11, 12, 13, 14, 15 },
                new int[] { 16, 17, 18, 19, 0 }
            },
            new int[][]
            {
                new int[] { 1, 0, 3, 4, 0 },
                new int[] { 0, 0, 0, 0, 0 },
                new int[] { 11, 0, 13, 14, 0 },
                new int[] { 0, 0, 0, 0, 0 }
            },
            "Test 1"
        );

        RunTest(
            new int[][]
            {
                new int[] { 1, 2, 3 },
                new int[] { 4, 5, 6 },
                new int[] { 7, 8, 9 }
            },
            new int[][]
            {
                new int[] { 1, 2, 3 },
                new int[] { 4, 5, 6 },
                new int[] { 7, 8, 9 }
            },
            "Test 2"
        );

        RunTest(
            new int[][]
            {
                new int[] { 0, 1 },
                new int[] { 2, 3 }
            },
            new int[][]
            {
                new int[] { 0, 0 },
                new int[] { 0, 3 }
            },
            "Test 3"
        );

        RunTest(
            new int[][]
            {
                new int[] { 1, 2, 0 },
                new int[] { 4, 5, 6 },
                new int[] { 7, 8, 9 }
            },
            new int[][]
            {
                new int[] { 0, 0, 0 },
                new int[] { 4, 5, 0 },
                new int[] { 7, 8, 0 }
            },
            "Test 4"
        );

        RunTest(
            new int[][]
            {
                new int[] { 1, 0, 3 },
                new int[] { 0, 5, 6 },
                new int[] { 7, 8, 9 }
            },
            new int[][]
            {
                new int[] { 0, 0, 0 },
                new int[] { 0, 0, 0 },
                new int[] { 0, 0, 9 }
            },
            "Test 5"
        );
    }

    private static void RunTest(int[][] matrix, int[][] expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("input:");
        PrintMatrix(matrix);
        Console.WriteLine("expected:");
        PrintMatrix(expected);

        try
        {
            int[][] actual = CopyMatrix(matrix);
            SetZeroes(actual);
            Console.WriteLine("actual:");
            PrintMatrix(actual);
            Console.WriteLine("pass     = " + AreEqual(actual, expected));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static int[][] CopyMatrix(int[][] matrix)
    {
        int[][] copy = new int[matrix.Length][];
        for (int i = 0; i < matrix.Length; i++)
        {
            copy[i] = new int[matrix[i].Length];
            Array.Copy(matrix[i], copy[i], matrix[i].Length);
        }

        return copy;
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

    private static bool AreEqual(int[][] left, int[][] right)
    {
        if (left == null || right == null)
        {
            return left == right;
        }

        if (left.Length != right.Length)
        {
            return false;
        }

        for (int i = 0; i < left.Length; i++)
        {
            if (left[i].Length != right[i].Length)
            {
                return false;
            }

            for (int j = 0; j < left[i].Length; j++)
            {
                if (left[i][j] != right[i][j])
                {
                    return false;
                }
            }
        }

        return true;
    }
}

/*
public class Solution
{
    public static int[][] SetZeroes(int[][] matrix)
    {
        bool firstRowWithZeros = false;
        int m = matrix.Length;
        int n = matrix[0].Length;
        for(int i= 0; i < n; i++)
        {
            if (matrix[0][i] == 0)
            {
                firstRowWithZeros = true;
                break;
            }
            
        }
        bool firstColWithZeros = false;
        for (int i = 0; i <m; i++)
        {
            if (matrix[i][0] == 0)
            {
                firstColWithZeros = true;
                break;
            }
        }
        //mark
        for (int i = 1; i< m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }

            }
        }
        //ztripping
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j <n; j++)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
        }
        if (firstRowWithZeros)
        {
            for (int i = 0; i < n; i++)
            {
                matrix[0][i] = 0;
            }
        }
        if (firstColWithZeros)
        Array.ForEach(Enumerable.Range(0, m).ToArray(), i=> matrix[i][0] =0);

        return matrix;

    }



*/
