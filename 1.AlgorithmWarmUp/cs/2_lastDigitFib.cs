using System;
using System.Collections.Generic;

class Program
{
	static void Main()
	{
		int n = int.Parse(Console.ReadLine());
		if ( n <=1)
		{
			Console.WriteLine(n);
			return;
		}

		List<int> F = new List<int> {0,1};

		for (int i = 2; i <= n; i++)
		{
			int last_digit_next_value = (F[i-1]% 10 +  F[i-2] % 10)% 10;
			F.Add(last_digit_next_value);
		}
		Console.WriteLine(F[n]);
	}
}

			




