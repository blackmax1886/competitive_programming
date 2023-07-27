from collections import deque

"""
Parameters:
graph : dict - グラフを表す辞書。キーは頂点、値はその頂点から出ていくエッジの終点のリスト。

Returns:
list - トポロジカルソートされたノードのリスト。巡回が存在する場合、空のリストを返します。
"""
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

"""
この関数は、頂点の数とエッジのリストを与えると、有向グラフを表現する辞書を作成します。

各頂点は1からnode_numまでの整数で表されます。エッジは、(始点, 終点)の形式のタプルかリストで表されます。 
エッジのリストは、すべてのエッジを含むリストで、エッジの始点と終点は頂点に対応します。

グラフは辞書で表現され、キーは頂点で、値はその頂点から出ていくエッジの終点のリストです。

Parameters:
node_num : int - グラフの頂点の数
edges : list - エッジのリスト。各エッジは (始点, 終点)の形式のタプルかリスト

Returns:
graph : dict - グラフを表す辞書。キーは頂点、値はその頂点から出ていくエッジの終点のリスト
"""
def make_directed_graph(node_num : int, edges: list):
    graph = {i: [] for i in range(1, node_num+1)}
    for start, end in edges:
        graph[start].append(end)
    return graph
