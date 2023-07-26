import numpy as np

def getInts():
    return map(int, input().split())

def getIntsArray():
    return [int(x) for x in input().split()]

# def matrix_power_mod(A, n, mod):
#     result = np.eye(A.shape[0])
#     while n > 0:
#         if n % 2 == 1:
#             result = np.dot(result, A) % mod
#         A = np.dot(A, A) % mod
#         n //= 2
#     return result

def matrix_power_mod(matrix, k, mod):
    result = np.identity(len(matrix), dtype='object')
    while k > 0:
        if (k % 2) == 1: result = result @ matrix % mod
        matrix = (matrix @ matrix) % mod
        k //= 2
    return result

N, B, K = getInts()
chars = getIntsArray()
mod = pow(10,9)+7

'''
K種類の数字を使って作れるN桁の整数はN^K個 <= 10^(18*9) = 10^162
小課題1でも10^36

そこで使うのが桁DP
大きい問題を分割して小問題として解くのが動的計画法
整数を1桁ずつ上から処理していけば、動的計画法が適用できる

ここでは
dp[i][j]:= i桁でmod Bがjとなる整数の数
i: 0(1?) to N
j: 0 to B-1
'''

# dp = [[0 for _ in range(B)] for _ in range(N+1)]
# dp[0][0] = 1
# for i in range(N):
#     for j in range(B):
#         for k in chars:
#             remainder = (10*j + k) % B
#             dp[i+1][remainder] += dp[i][j]
# print(dp[N][0] % mod)

# 遷移行列を計算する
# i行j列目の要素は余りjから余りiへの遷移がいくつあるか
transition_matrix = [[0 for _ in range(B)] for _ in range(B)]
for b in range(B):
    for k in chars:
        remainder = (10*b + k) % B
        transition_matrix[remainder][b] += 1
nd_transion_matrix = np.array(transition_matrix,dtype='object')

# 遷移行列のn乗を繰り返し二乗法で求める
# msb_exponent = len(bin(N)) - 3
# power_of_transition_mat = []
# for i in range(msb_exponent+1):
#     p = pow(2, i)
#     power_of_transition_mat.append(np.linalg.matrix_power(nd_transion_matrix,p))

# そもそもnumpy.linalg.matrix_powerが繰り返し二乗法で実装されてるっぽいからそのまま使えばよいか
init_state = np.zeros(B, dtype='object')
init_state[0] = 1
result = np.dot(matrix_power_mod(nd_transion_matrix,N, mod),init_state)
# result = np.dot(np.linalg.matrix_power(nd_transion_matrix,N), init_state)
print(int(result[0] % mod))
