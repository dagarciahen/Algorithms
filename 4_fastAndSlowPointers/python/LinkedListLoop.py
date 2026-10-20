"""
Linked List Loop

Given a singly linked list, determine if it contains a cycle.
A cycle occurs if a node's next pointer references an earlier node in the linked list,
causing a loop.

Example:
Input: head = [[1, 2, 3, 4, 5, 6], 2]
Output: True

The second value represents the index that the tail connects to.
If it is -1, the list has no cycle.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast: return False
    return False
        




def build_list(values, cycle_index):
    if not values:
        return None

    nodes = [ListNode(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_index >= 0:
        nodes[-1].next = nodes[cycle_index]
    return nodes[0]


def run_test(values, cycle_index, expected, test_name):
    print(test_name)
    print("head     = [" + str(values) + ", " + str(cycle_index) + "]")
    print("expected = " + str(expected))

    try:
        head = build_list(values, cycle_index)
        actual = has_cycle(head)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 2, 3, 4, 5, 6], 2, True, "Test 1")
    run_test([1, 2, 3, 4], -1, False, "Test 2")
    run_test([7], 0, True, "Test 3")
    run_test([9, 8], 0, True, "Test 4")
    run_test([5, 1, 4, 2, 3], -1, False, "Test 5")
