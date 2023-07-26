import numpy as np

def getInts():
    return map(int, input().split())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

H, W = getInts()
matrix = getIntsMatrix(H)

def solve(matrix, H, W):
    result = [[0 for _ in range(W)] for _ in range(H)]
    arr = np.array(matrix)
    row_sums = [0] * H
    col_sums = [0] * W

    for h in range(H):
        row_sums[h] = np.sum(arr[h, :])
    for w in range(W):
        col_sums[w] = np.sum(arr[:, w])

    for i in range(H):
        for j in range(W):
            row_sum = row_sums[i]
            col_sum = col_sums[j]
            result[i][j] = row_sum + col_sum - arr[i][j]
    return result

result = solve(matrix, H, W)
for row in result:
    print(' '.join(map(str, row)))
