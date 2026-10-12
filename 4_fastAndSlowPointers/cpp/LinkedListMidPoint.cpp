/*
Linked List Midpoint

Given a singly linked list, find and return its middle node.
If there are two middle nodes, return the second one.

Example 1:
Input: head = [1, 2, 4, 7, 3]
Output: Node 4

Example 2:
Input: head = [1, 2, 4, 7, 3, 9]
Output: Node 7

Constraints:
The linked list contains at least one node.
The linked list contains unique values.
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

ListNode* FindMidpoint(ListNode* head)
{
    throw runtime_error("Not implemented");
}

ListNode* BuildList(const vector<int>& values)
{
    ListNode dummy(0);
    ListNode* current = &dummy;
    for (int value : values)
    {
        current->next = new ListNode(value);
        current = current->next;
    }
    return dummy.next;
}

string FormatNode(ListNode* node)
{
    if (node == nullptr)
    {
        return "null";
    }

    return "Node " + to_string(node->val);
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

void RunTest(const vector<int>& input, int expectedValue, const string& testName)
{
    cout << testName << '\n';
    cout << "head     = " << FormatArray(input) << '\n';
    cout << "expected = Node " << expectedValue << '\n';

    try
    {
        ListNode* head = BuildList(input);
        ListNode* actual = FindMidpoint(head);
        cout << "actual   = " << FormatNode(actual) << '\n';
        cout << "pass     = " << ((actual != nullptr && actual->val == expectedValue) ? "true" : "false") << '\n';
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented" << '\n';
    }

    cout << '\n';
}

int main()
{
    RunTest({1, 2, 4, 7, 3}, 4, "Test 1");
    RunTest({1, 2, 4, 7, 3, 9}, 7, "Test 2");
    RunTest({5}, 5, "Test 3");
    RunTest({8, 6, 4, 2}, 4, "Test 4");
    RunTest({10, 20, 30, 40, 50, 60, 70}, 40, "Test 5");
    return 0;
}
