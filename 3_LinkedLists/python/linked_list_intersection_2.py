from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode:
    node_set = set()
    currA = head_A
    prevA = None 
    while currA:
        prevA = currA
        node_set.add(currA)
        currA = currA.next

    currB = head_B
    prevB = None
    while currB:
        prevB = currB
        if currB in node_set:
            return currB
        else:
            currB = currB.next
    return []
