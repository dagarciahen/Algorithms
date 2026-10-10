/*
LRU Cache

Design and implement a data structure for the Least Recently Used (LRU) cache
that supports the following operations:

LRUCache(capacity: int): Initialize an LRU cache with the specified capacity.
get(key: int) -> int: Return the value associated with a key. Return -1 if the key doesn't exist.
put(key: int, value: int) -> None: Add a key and its value to the cache. If adding the key
would result in the cache exceeding its size capacity, evict the least recently used element.
If the key already exists in the cache, update its value.

Example:
Input:
put(1, 100)
put(2, 250)
get(2)
put(4, 300)
put(3, 200)
get(4)
get(1)
capacity = 3

Output: [250, 300, -1]

Constraints:
All keys and values are positive integers.
*/

using System;

public class LRUCache
{
    public LRUCache(int capacity)
    {
        throw new NotImplementedException();
    }

    public int Get(int key)
    {
        throw new NotImplementedException();
    }

    public void Put(int key, int value)
    {
        throw new NotImplementedException();
    }
}

public class Solution
{
    public static void Main(string[] args)
    {
        RunTest1();
        RunTest2();
        RunTest3();
        RunTest4();
        RunTest5();
    }

    private static void RunTest1()
    {
        Console.WriteLine("Test 1");
        Console.WriteLine("capacity = 3");
        Console.WriteLine("operations = [put(1,100), put(2,250), get(2), put(4,300), put(3,200), get(4), get(1)]");
        Console.WriteLine("expected = [250, 300, -1]");

        try
        {
            LRUCache cache = new LRUCache(3);
            cache.Put(1, 100);
            cache.Put(2, 250);
            int result1 = cache.Get(2);
            cache.Put(4, 300);
            cache.Put(3, 200);
            int result2 = cache.Get(4);
            int result3 = cache.Get(1);

            int[] actual = new int[] { result1, result2, result3 };
            Console.WriteLine("actual   = " + FormatArray(actual));
            Console.WriteLine("pass     = " + AreEqual(actual, new int[] { 250, 300, -1 }));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static void RunTest2()
    {
        Console.WriteLine("Test 2");
        Console.WriteLine("capacity = 2");
        Console.WriteLine("operations = [put(1,10), put(2,20), get(1), put(3,30), get(2), get(3)]");
        Console.WriteLine("expected = [10, -1, 30]");

        try
        {
            LRUCache cache = new LRUCache(2);
            cache.Put(1, 10);
            cache.Put(2, 20);
            int result1 = cache.Get(1);
            cache.Put(3, 30);
            int result2 = cache.Get(2);
            int result3 = cache.Get(3);

            int[] actual = new int[] { result1, result2, result3 };
            Console.WriteLine("actual   = " + FormatArray(actual));
            Console.WriteLine("pass     = " + AreEqual(actual, new int[] { 10, -1, 30 }));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static void RunTest3()
    {
        Console.WriteLine("Test 3");
        Console.WriteLine("capacity = 2");
        Console.WriteLine("operations = [put(2,1), put(2,2), get(2)]");
        Console.WriteLine("expected = [2]");

        try
        {
            LRUCache cache = new LRUCache(2);
            cache.Put(2, 1);
            cache.Put(2, 2);
            int result1 = cache.Get(2);

            int[] actual = new int[] { result1 };
            Console.WriteLine("actual   = " + FormatArray(actual));
            Console.WriteLine("pass     = " + AreEqual(actual, new int[] { 2 }));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static void RunTest4()
    {
        Console.WriteLine("Test 4");
        Console.WriteLine("capacity = 1");
        Console.WriteLine("operations = [put(5,50), get(5), put(6,60), get(5), get(6)]");
        Console.WriteLine("expected = [50, -1, 60]");

        try
        {
            LRUCache cache = new LRUCache(1);
            cache.Put(5, 50);
            int result1 = cache.Get(5);
            cache.Put(6, 60);
            int result2 = cache.Get(5);
            int result3 = cache.Get(6);

            int[] actual = new int[] { result1, result2, result3 };
            Console.WriteLine("actual   = " + FormatArray(actual));
            Console.WriteLine("pass     = " + AreEqual(actual, new int[] { 50, -1, 60 }));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static void RunTest5()
    {
        Console.WriteLine("Test 5");
        Console.WriteLine("capacity = 3");
        Console.WriteLine("operations = [get(9), put(1,1), put(2,2), put(3,3), get(1), put(4,4), get(2), get(3), get(4)]");
        Console.WriteLine("expected = [-1, 1, -1, 3, 4]");

        try
        {
            LRUCache cache = new LRUCache(3);
            int result1 = cache.Get(9);
            cache.Put(1, 1);
            cache.Put(2, 2);
            cache.Put(3, 3);
            int result2 = cache.Get(1);
            cache.Put(4, 4);
            int result3 = cache.Get(2);
            int result4 = cache.Get(3);
            int result5 = cache.Get(4);

            int[] actual = new int[] { result1, result2, result3, result4, result5 };
            Console.WriteLine("actual   = " + FormatArray(actual));
            Console.WriteLine("pass     = " + AreEqual(actual, new int[] { -1, 1, -1, 3, 4 }));
        }
        catch (NotImplementedException)
        {
            Console.WriteLine("actual   = not implemented");
        }

        Console.WriteLine();
    }

    private static string FormatArray(int[] values)
    {
        if (values == null)
        {
            return "null";
        }

        return "[" + string.Join(", ", values) + "]";
    }

    private static bool AreEqual(int[] left, int[] right)
    {
        if (left == null || right == null)
        {
            return left == right;
        }

        if (left.Length != right.Length)
        {
            return false;
        }

        for (int i = 0; i < left.Length; i++)
        {
            if (left[i] != right[i])
            {
                return false;
            }
        }

        return true;
    }
}