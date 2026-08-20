using System;
using System.Collections.Generic;
using System.Linq;

public class ListNode {
	public int _val;
	public ListNode next;

	public ListNode(int val)
	{
		_val = val;
	}

}
public class Solution
{
	static ListNode removeKNode(ListNode head, int k)
	{
		ListNode dummy = new ListNode(-1);
		dummy.next = head;
		ListNode lead = dummy;
		ListNode trailer = dummy;
	

		for (int j = 0; j < k; j++)
		{
			lead = lead.next;
		}

		while (lead.next != null)
		{
			lead = lead.next;
			trailer = trailer.next;
		}
		
		trailer.next = trailer.next.next;
		return dummy.next;



	}

	public static void Main(string[] args)
	{
		ListNode head = BuildList(new[] {1,2, 4, 7, 3 });
		head = removeKNode(head, 2);
		PrintList(head);
	}
	static ListNode BuildList(int[] values)
	{
		ListNode head = new ListNode(values[0]);
		ListNode current = head;

		for (int i = 1; i < values.Length; i++)
		{
			current.next = new ListNode(values[i]);
			current = current.next;
		}
		return head;

	}
	static void PrintList(ListNode head)
	{
		while (head != null)
		{
			Console.WriteLine($"{head._val} -> ");
			head = head.next;

		}
		Console.WriteLine("null");
	}
	

}




