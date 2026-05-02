using System;

class Program 
{
	static void Main()
	{
		string line = Console.ReadLine();
		string [] parts = line.Split(' ');
		int a = int.Parse(parts[0]);
		int b = int.Parse(parts[1]);
		Console.WriteLine(Gcd(a,b));
	}

	static int Gcd(int a, int b) 
	{
		while (b != 0)
		{
			int r = a % b;
			a = b;
			b = r;
		};
		return a;
		 
	}
}



