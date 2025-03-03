import heapq

def prim_mst(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    min_heap = [(0, 0, -1)]
    mst_cost = 0
    mst_edges = []

    while len(mst_edges) < num_vertices - 1:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight
        if parent != -1:
            mst_edges.append((parent, u, weight))
        for v in range(num_vertices):
            w = graph[u][v]
            if w > 0 and not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst_cost, mst_edges

num_vertices = int(input("Enter number of vertices: "))
graph = []
print("Enter adjacency matrix (use 0 for no edge): ")
for _ in range(num_vertices):
    graph.append(list(map(int, input().split())))

min_cost, min_edges = prim_mst(graph)

print("\nMinimum Cost Spanning Tree (MST) Edges:")
for u, v, w in min_edges:
    print(f"Edge ({u} - {v}) with weight {w}") 
print("Total Minimum Cost of MST:", min_cost)
