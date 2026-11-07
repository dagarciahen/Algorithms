"""
Given k singly linked lists, each sorted in ascending order, combine them into one sorted linked list.
example
lists = 
[[1,6],[1,4,6],[3,7]]

"""

from typing import List
from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

import heapq
def combine_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    def _less(self, other):
        return self.val < other.val

    ListNode.__lt__ = _less

    minheap = []
    for head in lists:
        heapq.heappush(heap, head)

    dummy = ListNode(-1)
    curr = dummy
    
    while heap:
        smallest_node = heappq.heappop(heap)
        curr.next = smallest_node
        curr = curr.next

        if smallest_node.next:
            heapq.heappush(heap, smallest_node.next)
    return dummy.next
curr = dummy

while heap:
    smallest_node = heappq.heappop(heap)
    curr.next = smallest_node
    curr = curr.next

    if smallest_node.next:
        heapq.heappush(heap, smallest_node.next)
return dummy.next

