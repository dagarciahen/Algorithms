/*
Linked List Intersection

Return the node where two singly linked lists intersect.
If the linked lists do not intersect, return null.

Example:
head_A = [1, 3, 4, 8, 7, 2]
head_B = [6, 4, 8, 7, 2]
skip_A = 3
skip_B = 2
Output: Node 8
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

ListNode* getIntersectionNode(ListNode* headA, ListNode* headB)
{
    throw runtime_error("Not implemented");
}

vector<ListNode*> BuildNodes(const vector<int>& values)
{
    vector<ListNode*> nodes;
    for (int value : values)
    {
        nodes.push_back(new ListNode(value));
    }
    for (size_t i = 0; i + 1 < nodes.size(); i++)
    {
        nodes[i]->next = nodes[i + 1];
    }
    return nodes;
}

pair<ListNode*, ListNode*> BuildIntersectingLists(const vector<int>& valuesA, const vector<int>& valuesB, int skipA, int skipB)
{
    vector<ListNode*> nodesA = BuildNodes(valuesA);
    vector<ListNode*> nodesB = BuildNodes(valuesB);

    ListNode* headA = nodesA.empty() ? nullptr : nodesA[0];
    ListNode* headB = nodesB.empty() ? nullptr : nodesB[0];

    if (skipA < static_cast<int>(valuesA.size()) && skipB < static_cast<int>(valuesB.size()))
    {
        ListNode* intersection = nodesA[skipA];
        if (skipB == 0)
        {
            headB = intersection;
        }
        else
        {
            nodesB[skipB - 1]->next = intersection;
        }
    }

    return {headA, headB};
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

string FormatNode(ListNode* node)
{
    return node == nullptr ? "null" : "Node " + to_string(node->val);
}

void RunTest(const vector<int>& valuesA, const vector<int>& valuesB, int skipA, int skipB, int expectedValue, bool hasNode, const string& testName)
{
    cout << testName << '\n';
    cout << "head_A   = " << FormatArray(valuesA) << '\n';
    cout << "head_B   = " << FormatArray(valuesB) << '\n';
    cout << "skip_A   = " << skipA << '\n';
    cout << "skip_B   = " << skipB << '\n';
    cout << "expected = " << (hasNode ? "Node " + to_string(expectedValue) : string("null")) << '\n';

    try
    {
        auto [headA, headB] = BuildIntersectingLists(valuesA, valuesB, skipA, skipB);
        ListNode* actual = getIntersectionNode(headA, headB);
        cout << "actual   = " << FormatNode(actual) << '\n';
        bool pass = hasNode ? (actual != nullptr && actual->val == expectedValue) : (actual == nullptr);
        cout << "pass     = " << (pass ? "true" : "false") << '\n';
    }
    catch (const runtime_error&)
    {
        cout << "actual   = not implemented" << '\n';
    }

    cout << '\n';
}

int main()
{
    RunTest({1, 3, 4, 8, 7, 2}, {6, 4, 8, 7, 2}, 3, 2, 8, true, "Test 1");
    RunTest({1, 2, 3}, {4, 5, 6}, 3, 3, 0, false, "Test 2");
    RunTest({9, 8, 7}, {8, 7}, 1, 0, 8, true, "Test 3");
    RunTest({5, 1, 2, 3}, {9, 2, 3}, 2, 1, 2, true, "Test 4");
    RunTest({4, 6, 1}, {1}, 2, 0, 1, true, "Test 5");
    return 0;
}
