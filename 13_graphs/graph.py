class EdgeSetGraph:
    def __init__(self, V = (), E= ()):
        self._V = set()
        self._E = set()
        for v in V: self.addvertex(v)
        for u,v in E: self.addEdge(u,v)

    def vertices(self):
        return iter(self._V)

    def edges(self):
        return iter(self._E)

    def addvertex(self, v):
        self._V.add(v)

    def addedge(self, u, v):
        self._E.add((u,v))

    def removeedge(self, u, v):
        self._E.remove((u,v))

    def __contains__(self, v):
        return v in self._V

    def hasedge(self, u, v):
        return (u,v) in self._E

    def nbrs(self, v):
        return (w for u,w in self._E if u == v)

    def __len__(self):
        return len(self._V)

class UndirectedEdgeSetGraph(EdgeSetGraph):
    def addedge(self, u, v):
        self._E.add(frozenset({u,v}))

    def removeedge(self, u, v):
        self._E.remove(frozenset({u,v}))

    def nbrs(self, v):
        for u, w in self._E:
            if u == v:
                yield w
            elif w == v:
                yield u

class AdjacencySetGraph:
    def __init__(self, V = (), E = ()):
        self._V = set()
        self._nbrs = {}
        for v in V: self.addvertex(v)
        for e in E: self.addedge(*e)

    def vertices(self):
        return iter(self._V)

    def edges(self):
        for u in self._V:
            for v in self.nbrs(u):
                yield (u,v)

    def addvertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set()

    def addedge(self, u, v):
        self._nbrs[u].add(v)

    def removeedge(self, u, v):
        self._nbrs[u].remove(v)

    def __contains__(self, v):
        return v in self._nbrs

    def nbrs(self, v):
        return iter(self._nbrs[v])

    def __len__(self):
        return len(self._nbrs)

    ###pathh

    def ispath(self, V):
        """Return True if and only if the vertices V form a path."""
        return V and all(self.hasedge(V[i-1], V[i]) for i in range(1, len(V)))


G = AdjacencySetGraph({1,2,3}, {(1,2),(2,1),(1,3)})
print("neighbors of 1:", list(G.nbrs(1)))
print("neighbors of 2:", list(G.nbrs(2)))
print("neighbors of 3:", list(G.nbrs(3)))