def getInts():
    return map(int, input().split())

def getStrMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(input()))
    return mat

def solve(h, w, maze, mod):
    # dp[i][j] := (i+1,j+1)に到達する経路の数
    dp = [[0]*w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if i+1 <= h-1 and maze[i+1][j] == '.':
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= mod
            if j+1 <= w-1 and maze[i][j+1] == '.':
                dp[i][j+1] += dp[i][j]
                dp[i][j+1] %= mod
    return dp[h-1][w-1]

H, W = getInts()
maze = getStrMatrix(H)
MOD = pow(10,9) + 7
print(solve(H,W,maze,MOD))
