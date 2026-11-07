
#Minheap

class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

class HeapPQ:
    def __init__(self):
        self._entries = []

    def insert(self, item, priority):
        self._entries.append(Entry(item,priority))
        self._upheap(len(self._entries)-1)  

    def _parent(self, i):
        return (i-1)//2
    
    def _child(self, i):
        left = 2*i +1
        right = 2*i + 2
        return range(left, min(len(self._entries), right+1))

    def _swap(self, i, j):
        L = self._entries
        L[i], L[j] = L[j], L[i]

    def _upheap(self, i):
        L = self._entries
        parent = self._parent(i)
        if i > 0 and L[i].priority < L[parent].priority:
            self._swap(i, parent)
            self._upheap(parent)

    def findmin(self):
        return self._entries[0].item

    def removemin(self):
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._downheap(0)

    def _downheap(self, i):
        L = self._entries
        children = self._child(i)
        if children:
            child = min(children, key = lambda x : L[x].priority)
            if L[child].priority < L[i].priority:
                self._swap(i, child)
                self._downheap(child)

    def __len__(self):
        return len(self._entries)

    def _heapify(self):
        n = len(self._entries)
        for i in reversed(range(n)):
            self._downheap(i)






