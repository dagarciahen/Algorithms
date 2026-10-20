"""
LRU Cache

Design and implement a data structure for the Least Recently Used (LRU) cache
that supports the following operations:

LRUCache(capacity): Initialize an LRU cache with the specified capacity.
get(key): Return the value associated with a key. Return -1 if the key does not exist.
put(key, value): Add or update a key. If the cache exceeds capacity, evict the least recently used element.

Constraints:
All keys and values are positive integers.
"""


class ListNode:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

        if prev is not None:
            prev.next = self
        if next is not None:
            next.prev = self

class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, key, value):
        return self._addbetween(key, value, None, self._head)
    def addlast(self, key, value):
        return self._addbetween(key, value, self._tail, None)

    def _addbetween(self, key, value, before, after):
        node = ListNode(key, value, before, after)
        if before is None:
            self._head = node
        if after is None:
            self._tail = node
        self._length += 1
        return node
    
    def removefirst(self):
        return self._removebetween(self._head)
    def removelast(self):
        return self._removebetween(self._tail)

    def _removebetween(self, node):
        before = node.prev
        after = node.next
        
        if before is None:
            self._head = after
        else:
            before.next = after
        if after is None:
            self._tail = before
        else:
            after.prev = before
        self._length +=1
        return node

    def movetofirst(self, node):
        before = node.prev
        after = node.next

        if before is None:
            return
        else:
            before.next = after
        if after is None:
            self._tail = before
        else:
            after.prev = before

        node.next = self._head
        self._head.prev = node
        node.prev = None
        self._head = node
        return node

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lrucache = DoubleLinkedList()
        self.hashNodes = {}

    def get(self, key):
        if key not in self.hashNodes:
            return -1
        node = self.hashNodes[key]
        self.lrucache.movetofirst(node)
        return node.value

    def put(self, key, value):
        if key not in self.hashNodes:
            if self.capacity > self.lrucache._length:
                node = self.lrucache.addfirst(key, value)
                self.hashNodes[key] = node
            else:
                old_node = self.lrucache.removelast()
                del self.hashNodes[old_node.key]
                node = self.lrucache.addfirst(key, value)
                self.hashNodes[key] = node
        else:
            node = self.hashNodes[key]
            node.value = value
            self.lrucache.movetofirst(node)


def are_equal(left, right):
    return left == right


def run_test_1():
    print("Test 1")
    print("capacity = 3")
    print("operations = [put(1,100), put(2,250), get(2), put(4,300), put(3,200), get(4), get(1)]")
    print("expected = [250, 300, -1]")

    try:
        cache = LRUCache(3)
        cache.put(1, 100)
        cache.put(2, 250)
        result1 = cache.get(2)
        cache.put(4, 300)
        cache.put(3, 200)
        result2 = cache.get(4)
        result3 = cache.get(1)
        actual = [result1, result2, result3]
        print("actual   = " + str(actual))
        print("pass     = " + str(are_equal(actual, [250, 300, -1])))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


def run_test_2():
    print("Test 2")
    print("capacity = 2")
    print("operations = [put(1,10), put(2,20), get(1), put(3,30), get(2), get(3)]")
    print("expected = [10, -1, 30]")

    try:
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        result1 = cache.get(1)
        cache.put(3, 30)
        result2 = cache.get(2)
        result3 = cache.get(3)
        actual = [result1, result2, result3]
        print("actual   = " + str(actual))
        print("pass     = " + str(are_equal(actual, [10, -1, 30])))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


def run_test_3():
    print("Test 3")
    print("capacity = 2")
    print("operations = [put(2,1), put(2,2), get(2)]")
    print("expected = [2]")

    try:
        cache = LRUCache(2)
        cache.put(2, 1)
        cache.put(2, 2)
        actual = [cache.get(2)]
        print("actual   = " + str(actual))
        print("pass     = " + str(are_equal(actual, [2])))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


def run_test_4():
    print("Test 4")
    print("capacity = 1")
    print("operations = [put(5,50), get(5), put(6,60), get(5), get(6)]")
    print("expected = [50, -1, 60]")

    try:
        cache = LRUCache(1)
        cache.put(5, 50)
        result1 = cache.get(5)
        cache.put(6, 60)
        result2 = cache.get(5)
        result3 = cache.get(6)
        actual = [result1, result2, result3]
        print("actual   = " + str(actual))
        print("pass     = " + str(are_equal(actual, [50, -1, 60])))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


def run_test_5():
    print("Test 5")
    print("capacity = 3")
    print("operations = [get(9), put(1,1), put(2,2), put(3,3), get(1), put(4,4), get(2), get(3), get(4)]")
    print("expected = [-1, 1, -1, 3, 4]")

    try:
        cache = LRUCache(3)
        result1 = cache.get(9)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        result2 = cache.get(1)
        cache.put(4, 4)
        result3 = cache.get(2)
        result4 = cache.get(3)
        result5 = cache.get(4)
        actual = [result1, result2, result3, result4, result5]
        print("actual   = " + str(actual))
        print("pass     = " + str(are_equal(actual, [-1, 1, -1, 3, 4])))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test_1()
    run_test_2()
    run_test_3()
    run_test_4()
    run_test_5()
