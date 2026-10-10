/*
Reverse a singly linked list.

Example:
Input: head = [1, 2, 4, 7, 3]
Output: [3, 7, 4, 2, 1]
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
    public static ListNode ReverseLinkedList(ListNode head)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 1, 2, 4, 7, 3 }, new int[] { 3, 7, 4, 2, 1 }, "Test 1");
        RunTest(new int[] { 1 }, new int[] { 1 }, "Test 2");
        RunTest(new int[] { }, new int[] { }, "Test 3");
        RunTest(new int[] { 5, 6 }, new int[] { 6, 5 }, "Test 4");
        RunTest(new int[] { 9, 8, 7, 6 }, new int[] { 6, 7, 8, 9 }, "Test 5");
    }

    private static void RunTest(int[] input, int[] expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("input    = " + FormatArray(input));
        Console.WriteLine("expected = " + FormatArray(expected));

        try
        {
            ListNode head = BuildList(input);
            ListNode actual = ReverseLinkedList(head);
            Console.WriteLine("actual   = " + FormatList(actual));
            Console.WriteLine("pass     = " + (FormatList(actual) == FormatArray(expected)));
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

    private static string FormatList(ListNode head)
    {
        if (head == null)
        {
            return "[]";
        }

        System.Collections.Generic.List<int> values = new System.Collections.Generic.List<int>();
        ListNode current = head;

        while (current != null)
        {
            values.Add(current.val);
            current = current.next;
        }

        return "[" + string.Join(", ", values) + "]";
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