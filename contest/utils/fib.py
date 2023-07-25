def fibonacci(n):
    dp = [0] * n
    dp[1] = 1
    for i in range(n-2):
        dp[i+2] = dp[i+1] + dp[i]
    return dp[n-1]

for i in range(2, 10):
    print(fibonacci(i))
