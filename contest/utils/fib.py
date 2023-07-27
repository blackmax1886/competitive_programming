def fibonacci(n):
    dp = [0] * n
    dp[1] = 1
    for i in range(n-2):
        dp[i+2] = dp[i+1] + dp[i]
    return dp[n-1]

import numpy as np
def matrix_power_mod(matrix, k, mod):
    result = np.identity(len(matrix), dtype=int)
    while k > 0:
        if (k % 2) == 1: result = result @ matrix % mod
        matrix = (matrix @ matrix) % mod
        k //= 2
    return result

def fibonacchi_mod(n, mod):
    trans_mat = np.array([[1,1],[1,0]])
    init = np.array([1,0])
    trans = matrix_power_mod(trans_mat, n, mod)
    result = np.dot(trans, init)
    print(result)
    return result[1]

print(matrix_power_mod(np.array([[1,1],[1,0]]),4,100))
# print(fibonacchi_mod(pow(10,6),pow(2,31)))
# print(fibonacchi_mod(19,1000))
# print(fibonacchi_mod(9,20))
# print(fibonacchi_mod(29,17))
# print(fibonacchi_mod(10**14, 100007))
# for i in range(2, 10):
#     print(fibonacci(i))
