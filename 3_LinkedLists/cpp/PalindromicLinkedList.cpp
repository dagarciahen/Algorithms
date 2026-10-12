/*
Palindromic Linked List

Given the head of a singly linked list, determine if it is a palindrome.

Example 1:
Input: head = [1, 2, 3, 2, 1]
Output: true

Example 2:
Input: head = [1, 2, 3]
Output: false
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

bool isPalindrome(ListNode* head)
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

void RunTest(const vector<int>& input, bool expected, const string& testName)
{
    cout << testName << '\n';
    cout << "head     = " << FormatArray(input) << '\n';
    cout << "expected = " << (expected ? "true" : "false") << '\n';

    try
    {
        ListNode* head = BuildList(input);
        bool actual = isPalindrome(head);
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
    RunTest({1, 2, 3, 2, 1}, true, "Test 1");
    RunTest({1, 2, 2, 1}, true, "Test 2");
    RunTest({1, 2, 3}, false, "Test 3");
    RunTest({7}, true, "Test 4");
    RunTest({4, 5, 4, 6}, false, "Test 5");
    return 0;
}
