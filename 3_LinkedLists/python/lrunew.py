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

    def _addbetween(self, key, value, after, before):
        node = LinkedNode(key, value, after, before)
        if self._length == 0:
            self._tail = self._head = node
        if after is None:
            self._tail = node
        if before is None:
            self._head = node
        self._length += 1
        return node

    def addfirst(self, key, value):
        return self._addbetween(key, value, self._head, None)

    def addlast(self, key, valye):
        return self._addbetween(key, value, None, self._tail)

    def _removebetween(self, node):
        after = node.next
        before = node.prev

        if after is None:
            self._tail = before
        else:
            after.prev = before

        if before is None:
            self._head = after
        else:
            before.next = after
        self._length -=1

    def removelast(self):
        self._removebetween(self._tail)

    def removefirst(self):
        self._removebetween(self._head)

    def movetofirst(self,node):
        self._removebetween(node)
        return self.addfirst(node.key, node.value)


    def printlist(self):
        curr = self._head
        while curr:
            print(f"({curr.key}, {curr.value})", end="->")
            curr = curr.next
        print("None")


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = DoubleLinkedList()
        self.cache = {}


    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            node = self.movetofirst(node)
            return node.value


    def put(self, key, value):
        if key not in self.cache:
            new_node = self.list.addfirst(key, value)
            self.cache[key] = new_node
            if self.list._length > self.capacity:
                self.list.removelast()

        else:
            node = self.cache[key]
            node.value = value
            new_node = self.list.movetofirst(node)
            self.cache[key] = new_node



