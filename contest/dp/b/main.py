def getInts():
    return map(int, input().split())

def getIntsArray():
    return [int(x) for x in input().split()]

N, K = getInts()
heights = getIntsArray()

def dp(heights, k):
    INF = float("inf")
    n = len(heights)
    costs = [INF] * n
    costs[0] = 0

    for i in range(1,n):
        for j in range(1,k+1):
            if i-j >= 0:
                costs[i] = min(costs[i], costs[i-j]+abs(heights[i]-heights[i-j]))
    return costs

costs = dp(heights, K)
print(costs[-1])
