/*
Linked List Midpoint

Given a singly linked list, find and return its middle node.
If there are two middle nodes, return the second one.

Example 1:
Input: head = [1, 2, 4, 7, 3]
Output: Node 4

Example 2:
Input: head = [1, 2, 4, 7, 3, 9]
Output: Node 7

Constraints:
The linked list contains at least one node.
The linked list contains unique values.
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
    public static ListNode FindMidpoint(ListNode head)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 1, 2, 4, 7, 3 }, 4, "Test 1");
        RunTest(new int[] { 1, 2, 4, 7, 3, 9 }, 7, "Test 2");
        RunTest(new int[] { 5 }, 5, "Test 3");
        RunTest(new int[] { 8, 6, 4, 2 }, 4, "Test 4");
        RunTest(new int[] { 10, 20, 30, 40, 50, 60, 70 }, 40, "Test 5");
    }

    private static void RunTest(int[] input, int expectedValue, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("head     = " + FormatArray(input));
        Console.WriteLine("expected = Node " + expectedValue);

        try
        {
            ListNode head = BuildList(input);
            ListNode actual = FindMidpoint(head);
            Console.WriteLine("actual   = " + FormatNode(actual));
            Console.WriteLine("pass     = " + (actual != null && actual.val == expectedValue));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static ListNode BuildList(int[] values)
    {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        for (int i = 0; i < values.Length; i++)
        {
            current.next = new ListNode(values[i]);
            current = current.next;
        }

        return dummy.next;
    }

    private static string FormatNode(ListNode node)
    {
        if (node == null)
        {
            return "null";
        }

        return "Node " + node.val;
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