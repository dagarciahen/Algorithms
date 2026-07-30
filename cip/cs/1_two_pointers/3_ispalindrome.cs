/*
A palindrome is a sequence of characters that reads the same forward and backward.


/*
A palindrome is a sequence of characters that reads the same forward and backward.

Given a string, determine if it's a palindrome after removing all non-alphanumeric characters. A character is alphanumeric if it's either a letter or a number.
*/
using System;
using System.Linq;
public class Solution
{
	public static void Main(string[] args)
	{
		string s = "a dog! a panic in a pagoda.";

		bool result = isPalindrome(s);
		Console.WriteLine(result);
	}
		public static bool isPalindrome(string s)
		{
			string new_s = "";
			int n = s.Length;
			for (int i = 0; i < n; i++)
			{
				if (char.IsLetterOrDigit(s[i]))
				{
					new_s = new_s + s[i];
				}
			}
			n = new_s.Length;
			int j = 0;
			int k = n -1;
				while(j < k)
				{
					if (new_s[j] == new_s[k])
					{
						j++;
						k--;
					}
					else
					{
						return false;
					}
				}
			return true;
		}

}

