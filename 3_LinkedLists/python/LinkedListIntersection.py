"""
Linked List Intersection

Return the node where two singly linked lists intersect.
If the linked lists do not intersect, return None.

Example:
head_A = [1, 3, 4, 8, 7, 2]
head_B = [6, 4, 8, 7, 2]
skip_A = 3
skip_B = 2
Output: Node 8
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_intersection_node(head_a, head_b):
    raise NotImplementedError()


def build_nodes(values):
    nodes = [ListNode(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes


def build_intersecting_lists(values_a, values_b, skip_a, skip_b):
    nodes_a = build_nodes(values_a)
    nodes_b = build_nodes(values_b)

    head_a = nodes_a[0] if nodes_a else None
    head_b = nodes_b[0] if nodes_b else None

    if skip_a < len(values_a) and skip_b < len(values_b):
        intersection = nodes_a[skip_a]
        if skip_b == 0:
            head_b = intersection
        else:
            nodes_b[skip_b - 1].next = intersection

    return head_a, head_b


def format_node(node):
    if node is None:
        return "null"
    return "Node " + str(node.val)


def run_test(values_a, values_b, skip_a, skip_b, expected_value, test_name):
    print(test_name)
    print("head_A   = " + str(values_a))
    print("head_B   = " + str(values_b))
    print("skip_A   = " + str(skip_a))
    print("skip_B   = " + str(skip_b))
    print("expected = " + ("null" if expected_value is None else "Node " + str(expected_value)))

    try:
        head_a, head_b = build_intersecting_lists(values_a, values_b, skip_a, skip_b)
        actual = get_intersection_node(head_a, head_b)
        print("actual   = " + format_node(actual))
        print("pass     = " + str((actual is None and expected_value is None) or (actual is not None and actual.val == expected_value)))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test([1, 3, 4, 8, 7, 2], [6, 4, 8, 7, 2], 3, 2, 8, "Test 1")
    run_test([1, 2, 3], [4, 5, 6], 3, 3, None, "Test 2")
    run_test([9, 8, 7], [8, 7], 1, 0, 8, "Test 3")
    run_test([5, 1, 2, 3], [9, 2, 3], 2, 1, 2, "Test 4")
    run_test([4, 6, 1], [1], 2, 0, 1, "Test 5")
