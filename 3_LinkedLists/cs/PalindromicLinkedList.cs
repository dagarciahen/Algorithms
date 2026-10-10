/*
Palindromic Linked List

Given the head of a singly linked list, determine if it's a palindrome.

Example 1:
Input: head = [1, 2, 3, 2, 1]
Output: true

Example 2:
Input: head = [1, 2, 3]
Output: false
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
    public static bool IsPalindrome(ListNode head)
    {
        throw new NotImplementedException();
    }

    public static void Main(string[] args)
    {
        RunTest(new int[] { 1, 2, 3, 2, 1 }, true, "Test 1");
        RunTest(new int[] { 1, 2, 2, 1 }, true, "Test 2");
        RunTest(new int[] { 1, 2, 3 }, false, "Test 3");
        RunTest(new int[] { 7 }, true, "Test 4");
        RunTest(new int[] { 4, 5, 4, 6 }, false, "Test 5");
    }

    private static void RunTest(int[] input, bool expected, string testName)
    {
        Console.WriteLine(testName);
        Console.WriteLine("head     = " + FormatArray(input));
        Console.WriteLine("expected = " + expected);

        try
        {
            ListNode head = BuildList(input);
            bool actual = IsPalindrome(head);
            Console.WriteLine("actual   = " + actual);
            Console.WriteLine("pass     = " + (actual == expected));
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

    private static string FormatArray(int[] values)
    {
        if (values == null)
        {
            return "null";
        }

        return "[" + string.Join(", ", values) + "]";
    }
}