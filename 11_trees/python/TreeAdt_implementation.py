T = ['c', ['a', ['p'], ['n'], ['t']], ['o', ['n']]]


def printtree_first(T):
    print(T[0])
    for child in range(1, len(T)):
        printree(T[child])

def printtree_iter(T):
    iterator = iter(T)
    print(next(iterator))
    for child in range(1, len(T)):
        printtree_iter(T)


class Tree:
    def __init__(self, L):
        iterator = iter(L)
        self.data = next(iterator)
        self.children = [Tree(c) for c in iterator]

    def printtree(self):
        print(self.data)
        for child in self.children:
            child.printtree()

    def _listwithlevels(self, level, trees):
        trees.append(" "*level + str(self.data))
        for child in self.children:
            child._listwithlevels(level +1, trees)


    def __str__(self, level = 0):
        trees = []
        self._listwithlevels(0, trees)
        return "\n".join(trees)

    def __eq__(self, other):
        return self.data == other.data and self.children == other.children

    def height(self):
        if len(self.children) == 0:
            return 0
        else:
            return 1 + max(child.height() for child in self.children)

    def __contains__(self, k):
        return self.data == k or any(k in ch for ch in self.children)
    
    def printpostorder(self):
        for child in self.children:
            child.printpostorder()
        print(self.data)

    def preorder(self):
        yield self.data
        for child in self.children:
            for data in child.preorder():
                yield data

    __iter__ = preorder

    def _preorder(self):
        yield self
        for child in self.children:
            for descendant in child._preorder():
                yield descendant


T = Tree(['a', ['b', ['c', ['d']]], ['e', ['f'], ['g']]])


print("printtree:")

T.printtree()
print("printpostorder")
T.printpostorder()

print("preorder")
for n in T._preorder():
    print(n.data)

