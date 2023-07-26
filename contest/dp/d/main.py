def getInts():
    return map(int, input().split())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

# def solve(items, w):
#     items = [[0,0]] + items
#     n = len(items)
#     dp = [[0 for _ in range(w+1)] for _ in range(n)]
#     for i in range(n-1):
#         for j in range(w+1):
#             added_w = items[i+1][0]
#             added_v = items[i+1][1]
#             if j - added_w >= 0:
#                 dp[i+1][j] = max(dp[i][j-added_w]+added_v, dp[i][j])
#             else:
#                 dp[i+1][j] = max(dp[i][j], dp[i+1][j])
#     return dp[n-1][w]



N, W = getInts()
# Items = getIntsMatrix(N)
# print(solve(Items, W))

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

import numpy as np

# N, W = map(int, "5 10".split())
# m = map(int, "1 2 3 4 5 6 7 8 9 10".split())
WV = getIntsMatrix(N)

# 重さ -> 最大価値

dp = np.zeros(W+1,np.int64)

for w,v in WV:
    np.maximum(dp[w:],dp[:-w].copy()+v,out=dp[w:])

answer = dp.max()
print(answer)
