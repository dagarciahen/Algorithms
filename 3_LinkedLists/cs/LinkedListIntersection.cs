/*
Linked List Intersection

Return the node where two singly linked lists intersect.
If the linked lists don't intersect, return null.

Example:
head_A = [1, 3, 4, 8, 7, 2]
head_B = [6, 4, 8, 7, 2]
skip_A = 3
skip_B = 2
Output: Node 8

How the custom test cases work:
The input is designed to describe how the two input linked lists intersect.

skip_A: The number of nodes to skip in list A from the head to reach the intersection node.
skip_B: The number of nodes to skip in list B from the head to reach the intersection node.

For a linked list with no intersection, set skip_A and skip_B to the length
of their respective linked lists.
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
    public static ListNode GetIntersectionNode(ListNode headA, ListNode headB)
    {
        ListNode pointA = headA;
        ListNode pointB = headB;

        while (pointA != pointB)
        {
            pointA = pointA.next != null ? pointA.next : headB;
            pointB = pointB.next != null ? pointB.next : headA;


        }
        return pointA;
     }

    public static void Main(string[] args)
    {
        RunTest(
            new int[] { 1, 3, 4, 8, 7, 2 },
            new int[] { 6, 4, 8, 7, 2 },
            3,
            2,
            8,
            "Test 1"
        );

        RunTest(
            new int[] { 1, 2, 3 },
            new int[] { 4, 5, 6 },
            3,
            3,
            null,
            "Test 2"
        );

        RunTest(
            new int[] { 9, 8, 7 },
            new int[] { 8, 7 },
            1,
            0,
            8,
            "Test 3"
        );

        RunTest(
            new int[] { 5, 1, 2, 3 },
            new int[] { 9, 2, 3 },
            2,
            1,
            2,
            "Test 4"
        );

        RunTest(
            new int[] { 4, 6, 1 },
            new int[] { 1 },
            2,
            0,
            1,
            "Test 5"
        );
    }

    private static void RunTest(int[] valuesA, int[] valuesB, int skipA, int skipB, int? expectedValue, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("head_A   = " + FormatArray(valuesA));
        Console.WriteLine("head_B   = " + FormatArray(valuesB));
        Console.WriteLine("skip_A   = " + skipA);
        Console.WriteLine("skip_B   = " + skipB);
        Console.WriteLine("expected = " + FormatNodeValue(expectedValue));

        try
        {
            ListNode[] lists = BuildIntersectingLists(valuesA, valuesB, skipA, skipB);
            ListNode actual = GetIntersectionNode(lists[0], lists[1]);
            Console.WriteLine("actual   = " + FormatNode(actual));
            Console.WriteLine("pass     = " + AreEqual(actual, expectedValue));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static ListNode[] BuildIntersectingLists(int[] valuesA, int[] valuesB, int skipA, int skipB)
    {
        ListNode[] nodesA = BuildNodes(valuesA);
        ListNode[] nodesB = BuildNodes(valuesB);

        ListNode headA = nodesA.Length > 0 ? nodesA[0] : null;
        ListNode headB = nodesB.Length > 0 ? nodesB[0] : null;

        if (skipA < valuesA.Length && skipB < valuesB.Length)
        {
            ListNode intersection = nodesA[skipA];

            if (skipB == 0)
            {
                headB = intersection;
            }
            else
            {
                nodesB[skipB - 1].next = intersection;
            }
        }

        return new ListNode[] { headA, headB };
    }

    private static ListNode[] BuildNodes(int[] values)
    {
        if (values.Length == 0)
        {
            return new ListNode[0];
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

        return nodes;
    }

    private static string FormatNode(ListNode node)
    {
        if (node == null)
        {
            return "null";
        }

        return "Node " + node.val;
    }

    private static string FormatNodeValue(int? value)
    {
        if (value == null)
        {
            return "null";
        }

        return "Node " + value.Value;
    }

    private static bool AreEqual(ListNode node, int? expectedValue)
    {
        if (node == null || expectedValue == null)
        {
            return node == null && expectedValue == null;
        }

        return node.val == expectedValue.Value;
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