/*
Flatten a Multi-Level Linked List

In a multi-level linked list, each node has a next pointer and a child pointer.
Flatten the structure into a single-level linked list by linking the end of each level
to the start of the next one.

Example output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
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
    ListNode* child;

    ListNode(int value = 0, ListNode* nextNode = nullptr, ListNode* childNode = nullptr)
        : val(value), next(nextNode), child(childNode) {}
};

ListNode* flattenLinkedList(ListNode* head)
{
    throw runtime_error("Not implemented");
}

ListNode* BuildTest1()
{
    ListNode* n1 = new ListNode(1);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(3);
    ListNode* n4 = new ListNode(4);
    ListNode* n5 = new ListNode(5);
    ListNode* n6 = new ListNode(6);
    ListNode* n7 = new ListNode(7);
    ListNode* n8 = new ListNode(8);
    ListNode* n9 = new ListNode(9);
    ListNode* n10 = new ListNode(10);
    ListNode* n11 = new ListNode(11);
    n1->next = n2; n2->next = n3; n3->next = n4; n4->next = n5;
    n3->child = n6; n6->next = n7;
    n4->child = n8; n5->child = n9;
    n7->child = n10; n8->child = n11;
    return n1;
}

ListNode* BuildTest2()
{
    ListNode* n1 = new ListNode(1);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(3);
    n1->next = n2; n2->next = n3;
    return n1;
}

ListNode* BuildTest3()
{
    ListNode* n1 = new ListNode(1);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(3);
    ListNode* n4 = new ListNode(4);
    ListNode* n5 = new ListNode(5);
    n1->child = n2; n2->child = n3; n3->child = n4; n4->child = n5;
    return n1;
}

ListNode* BuildTest4() { return new ListNode(7); }

ListNode* BuildTest5()
{
    ListNode* n1 = new ListNode(1);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(3);
    ListNode* n4 = new ListNode(4);
    ListNode* n5 = new ListNode(5);
    ListNode* n6 = new ListNode(6);
    ListNode* n7 = new ListNode(7);
    ListNode* n8 = new ListNode(8);
    n1->next = n2; n2->next = n3; n3->next = n4;
    n1->child = n5; n2->child = n6; n5->child = n7; n6->child = n8;
    return n1;
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

void RunTest(ListNode* head, const vector<int>& expected, const string& testName)
{
    cout << testName << '\n';
    cout << "expected = " << FormatArray(expected) << '\n';

    try
    {
        ListNode* actual = flattenLinkedList(head);
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
    RunTest(BuildTest1(), {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, "Test 1");
    RunTest(BuildTest2(), {1, 2, 3}, "Test 2");
    RunTest(BuildTest3(), {1, 2, 3, 4, 5}, "Test 3");
    RunTest(BuildTest4(), {7}, "Test 4");
    RunTest(BuildTest5(), {1, 2, 3, 4, 5, 6, 7, 8}, "Test 5");
    return 0;
}
