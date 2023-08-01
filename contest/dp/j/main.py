from functools import lru_cache


def getInt():
    return int(input())


def getIntsArray():
    return [int(x) for x in input().split()]


N = getInt()
nums_sushi = getIntsArray()


# @lru_cache(maxsize=None)
# def dp(i, j, k, N):
#     if i + j + k == 0:
#         return 0
#     result = N
#     if i > 0:
#         result += i * dp(i - 1, j, k, N)
#     if j > 0 and i + 1 <= N:
#         result += j * dp(i + 1, j - 1, k, N)
#     if k > 0 and j + 1 <= N:
#         result += k * dp(i, j + 1, k - 1, N)
#     return result / (i + j + k)


def solve(N, lst):
    """
    dpをどうとるか
    愚直に考えると、dp[a1][a2]...[aN]みたいにN次元欲しくなる。皿にその個数あるとき食べきる期待値という定義
    しかし、どの皿にあるかはどうでもよく、結局個数と枚数だけわかれば期待値は変わらない
    例えば個数が(1,2,2)という状態と(2,1,2)という状態の期待値は変わらない
    dp[i][j][k] = 1個の皿がi枚, 2個の皿がj枚, 3個の皿がk枚あるときの期待値
    """
    one = lst.count(1)
    two = lst.count(2)
    three = lst.count(3)

    dp = [[[0.0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    for k in range((three) + 1):
        for j in range((two + three) + 1 - k):
            for i in range((one + two + three) + 1 - k - j):
                if i + j + k == 0:
                    continue
                temp = N
                if i - 1 >= 0:
                    temp += i * dp[i - 1][j][k]
                if j - 1 >= 0 and i + 1 <= N:
                    temp += j * dp[i + 1][j - 1][k]
                if k - 1 >= 0 and j + 1 <= N:
                    temp += k * dp[i][j + 1][k - 1]
                dp[i][j][k] += temp / (i + j + k)
    return dp[one][two][three]


print(solve(N, nums_sushi))
