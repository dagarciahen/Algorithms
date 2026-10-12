/*
LRU Cache

Design and implement a data structure for the Least Recently Used (LRU) cache.

Operations:
LRUCache(capacity)
get(key) -> int
put(key, value)
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

class LRUCache
{
public:
    explicit LRUCache(int capacity)
    {
        throw runtime_error("Not implemented");
    }

    int Get(int key)
    {
        throw runtime_error("Not implemented");
    }

    void Put(int key, int value)
    {
        throw runtime_error("Not implemented");
    }
};

string FormatArray(const vector<int>& values)
{
    string result = "[";
    for (size_t i = 0; i < values.size(); i++)
    {
        if (i > 0) result += ", ";
        result += to_string(values[i]);
    }
    result += "]";
    return result;
}

void RunTest1()
{
    cout << "Test 1\n";
    cout << "capacity = 3\n";
    cout << "expected = [250, 300, -1]\n";
    try
    {
        LRUCache cache(3);
        cache.Put(1, 100);
        cache.Put(2, 250);
        int result1 = cache.Get(2);
        cache.Put(4, 300);
        cache.Put(3, 200);
        int result2 = cache.Get(4);
        int result3 = cache.Get(1);
        vector<int> actual = {result1, result2, result3};
        cout << "actual   = " << FormatArray(actual) << "\n\n";
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented\n\n";
    }
}

void RunTest2()
{
    cout << "Test 2\n";
    cout << "capacity = 2\n";
    cout << "expected = [10, -1, 30]\n";
    try
    {
        LRUCache cache(2);
        cache.Put(1, 10);
        cache.Put(2, 20);
        int result1 = cache.Get(1);
        cache.Put(3, 30);
        int result2 = cache.Get(2);
        int result3 = cache.Get(3);
        vector<int> actual = {result1, result2, result3};
        cout << "actual   = " << FormatArray(actual) << "\n\n";
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented\n\n";
    }
}

void RunTest3()
{
    cout << "Test 3\n";
    cout << "capacity = 2\n";
    cout << "expected = [2]\n";
    try
    {
        LRUCache cache(2);
        cache.Put(2, 1);
        cache.Put(2, 2);
        vector<int> actual = {cache.Get(2)};
        cout << "actual   = " << FormatArray(actual) << "\n\n";
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented\n\n";
    }
}

void RunTest4()
{
    cout << "Test 4\n";
    cout << "capacity = 1\n";
    cout << "expected = [50, -1, 60]\n";
    try
    {
        LRUCache cache(1);
        cache.Put(5, 50);
        int result1 = cache.Get(5);
        cache.Put(6, 60);
        int result2 = cache.Get(5);
        int result3 = cache.Get(6);
        vector<int> actual = {result1, result2, result3};
        cout << "actual   = " << FormatArray(actual) << "\n\n";
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented\n\n";
    }
}

void RunTest5()
{
    cout << "Test 5\n";
    cout << "capacity = 3\n";
    cout << "expected = [-1, 1, -1, 3, 4]\n";
    try
    {
        LRUCache cache(3);
        int result1 = cache.Get(9);
        cache.Put(1, 1);
        cache.Put(2, 2);
        cache.Put(3, 3);
        int result2 = cache.Get(1);
        cache.Put(4, 4);
        int result3 = cache.Get(2);
        int result4 = cache.Get(3);
        int result5 = cache.Get(4);
        vector<int> actual = {result1, result2, result3, result4, result5};
        cout << "actual   = " << FormatArray(actual) << "\n\n";
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented\n\n";
    }
}

int main()
{
    RunTest1();
    RunTest2();
    RunTest3();
    RunTest4();
    RunTest5();
    return 0;
}
