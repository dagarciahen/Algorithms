"""
Remove the Kth Last Node From a Linked List

Return the head of a singly linked list after removing the kth node from the end of it.

Example:
Input: head = [1, 2, 4, 7, 3], k = 2
Output: [1, 2, 4, 3]

Constraints:
The linked list contains at least one node.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_kth_last_node(head, k):
    dummy = ListNode(0)
    dummy.next = head
    lead = trailer = dummy
    for _ in range(k+1):
        lead = lead.next
    while lead:
        lead = lead.next
        trailer = trailer.next
    trailer.next = trailer.next.next
    return dummy.next





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


def run_test(input_values, k, expected, test_name):
    print(test_name)
    print("input    = " + str(input_values))
    print("k        = " + str(k))
    print("expected = " + str(expected))

    try:
        head = build_list(input_values)
        actual = remove_kth_last_node(head, k)
        actual_values = format_list(actual)
        print("actual   = " + actual_values)
        print("pass     = " + str(actual_values == str(expected)))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 2, 4, 7, 3], 2, [1, 2, 4, 3], "Test 1")
    run_test([5], 1, [], "Test 2")
    run_test([1, 2], 2, [2], "Test 3")
    run_test([9, 8, 7, 6], 1, [9, 8, 7], "Test 4")
    run_test([3, 1, 4, 1, 5, 9], 4, [3, 1, 1, 5, 9], "Test 5")
