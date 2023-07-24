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

def make_directed_graph(node_num : int, edges: list):
    graph = {i: [] for i in range(1, node_num+1)}
    for start, end in edges:
        graph[start].append(end)
    return graph

def getInts():
    return map(int, input().split())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

def longest_path(graph, sorted_nodes):
    dist = {node: 0 for node in graph}
    dist[sorted_nodes[0]] = 0

    for node in sorted_nodes:
        for neighbour in graph[node]:
            dist[neighbour] = max(dist[neighbour], dist[node]+1)
    return max(dist.values())


N, M = getInts()
edges = getIntsMatrix(M)
dag = make_directed_graph(N,edges)
sorted_nodes = topological_sort(dag)
print(longest_path(dag,sorted_nodes))
