
T = Tree(['a', ['b', ['c', ['d']]], ['e', ['f'], ['g']]])

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
        trees.append(" "*level + str(data))
        for child in self.children:
            child._listwithlevels(level+1, trees)

    def __str__(self):
        trees = []
        self._listwithlevels(0, trees)
        return "\n".join(trees)

    def __eq__(self, other):
        return self.data == other.data and self.children == other.children

    def __contains__(self, k):
        return self.data == k or any(k in ch for ch in self.children)

    def height(self):
        if len(self.children) == 0:
            return 0
        else:
            return 1 + max(child.height() for child in self.children)

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


    def _postorder(self):
        node, childiter = self, iter(self.children)
        stack = [(node, childiter)]
        while stack:
            try:
                stack.append(next(stack[-1][1]), next(iter(stack[-1][1].children)))
            except StopIteration:
                yield stack[1][0]
                stack.pop()
    def postorder(self):
        return (node.data for node in self._postorder())




            

