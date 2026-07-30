"""
Design and implement a data structure for the Least Recently Used (LRU) cache that supports the following operations:

LRUCache(capacity: int): Initialize an LRU cache with the specified capacity.
get(key: int) -> int: Return the value associated with a key. Return -1 if the key doesn't exist.
put(key: int, value: int) -> None: Add a key and its value to the cache. If adding the key would result in the cache exceeding its size capacity, evict the least recently used element. If the key already exists in the cache, update its value.
"""

class DoubleLinkedList:
    def __init__(self, key, val):
        self.next = self.prev = None
        self.key = key
        self.val = val
    


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.head = DoubleLinkedList(-1,-1)
        self.tail = DoubleLinkedList(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head 
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_tail(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev_node
    def get(self, key:int) -> int:
        if key not in self.hashmap:
            return -1

        self.remove_node(self.hashmap[key])
        self.add_to_tail(self.hashmap[key])

        
        return self.hashmap[key].val

    def put(self, key:int, val:int) -> None:
        if key in self.hashmap:
            self.remove_node(self.hashmap[key])
        node = DoubleLinkedList(key, val)
        self.hashmap[key] = node

        if len(self.hashmap) > capacity:
            del self.hashmap[self.head.next.key]
            self.remove_node(self.head.next)
        self.add_to_tail(node)



    
