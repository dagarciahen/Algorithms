"""
Flatten a Multi-Level Linked List

In a multi-level linked list, each node has a next pointer and a child pointer.
Flatten the structure into a single-level linked list by linking the end of each level
to the start of the next one.

Example:
Input:
[
  [1, []],
  [2, []],
  [3, [[6, []], [7, [[10, []]]]]],
  [4, [[8, [[11, []]]]]],
  [5, [[9, []]]]
]

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
"""


class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child


def flatten_linked_list(head):
    raise NotImplementedError()


def build_test_1():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)
    n8 = ListNode(8)
    n9 = ListNode(9)
    n10 = ListNode(10)
    n11 = ListNode(11)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n3.child = n6
    n6.next = n7
    n4.child = n8
    n5.child = n9
    n7.child = n10
    n8.child = n11
    return n1


def build_test_2():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    return n1


def build_test_3():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.child = n2
    n2.child = n3
    n3.child = n4
    n4.child = n5
    return n1


def build_test_4():
    return ListNode(7)


def build_test_5():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)
    n8 = ListNode(8)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n1.child = n5
    n2.child = n6
    n5.child = n7
    n6.child = n8
    return n1


def format_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return str(values)


def run_test(head, expected, test_name):
    print(test_name)
    print("expected = " + str(expected))

    try:
        actual = flatten_linked_list(head)
        actual_values = format_list(actual)
        print("actual   = " + actual_values)
        print("pass     = " + str(actual_values == str(expected)))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test(build_test_1(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "Test 1")
    run_test(build_test_2(), [1, 2, 3], "Test 2")
    run_test(build_test_3(), [1, 2, 3, 4, 5], "Test 3")
    run_test(build_test_4(), [7], "Test 4")
    run_test(build_test_5(), [1, 2, 3, 4, 5, 6, 7, 8], "Test 5")
