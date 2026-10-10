/*
Flatten a Multi-Level Linked List

In a multi-level linked list, each node has a next pointer and a child pointer.
Flatten the structure into a single-level linked list by linking the end of each level
to the start of the next one.

Example:
Input:
[
  [1, []],
  [2, []],
  [3, [[6, []], [7, [[10, []]]]]],
  [4, [[8, [[11, []]]]]],
  [5, [[9, []]]]
]

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
*/

using System;
using System.Collections.Generic;

public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode child;

    public ListNode(int val = 0, ListNode next = null, ListNode child = null)
    {
        this.val = val;
        this.next = next;
        this.child = child;
    }
}

public class Solution
{
    public static ListNode FlattenLinkedList(ListNode head)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(BuildTest1(), new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 }, "Test 1");
        RunTest(BuildTest2(), new int[] { 1, 2, 3 }, "Test 2");
        RunTest(BuildTest3(), new int[] { 1, 2, 3, 4, 5 }, "Test 3");
        RunTest(BuildTest4(), new int[] { 7 }, "Test 4");
        RunTest(BuildTest5(), new int[] { 1, 2, 3, 4, 5, 6, 7, 8 }, "Test 5");
    }

    private static void RunTest(ListNode head, int[] expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("expected = " + FormatArray(expected));

        try
        {
            ListNode actual = FlattenLinkedList(head);
            Console.WriteLine("actual   = " + FormatList(actual));
            Console.WriteLine("pass     = " + (FormatList(actual) == FormatArray(expected)));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static ListNode BuildTest1()
    {
        ListNode n1 = new ListNode(1);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(3);
        ListNode n4 = new ListNode(4);
        ListNode n5 = new ListNode(5);
        ListNode n6 = new ListNode(6);
        ListNode n7 = new ListNode(7);
        ListNode n8 = new ListNode(8);
        ListNode n9 = new ListNode(9);
        ListNode n10 = new ListNode(10);
        ListNode n11 = new ListNode(11);

        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = n5;

        n3.child = n6;
        n6.next = n7;

        n4.child = n8;
        n5.child = n9;

        n7.child = n10;
        n8.child = n11;

        return n1;
    }

    private static ListNode BuildTest2()
    {
        ListNode n1 = new ListNode(1);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(3);

        n1.next = n2;
        n2.next = n3;

        return n1;
    }

    private static ListNode BuildTest3()
    {
        ListNode n1 = new ListNode(1);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(3);
        ListNode n4 = new ListNode(4);
        ListNode n5 = new ListNode(5);

        n1.child = n2;
        n2.child = n3;
        n3.child = n4;
        n4.child = n5;

        return n1;
    }

    private static ListNode BuildTest4()
    {
        return new ListNode(7);
    }

    private static ListNode BuildTest5()
    {
        ListNode n1 = new ListNode(1);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(3);
        ListNode n4 = new ListNode(4);
        ListNode n5 = new ListNode(5);
        ListNode n6 = new ListNode(6);
        ListNode n7 = new ListNode(7);
        ListNode n8 = new ListNode(8);

        n1.next = n2;
        n2.next = n3;
        n3.next = n4;

        n1.child = n5;
        n2.child = n6;
        n5.child = n7;
        n6.child = n8;

        return n1;
    }

    private static string FormatList(ListNode head)
    {
        if (head == null)
        {
            return "[]";
        }

        List<int> values = new List<int>();
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