"""
Palindromic Linked List

Given the head of a singly linked list, determine if it is a palindrome.

Example 1:
Input: head = [1, 2, 3, 2, 1]
Output: True

Example 2:
Input: head = [1, 2, 3]
Output: False
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    pointera = head
    pointerb = head
    while pointera and pointera.next:
        pointera = pointera.next.next
        pointerb = pointerb.next
    head2 = pointerb
    curr = head2
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    pointera = head
    pointerb = head2
    while pointerb.next:
        if pointera.val != pointerb.val: return False
        pointera = pointera.next
        pointerb = pointerb.next
    return True

    


def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def run_test(input_values, expected, test_name):
    print(test_name)
    print("head     = " + str(input_values))
    print("expected = " + str(expected))

    try:
        head = build_list(input_values)
        actual = is_palindrome(head)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 2, 3, 2, 1], True, "Test 1")
    run_test([1, 2, 2, 1], True, "Test 2")
    run_test([1, 2, 3], False, "Test 3")
    run_test([7], True, "Test 4")
    run_test([4, 5, 4, 6], False, "Test 5")
