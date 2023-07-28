def getInt():
    return int(input())

def getFloatsArray():
    return [float(x) for x in input().split()]

N = getInt()
ps = getFloatsArray()

def solve(n, ps):
    """
    dp[i][j]:= i枚目までで、j枚表が出る確率
    0<=i<=N, 0<=j<=N
    最終的に求めるのは j >= (N // 2)
    dp[i][j]からdp[i+1][j+1] or dp[i+1][j]への遷移を考える
    """
    dp = [[0.00]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1.00
    for i in range(n):
        for j in range(i+1):
            dp[i+1][j+1] += dp[i][j] * ps[i]
            dp[i+1][j] += dp[i][j] * (1.00 - ps[i])
    half = n // 2 + 1
    return sum(dp[n][half:])

print(solve(N, ps))
