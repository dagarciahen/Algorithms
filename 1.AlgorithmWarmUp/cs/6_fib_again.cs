using System;
using System.Collections;

class Program
{
    static void Main()
    {
        string[] parts  = Console.ReadLine().Split(' ');
        int n = int.Parse(parts[0]);
        Console.WriteLine(LastDigitFibSum(n));
    }
    static int LastDigitFibSum(int a)
    {
        List<int> F = new List<int>{0,1};
        bool condition = false;
        while (condition!)
        {
            int prev = F[F.Count -2];
            int curr = F[F.Count -1];
            int next_val = (prev + curr) % 10;
            F.Add(next_val);
            if (curr == 0 && next_val == 1){condition =true;}
        }
        
        ##sum Fi = Fn+2 -1
        
        int periodLen = F.Count -2;
        int index = (n+2) % period;
        
        int result = F[index] -1;
        return F[result];
    }
}