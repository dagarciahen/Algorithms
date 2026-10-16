
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

    def _listwithlevels(self, trees):
        trees.append(" "*level, str(self.data))
        for child in self.children:
            child._listwithlevels(level+1, trees)

    def __str__(self):
        trees = []
        self._listwithlevels(self, trees)
        return "\n".join(trees)

    def __eq__(self, other):
        self.data == other.data and self.children == other.children


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

    def _preorder(self):
        yield self
        for child in self.children:
            for descendant in child._preorder():
                yield descendant
        def _postorder(self):
        node, childiter = self, iter(childiter)
        stack = [(node, childiter)]
        while stack:
            node, childiter = stack[-1]
            try:
                child = next(childiter)
                stack.append((child, iter(child.children)))
            except StopIteration:
                yield node
                stack.pop()

    def _preorderbetter(self):
        node, childiter = self, iter(childiter)
        stack = [(node, childiter)]
        while stack:
            try:
                stack.append((next(stack[-1][1]), iter(next(stack[-1][1].children))))
            except StopIteration:
                yield stack[-1][0]
                stack.pop()


    def postorder(self):
        return (node.data for node in self._postorder())


##how to avoid reassingn ode and childiter at every iteration 
    



def printpreorder(T):
    print(T.data)
    for child in self.children:
        printpreorder(T)



def printpostorder(self):
    for child in self.children:
        printpostorder(T)
    print(T.data)

        

