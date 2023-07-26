from collections import deque


def getInt():
    return int(input())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

def find_max_index(numbers):
    max_index, max_value = max(enumerate(numbers), key=lambda pair: pair[1])
    return max_index

N = getInt()
roads = getIntsMatrix(N-1)
roads = [[node-1 for node in road] for road in roads]

class Node:
    def __init__(self, index) -> None:
        self.index = index
        self.nears = []

    def __repr__(self) -> str:
        return f"(index:{self.index}, nears:{self.nears})"
    
nodes = [Node(i) for i in range(N)]
for road in roads:
    left = road[0]
    right = road[1]
    nodes[left].nears.append(right)
    nodes[right].nears.append(left)

def bfs(index):
    distances = [-1] * N
    distances[index] = 0
    frontier = deque([])
    frontier.append(nodes[index])
    while frontier:
        current_node = frontier.pop()
        for next in current_node.nears:
            if distances[next] == -1:
                distances[next] = distances[current_node.index] + 1
                frontier.append(nodes[next])
    return distances

dist0 = bfs(0)
furthest = find_max_index(dist0)
dist = bfs(furthest)
diameter = max(dist) + 1
print(diameter)


# N = int(input())
# G = [[] for _ in range(N)]
# for _ in range(N - 1):
#     a, b = map(int, input().split())
#     a, b = a - 1, b - 1  # 0-indexed に
#     G[a].append(b)
#     G[b].append(a)

# # 頂点 s から DFS (ここではスタックを使う)
# def dfs(s):
#     # 頂点 s からの距離
#     dist = [-1] * N
#     dist[s] = 0

#     # スタックで DFS
#     st = [s]
#     while st:
#         v = st.pop()
#         for nv in G[v]:
#             if dist[nv] == -1:
#                 st.append(nv)
#                 dist[nv] = dist[v] + 1

#     # リターン
#     return dist

# # 頂点 0 から
# dist0 = dfs(0)
# mv = max(enumerate(dist0), key=lambda x: x[1])[0]
# distmv = dfs(mv)
# print(max(distmv) + 1)
