class LinkedNode:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value 
        self.prev = prev 
        self.next = next

        if self.next is not None:
            self.next.prev = self
        if self.prev is not None:
            self.prev.next = self

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
        node = LinkedNode(key, value, before, after)
        if before is None:
            self._head = node
        if after is None:
            self._tail = node
        self._length += 1
        return node


    def removefirst(self):
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
        self._length -=1
        return node

    def movetofirst(self, node):
        before = node.prev
        after = node.next

        if before is not None:
            before.next = after
        else:
            return
        if after is not None:
            after.prev = before
        else:
            self._tail = before

        node.next = self._head
        node.prev = None 
        self._head.prev = node
        self._head = node

    def __str__(self):
        items = []
        node = self._head
        while node is not None:
            items.append(f"({node.key}), ({node.value})")
            node = node.next
        return "[" +"<->".join(items) + "]"
    
dls = DoubleLinkedList()

nodea = dls.addfirst(1, "a")
nodeb = dls.addlast(1, "b")
dls.movetofirst(nodeb)

print(dls)

    
        
