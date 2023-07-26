def getInts():
    return map(int, input().split())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

def max_index_below_threshold(lst, value):
    return next((i for i in reversed(range(len(lst))) if lst[i] <= value), None)

def sum_last_column(matrix):
    return sum(row[-1] for row in matrix)

N, W = getInts()
WV = getIntsMatrix(N)

def solve(N, W, WV):
    # dp[i][sum_v]:= i番目までの品物から価値がsum_vとなるように選んだ時の重さ総和の最小値
    V = sum_last_column(WV)
    INF = float("inf")
    min_w = [[INF for _ in range(V+1)] for _ in range(N+1)]
    min_w[0][0] = 0
    WV = [[0, 0]] + WV
    for i in range(N):
        for sum_v in range(V+1):
            if sum_v-WV[i+1][1] >= 0:
                min_w[i+1][sum_v] = min(min_w[i][sum_v], min_w[i][sum_v-WV[i+1][1]]+WV[i+1][0])
            else:
                min_w[i+1][sum_v] = min(min_w[i][sum_v], min_w[i+1][sum_v])
    return max_index_below_threshold(min_w[-1], W)

print(solve(N,W,WV))
