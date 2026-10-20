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
    pointer_a = pointer_b = head

    while pointer_a and pointer_a.next:
        pointer_a = pointer_a.next.next
        pointer_b = pointer_b.next

    mid = pointer_b

    curr = mid
    prev = mid

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    head2 = prev

    pointer_a = head
    pointer_b = head2

    while pointer_b != pointer_a:
        pointer_a = pointer_a.next
        pointer_b = pointer_b.next
        if pointer_a.val != pointer_b.val:
            return False
        
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
