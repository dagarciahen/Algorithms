"""
Linked List Midpoint

Given a singly linked list, find and return its middle node.
If there are two middle nodes, return the second one.

Example 1:
Input: head = [1, 2, 4, 7, 3]
Output: Node 4

Example 2:
Input: head = [1, 2, 4, 7, 3, 9]
Output: Node 7
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_midpoint(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def format_node(node):
    if node is None:
        return "null"
    return "Node " + str(node.val)


def run_test(input_values, expected_value, test_name):
    print(test_name)
    print("head     = " + str(input_values))
    print("expected = Node " + str(expected_value))

    try:
        head = build_list(input_values)
        actual = find_midpoint(head)
        print("actual   = " + format_node(actual))
        print("pass     = " + str(actual is not None and actual.val == expected_value))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 2, 4, 7, 3], 4, "Test 1")
    run_test([1, 2, 4, 7, 3, 9], 7, "Test 2")
    run_test([5], 5, "Test 3")
    run_test([8, 6, 4, 2], 4, "Test 4")
    run_test([10, 20, 30, 40, 50, 60, 70], 40, "Test 5")
