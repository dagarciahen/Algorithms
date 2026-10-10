/*
Linked List Loop

Given a singly linked list, determine if it contains a cycle.
A cycle occurs if a node's next pointer references an earlier node in the linked list,
causing a loop.

Example:
Input: head = [[1, 2, 3, 4, 5, 6], 2]
Output: true

The second value represents the index that the tail connects to.
If it is -1, the list has no cycle.
*/

using System;

public class ListNode
{
    public int val;
    public ListNode next;

    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution
{
    public static bool HasCycle(ListNode head)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 1, 2, 3, 4, 5, 6 }, 2, true, "Test 1");
        RunTest(new int[] { 1, 2, 3, 4 }, -1, false, "Test 2");
        RunTest(new int[] { 7 }, 0, true, "Test 3");
        RunTest(new int[] { 9, 8 }, 0, true, "Test 4");
        RunTest(new int[] { 5, 1, 4, 2, 3 }, -1, false, "Test 5");
    }

    private static void RunTest(int[] values, int cycleIndex, bool expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("head     = [" + FormatArray(values) + ", " + cycleIndex + "]");
        Console.WriteLine("expected = " + expected);

        try
        {
            ListNode head = BuildList(values, cycleIndex);
            bool actual = HasCycle(head);
            Console.WriteLine("actual   = " + actual);
            Console.WriteLine("pass     = " + (actual == expected));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static ListNode BuildList(int[] values, int cycleIndex)
    {
        if (values == null || values.Length == 0)
        {
            return null;
        }

        ListNode[] nodes = new ListNode[values.Length];

        for (int i = 0; i < values.Length; i++)
        {
            nodes[i] = new ListNode(values[i]);
        }

        for (int i = 0; i < values.Length - 1; i++)
        {
            nodes[i].next = nodes[i + 1];
        }

        if (cycleIndex >= 0)
        {
            nodes[values.Length - 1].next = nodes[cycleIndex];
        }

        return nodes[0];
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