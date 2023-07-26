from collections import deque

def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    Q = deque([u for u in in_degree if in_degree[u] == 0])

    L = []

    while Q:
        u = Q.popleft()
        L.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.append(v)

    if len(L) == len(graph):
        return L
    else:
        return []

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['B','D'],
#     'D': [],
# }

# print(topological_sort(graph))

def make_directed_graph(node_num : int, edges: list):
    graph = {i: [] for i in range(1, node_num+1)}
    for start, end in edges:
        graph[start].append(end)
    return graph
