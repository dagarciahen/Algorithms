"""
Reverse a singly linked list.

Example:
Input: head = [1, 2, 4, 7, 3]
Output: [3, 7, 4, 2, 1]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    head = prev
    return head




def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def format_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return str(values)


def run_test(input_values, expected, test_name):
    print(test_name)
    print("input    = " + str(input_values))
    print("expected = " + str(expected))

    try:
        head = build_list(input_values)
        actual = reverse_linked_list(head)
        actual_values = format_list(actual)
        print("actual   = " + actual_values)
        print("pass     = " + str(actual_values == str(expected)))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 2, 4, 7, 3], [3, 7, 4, 2, 1], "Test 1")
    run_test([1], [1], "Test 2")
    run_test([], [], "Test 3")
    run_test([5, 6], [6, 5], "Test 4")
    run_test([9, 8, 7, 6], [6, 7, 8, 9], "Test 5")
