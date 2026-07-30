/*
Given a string of lowercase English letters, rearrange the characters to form a new string representing the next immediate sequence in lexicographical (alphabetical) order. If the given string is already last in lexicographical order among all possible arrangements, return the arrangement that's first in lexicographical order.
Input = "abcd"
Output: "abdc"
*/

using System;
using System.Linq;
using System.Colllections.Generic;

public class Solution
{
	public void static main(string[] args)
	{
		string s = 'abcd';
		string result = nextLexicoGraphicalSeq(s);
		Console.WriteLine(result);
	}

	public static string nextLexicoGraphicalSeq(string s)
	{
		if (s == null || s.Length == 0)
		{
			return "";
		}

		int n = s.Length;
		char[] new_s = s.ToCharArray();
		int i = n-1;
		while (i > 0 && new_s[i-1] >= new_s[i])
		{
			i--;
		}
		if (i == 0)
		{
			Array.Reverse(new_s);
			return new String(new_s);
		}
		int pivot = i -1;
		i = n-1;
		
		while (new_s[pivot] <= new_s[i])
		{
			i--;
		}
		char[] slice = new_s[pivot..];
		Array.Reverse(slice);
		for (int j = 0; j < slice.Length; j++)
		{
			new_s[pivot + j] = slice[j];
		}
		string result = new String(new_s);
		return result;
	}
}

		

