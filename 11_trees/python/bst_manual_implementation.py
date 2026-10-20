import Mapping

class BSTMapping(Mapping):
    def __init__(self):
        self._root = None

    def get(self, key):
        if self._root:
            return self._root.get(key).value
        raise KeyError

    def put(self, key, value):
        if self._root:
            return self._root.put(key, value)
        else:
            self._root = BSTNode(key, value)

    def __len__(self, key, value):
        return len(self._root) if self._root is not None else 0

    def _entryiter(self):
        if self._root:
            yield from self._root ## same as for item in iter(self._root): yield item 

    def floor(self, key):
        if self._root:
            floornode = self._root.floor(key)
            if floornode is not None:
                return floornode.key, floornode.value

        return None, None

    def remove(self, key):
        if self._root:
            self._root = self._root.remove(key)
        else:
            raise KeyError

    def __delitem__(self, key):
        self.remove(key)


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self._length = 1
        

    def __len__(self):
        return len(self._length)

    def __str__(self):
        return str(self.key) + " : " str(self.value)

    def get(self, key):
        if key == self.key:
            return self.value
        elif key < self.key and self.left:
            return self.get(key)
        elif key > self.key and self.right:
            return self.get(key)
        else:
            raise KeyError

    def put(self, key, value):
        if key == self.key:
            self.value = value
        elif key < self.key:
            if self.left:
                return self.left.put(key,value)
            else:
                self.left = BTSNode(key, value)
        elif key > self.key:
            if self.right:
                return self.right.put(key, value)
            else:
                self.right = BTSNode(key, value)
        self._updatelength()

    def _updatelength(self):
        len_left = len(self.left) is self.left else 0
        len_right = len(self.right) is self.right else 0
        self._length = 1 + len_left + len_right

    def floor(self, key):
        if self.key == key:
            return self
        elif key < self.key:
            if self.left is not None:
                return self.left.floor(key)
            else:
                return None
        elif key > self.key:
            if self.right is Not None:
                return self.right.floor(key)
            else:
                return None
        else:
            return self

    def __iter__(self):
        if self.left is not None:
            yield from self.left
        yield self
        if self.right is not None:
            yield from self.right

    def _swapwith(self, other):
        self.key, other.key = other.key, self.key
        other.value, self.value = self.value, other.value

    def maxnode(self):
        return self.right.maxnode() if self.right else self

    def remove(self, key):
        if self.key == key:
            if self.left is None: return self.right
            if self.right is None: return self.left
            self._swapwith(self.left.maxnode())
            self.left = self.left.remove(key)
        elif key < self.key and self.left:
            self.left = self.left.remove(key)
        elif key > self.key and self.right:
            self.right = self.right.remove(key)
        else: raise KeyError
        self._updatelength()
        return self



