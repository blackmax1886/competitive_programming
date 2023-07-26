s = input()
t = input()

def longest_common_subsequence(s, t):
    dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    res = ""
    i, j = len(s), len(t)
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            res = s[i-1] + res
            i -= 1
            j -= 1

    return res

print(longest_common_subsequence(s,t))
