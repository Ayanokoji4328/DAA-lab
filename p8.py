class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find_parent(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find_parent(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x, root_y = self.find_parent(parent, x), self.find_parent(parent, y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
                rank[root_y] += rank[root_x] == rank[root_y]

    def kruskal_mst(self):
        self.edges.sort()
        parent = list(range(self.V))
        rank = [0] * self.V
        mst = []

        for weight, u, v in self.edges:
            root_u, root_v = self.find_parent(parent, u), self.find_parent(parent, v)
            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)
                if len(mst) == self.V - 1:
                    break

        print("Edges in MST:")
        for u, v, w in mst:
            print(f"{u} -- {v} == {w}")
        print("Minimum Cost:", sum(w for _, _, w in mst))


V = int(input("Enter number of vertices: "))
g = Graph(V)

print("Enter adjacency matrix (use 0 for no edge):")
for i in range(V):
    for j, w in enumerate(map(int, input().split())):
        if i < j and w:
            g.add_edge(i, j, w)

g.kruskal_mst()
