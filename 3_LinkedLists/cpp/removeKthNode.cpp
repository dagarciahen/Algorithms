/*
Remove the Kth Last Node From a Linked List

Return the head of a singly linked list after removing the kth node from the end of it.

Example:
Input: head = [1, 2, 4, 7, 3], k = 2
Output: [1, 2, 4, 3]
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

ListNode* removeKthLastNode(ListNode* head, int k)
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

string FormatList(ListNode* head)
{
    string result = "[";
    bool first = true;
    while (head != nullptr)
    {
        if (!first) result += ", ";
        result += to_string(head->val);
        first = false;
        head = head->next;
    }
    result += "]";
    return result;
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

void RunTest(const vector<int>& input, int k, const vector<int>& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "input    = " << FormatArray(input) << '\n';
    cout << "k        = " << k << '\n';
    cout << "expected = " << FormatArray(expected) << '\n';

    try
    {
        ListNode* head = BuildList(input);
        ListNode* actual = removeKthLastNode(head, k);
        cout << "actual   = " << FormatList(actual) << '\n';
        cout << "pass     = " << (FormatList(actual) == FormatArray(expected) ? "true" : "false") << '\n';
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented" << '\n';
    }

    cout << '\n';
}

int main()
{
    RunTest({1, 2, 4, 7, 3}, 2, {1, 2, 4, 3}, "Test 1");
    RunTest({5}, 1, {}, "Test 2");
    RunTest({1, 2}, 2, {2}, "Test 3");
    RunTest({9, 8, 7, 6}, 1, {9, 8, 7}, "Test 4");
    RunTest({3, 1, 4, 1, 5, 9}, 4, {3, 1, 1, 5, 9}, "Test 5");
    return 0;
}
