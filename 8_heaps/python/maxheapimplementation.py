##maxheap
class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.item < other.item
        return self.priority > other.priority

class HeapPQ:
    def __init__(self):
        self._entries = []

    def _parent(self, i):
        return (i-1)//2
    def _child(self, i):
        left = 2*i+1
        right = 2*i+2
        return range(left, min(len(self._entries), right+1))

    def _swap(self, i, j):
        L = self._entries
        L[i], L[j] = L[j], L[i]

    def _insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._upheap(len(self._entries)-1)

    def _upheap(self, i):
        L = self._entries
        parent = self._parent(i)
        if i > 0 and L[i] > L[parent]:
            self._swap(i, parent)
            self._downheap(parent)
    def findmin(self, i):
        return self._entries[-1]

    def removemax(self):
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._downheap(0)
        return item
        
    def _downheap(self, i):
        L = self._entries
        children = self._child(i)
        child = min(children, key = lambda x : L[x])

    def _heapify(self):
        n = len(self._entries)
        for i in reversed(range(n)):
            self._downheap(i)


