using System;
using System.Collections;

class Program
{
    static void Main()
    {
        string[] parts  = Console.ReadLine().Split(' ');
        int n = int.Parse(parts[0]);
        int m = int.Parse(parts[1]);
        Console.WriteLine(FibAgain(n,m));
    }
    static int FibAgain(int n, int m)
    {
        List<int> P = new List<int> {0, 1};
        bool condition = false;
        while (condition!)
        { 
            int a = P[P.Count-2];
            int b = P[P.Count-1];
            int next_val = (a + b) % m;
            P.Add(next_val);
            if (b == 0 && next_val == 1){ condition = true;}
        };
        int period_len = P.Count -2 ;
        int r = n % period_len;
        //n y n+knpi(m) caen en la misma posicion del ciclo (n+kn = r)
        int result = P[r];
        return result;
    }


}