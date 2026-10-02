class LinkedNode:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

        if prev is not None:
            prev.next = self
        if next is not None:
            next.prev = self

class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
"""
    def addfirst(self, item, value):
        if len(self._length) == 0:
            self._head = self._tail = LinkedNode(item, value)
        else:
            node = LinkedNode(item, value)
            node.next = self._head
            self._head.prev = node
            self._head = node
    def addlast(self, item, value):
        if len(self._length) == 0:
            self._head = self._tail = LinkedNode(item, value)
        else:
            node = LinkedNode(item, value)
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
"""
    def _addbetween(self, item, value, after, before):
        node = LinkedNode(item, value, after, before)
        if before is None:
            self._head = node
        if after is None:
            self._tail = node
        self._length += 1
    
    def addfirst(self, item, value):
        return self._addbetween(item, value, self._head, None)

    def addlast(self, item, value):
        return self._addbetween(item, value, None, self._tail)

    def _removebetween(self, node):
        before = node.prev
        after = node.next

        if before is None:
            self._head = node.next
        else:
            before.next = after

            
        if after is None:
            self._tail = before
        else:
            after.prev = before
        self._length -= 1

    def removefirst(self):
        self._removebetween(self._head, None)

    def removelast(self):
        self._removebetween(None, self._tail)

    def move_to_front(self, node):
        self._removebetween(node)
        return self.addfirst(node.key, node.value)
    


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lista = DoubleLinkedList()

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            new_node = self.lista.move_to_front(node)
            self.cache[key] = new_node           
            return node.value
    
    def put(self, key, value):
        if key not in self.cache:
            new_node = lru.addfirst(key, value)
            self.cache[key] = new_node
            if self.lista._length > self.capacity:
                self.lista.removelast()
        else:
            node = self.cache[key]
            node.value = value
            new_node = self.lista.move_to_front(node)
            self.cache[key] = new_node




