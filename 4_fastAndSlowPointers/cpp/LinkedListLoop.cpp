/*
Linked List Loop

Given a singly linked list, determine if it contains a cycle.
A cycle occurs if a node's next pointer references an earlier node in the linked list,
causing a loop.

Example:
Input: head = [[1, 2, 3, 4, 5, 6], 2]
Output: true

The second value represents the index that the tail connects to.
If it is -1, the list has no cycle.
*/

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

struct ListNode
{
    int val;
    ListNode* next;

    ListNode(int value = 0, ListNode* nextNode = nullptr) : val(value), next(nextNode) {}
};

bool HasCycle(ListNode* head)
{
    throw runtime_error("Not implemented");
}

ListNode* BuildList(const vector<int>& values, int cycleIndex)
{
    if (values.empty())
    {
        return nullptr;
    }

    vector<ListNode*> nodes;
    nodes.reserve(values.size());

    for (int value : values)
    {
        nodes.push_back(new ListNode(value));
    }

    for (size_t i = 0; i + 1 < nodes.size(); i++)
    {
        nodes[i]->next = nodes[i + 1];
    }

    if (cycleIndex >= 0)
    {
        nodes.back()->next = nodes[cycleIndex];
    }

    return nodes[0];
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

void RunTest(const vector<int>& values, int cycleIndex, bool expected, const string& testName)
{
    cout << testName << '\n';
    cout << "head     = [" << FormatArray(values) << ", " << cycleIndex << "]\n";
    cout << "expected = " << (expected ? "true" : "false") << '\n';

    try
    {
        ListNode* head = BuildList(values, cycleIndex);
        bool actual = HasCycle(head);
        cout << "actual   = " << (actual ? "true" : "false") << '\n';
        cout << "pass     = " << (actual == expected ? "true" : "false") << '\n';
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented" << '\n';
    }

    cout << '\n';
}

int main()
{
    RunTest({1, 2, 3, 4, 5, 6}, 2, true, "Test 1");
    RunTest({1, 2, 3, 4}, -1, false, "Test 2");
    RunTest({7}, 0, true, "Test 3");
    RunTest({9, 8}, 0, true, "Test 4");
    RunTest({5, 1, 4, 2, 3}, -1, false, "Test 5");
    return 0;
}
