/*
Given a partially completed 9x9 Sudoku board, determine if the current state of the board
adheres to the rules of the game:

Each row and column must contain unique numbers between 1 and 9, or be empty
(represented as 0).

Each of the nine 3x3 subgrids must contain unique numbers between 1 and 9, or be empty.

Note: You are asked to determine whether the current state of the board is valid
given these rules, not whether the board is solvable.

Example:
Output: false
*/

using System;

public class Solution
{
    public static bool VerifySudokuBoard(int[][] board)
    {
        HashSet<int>[] rowSets = new HashSet<int>[3];
        HashSet<int>[] colSets = new HashSet<int>[3];
        HashSet<int>[][] subGridSets =new HashSet<int>[3][];
        //HashSet<int>[,] subGridSets = new HashSet<int>[3,3];

        for (int i = 0; i < 9; i++)
        {
            rowSets[i] = new();
            colSets[i] = new();
        }
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                subGridSets[i][j] = new();
            }
        }
        for(int r; r < 9; r++)
        {
            for (int c; c <9 ; c++)
            {
                int num = board[r][c];
                if (num == 0){continue;}
                if (rowSets[r].Contains(num) || colSets[c].Contains(num)|| subGridSets[r / 3][c / 3].Contains(num))
                {
                    return false;
                }
                rowSets[r].Add(num);
                colSets[c].Add(num);
                subGridSets[r/3][c/3].Add(num);
            }

        }
        return true;
        
    }

    public static void Main(string[] args)
    {
        RunTest(
            new int[][]
            {
                new int[] { 5, 3, 0, 0, 7, 0, 0, 0, 0 },
                new int[] { 6, 0, 0, 1, 9, 5, 0, 0, 0 },
                new int[] { 0, 9, 8, 0, 0, 0, 0, 6, 0 },
                new int[] { 8, 0, 0, 0, 6, 0, 0, 0, 3 },
                new int[] { 4, 0, 0, 8, 0, 3, 0, 0, 1 },
                new int[] { 7, 0, 0, 0, 2, 0, 0, 0, 6 },
                new int[] { 0, 6, 0, 0, 0, 0, 2, 8, 0 },
                new int[] { 0, 0, 0, 4, 1, 9, 0, 0, 5 },
                new int[] { 0, 0, 0, 0, 8, 0, 0, 7, 9 }
            },
            true,
            "Test 1"
        );

        RunTest(
            new int[][]
            {
                new int[] { 5, 3, 5, 0, 7, 0, 0, 0, 0 },
                new int[] { 6, 0, 0, 1, 9, 5, 0, 0, 0 },
                new int[] { 0, 9, 8, 0, 0, 0, 0, 6, 0 },
                new int[] { 8, 0, 0, 0, 6, 0, 0, 0, 3 },
                new int[] { 4, 0, 0, 8, 0, 3, 0, 0, 1 },
                new int[] { 7, 0, 0, 0, 2, 0, 0, 0, 6 },
                new int[] { 0, 6, 0, 0, 0, 0, 2, 8, 0 },
                new int[] { 0, 0, 0, 4, 1, 9, 0, 0, 5 },
                new int[] { 0, 0, 0, 0, 8, 0, 0, 7, 9 }
            },
            false,
            "Test 2"
        );

        RunTest(
            new int[][]
            {
                new int[] { 5, 3, 0, 0, 7, 0, 0, 0, 0 },
                new int[] { 6, 0, 0, 1, 9, 5, 0, 0, 0 },
                new int[] { 5, 9, 8, 0, 0, 0, 0, 6, 0 },
                new int[] { 8, 0, 0, 0, 6, 0, 0, 0, 3 },
                new int[] { 4, 0, 0, 8, 0, 3, 0, 0, 1 },
                new int[] { 7, 0, 0, 0, 2, 0, 0, 0, 6 },
                new int[] { 0, 6, 0, 0, 0, 0, 2, 8, 0 },
                new int[] { 0, 0, 0, 4, 1, 9, 0, 0, 5 },
                new int[] { 0, 0, 0, 0, 8, 0, 0, 7, 9 }
            },
            false,
            "Test 3"
        );

        RunTest(
            new int[][]
            {
                new int[] { 3, 0, 6, 0, 5, 8, 4, 0, 0 },
                new int[] { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
                new int[] { 1, 0, 2, 5, 0, 0, 3, 2, 0 },
                new int[] { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
                new int[] { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
                new int[] { 0, 1, 0, 0, 0, 0, 0, 7, 4 },
                new int[] { 0, 3, 0, 0, 0, 8, 2, 5, 0 },
                new int[] { 0, 0, 5, 2, 0, 6, 0, 0, 0 }
            },
            false,
            "Test Sudoku"
        );

        RunTest(
            new int[][]
            {
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                new int[] { 0, 0, 0, 0, 0, 0, 0, 0, 0 }
            },
            true,
            "Test 5"
        );
    }

    private static void RunTest(int[][] board, bool expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("board:");
        PrintBoard(board);
        Console.WriteLine("expected = " + expected);

        try
        {
            bool actual = VerifySudokuBoard(board);
            Console.WriteLine("actual   = " + actual);
            Console.WriteLine("pass     = " + (actual == expected));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static void PrintBoard(int[][] board)
    {
        if (board == null)
        {
            Console.WriteLine("null");
            return;
        }

        for (int r = 0; r < board.Length; r++)
        {
            Console.WriteLine("[" + string.Join(", ", board[r]) + "]");
        }
    }
}


/*
SOLUTON WITH LINQ


using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public static bool VerifySudokuBoard(int[][] board)
    {
        HashSet<int>[] rowSets = Enumerable.Range(0, 9)
            .Select(_ => new HashSet<int>())
            .ToArray();

        HashSet<int>[] colSets = Enumerable.Range(0, 9)
            .Select(_ => new HashSet<int>())
            .ToArray();

        HashSet<int>[][] subgridSets = Enumerable.Range(0, 3)
            .Select(_ => Enumerable.Range(0, 3)
                .Select(_ => new HashSet<int>())
                .ToArray())
            .ToArray();

        for (int r = 0; r < 9; r++)
        {
            for (int c = 0; c < 9; c++)
            {
                int num = board[r][c];

                if (num == 0)
                {
                    continue;
                }

                if (rowSets[r].Contains(num))
                {
                    return false;
                }

                if (colSets[c].Contains(num))
                {
                    return false;
                }

                if (subgridSets[r / 3][c / 3].Contains(num))
                {
                    return false;
                }

                rowSets[r].Add(num);
                colSets[c].Add(num);
                subgridSets[r / 3][c / 3].Add(num);
            }
        }

        return true;
    }
}
*/