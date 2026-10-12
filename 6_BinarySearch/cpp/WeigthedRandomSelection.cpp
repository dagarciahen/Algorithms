/*
Weighted Random Selection

Given an array of items, each with a corresponding weight, implement a function
that randomly selects an item from the array, where the probability of selecting
any item is proportional to its weight.

In other words, the probability of picking the item at index i is:
weights[i] / sum(weights)

Return the index of the selected item.

Example:
Input: weights = [3, 1, 2, 4]

Explanation:
sum(weights) = 10
Index 0 has probability 3/10
Index 1 has probability 1/10
Index 2 has probability 2/10
Index 3 has probability 4/10

For example, we expect index 0 to be returned about 30% of the time.

Constraints:
The weights array contains at least one element.
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

int WeightedRandomSelection(const vector<int>& weights)
{
    throw runtime_error("Not implemented");
}

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

void RunBasicTest(const vector<int>& weights, const string& testName)
{
    cout << testName << '\n';
    cout << "weights   = " << FormatArray(weights) << '\n';
    cout << "expected  = a valid index between 0 and " << (static_cast<int>(weights.size()) - 1) << '\n';

    try
    {
        int actual = WeightedRandomSelection(weights);
        cout << "actual    = " << actual << '\n';
        cout << "pass      = " << (actual >= 0 && actual < static_cast<int>(weights.size()) ? "true" : "false") << '\n';
    }
    catch (const runtime_error&)
    {
        cout << "actual    = not implemented" << '\n';
    }

    cout << '\n';
}

int main()
{
    RunBasicTest({3, 1, 2, 4}, "Test 1");
    RunBasicTest({1}, "Test 2");
    RunBasicTest({10, 10, 10}, "Test 3");
    RunBasicTest({5, 100}, "Test 4");
    RunBasicTest({2, 4, 6, 8, 10}, "Test 5");
    return 0;
}
