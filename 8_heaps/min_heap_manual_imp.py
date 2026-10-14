class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class HeapPQ:
    def __init__(self):
        self._entries = []

    def insert(self, item ,priority):
        self._entries.append(Entry(item,priority))
        self._upheap(len(self._entries)-1)


    def _parent(self, i):
        return (i-1)//2

    def _child(self, i):
        left = 2*i+1
        right = 2*i +2
        return range(left, min(len(self._entries), right+1))

    def _swap(self, a, b):
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        L = self._entries
        parent = self._parent(i)
        if i > 0 and L[i] < L[parent]:
            self._swap(parent, i)
            self._upheap(parent)
    def findmin(self):
        return self._entries[0].item

    def removemin(self):
        L = self._entries
        item = L[0].item 
        L[0] = L[-1]
        L.pop()
        self._downheap(0)
        return item

    def _downheap(self, i):
        L = self._entries
        children = self._child(i)
        if children:
            child = min(children, key = lambda x : L[x])
            if L[child] < L[i]:
                self._swap(child, i)
                self._downheap(child)

    def _heapify(self):
        for i in reversed(range(len(self._entries))):
            self._downheap(i)
                          
    