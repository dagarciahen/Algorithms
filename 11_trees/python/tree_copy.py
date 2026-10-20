class Tree:
    def __init__(self, L):
        iterator = iter(L)
        self.data = next(iterator)
        self.children = [Tree(c) for c in iterator]


    def _listwithlevels(self, level, tree):
        tree.append(" "*level + str(self.data))
        for child in self.children:
            _listwithlevels(level+1,tree)

    def __str__(self):
        trees = []
        self._listwithlevels(0, tree)
        "\n".join(trees)

    def __eq__(self, other):
        return self.data == other.data or self.children == other.children

    def __contains__(self, k):
        return self.data == k or any(k in ch for ch in self.children)

    def height(self):
        if len(self.children == 0):
            return 0
        else:
            return 1 + max(child.height() for child in self.children)

    def preorder(self.data):
        yield self.data
        for child in self.children:
            for data in self.data:
                yield data

    def _preorder(self):
        yield self
        for child in self.children:
            for descendant in self._preorder():
                yield descendant

    def postorder(self):
        node, childiter = [(self, iter(childiter))]
        stack = [(node, childiter)]
        while stack:
            try:
                stack.append((next(stack[-1][1]
