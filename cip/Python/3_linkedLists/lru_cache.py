
class LinkedNode:
    def __init__(self, key, value, prev = None, link = None):
        self.key = key
        self.link = link

        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
"""
    def addfirst(self, item):
        if len(self._length) == 0:
            self._head = self._tail = LinkedNode(item)
        else:
            new_node = LinkedNode(item)
            new_node.link = self._head
            self._head.prev = new_node
            self._head = new_node
        self._length += 1

    def addlast(self, item):
        if len(self._length) == 0:
            self._head = self._tail = LinkedNode(item)
        else:
            new_node = LinkedNode(item)
            new_node.prev = self._tail
            self._tail.link = new_node
            self._tail = new_node
        self._length +=1
""" 
    def addbetween(self, item, prev, after):
        node = ListNode(item, before, after)
        if after == self._head:
            self._head = node
        if prev == self._tail:
            self._tail = node
        self._length += 1
    
    def addfirst(self, item):
        return addbetween(self, item, None, self._head):

    def addlast(self, item):
        return addbetween(self, item, self._tail, None)

    def _remove(self, node):
        before = node.prev
        after = node.link
        if node is self._head:
            self._head = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before

    def removefirst(self):
        return self._remove(self._head)
    def removelast(self):
        return self._remove(self._tail)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = DoubleLinkedList()
        self.cache = {}

    def get(key: int):
        """
        retrun the value associeid with the key return -1 if key does ot excists
        """
        if key in self.cache:
            return cache[key]
        else:
            return -1



    def put(key: int, value: int):
        """
        add a key and the value to the cache if adding the key result in cache exceeding size evit hte least recetnyly used element if key exists already update value
        """
        node = ListedNode(key)
        if key in self.cache:
            self.cache[key] = value
            self.lru.remove(node)
            self.lru.addfirst(node)

        else:
            if self.lru._length < self.capacity:
                self.lru.addfirst(node)
            else:
                self.lru.removelast()
        self.cache[key] = value




