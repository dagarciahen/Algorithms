using System;
using System.Collections.generic;

int n = int.Parse(Console.ReadLine());

class Program 
{
	static void Main()
	{
		int n = int.Parse(Console.ReadLine());
		Console.WriteLine(Fibonacci(n));
	}

	private static int Fibonacci(int n)
	{
		if ( n<=1) 
		{
			return n;
		}
		else
		{
			return Fibonacci(n-1) + Fibonacci(n-2);
		}
	}
}
