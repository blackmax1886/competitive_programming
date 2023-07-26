def getInt():
    return int(input())

def getIntsArray():
    return [int(x) for x in input().split()]

N = getInt()
heights = getIntsArray()

def dp(heights):
    # 各足場にいくための最小コスト
    costs = [0] * N
    # 足場iに行くときを考える
    # edge caseは後で考えることにして、rangeは適当に取っておく
    costs[0] = 0
    costs[1] = abs(heights[1]-heights[0])
    for i in range(2,len(heights)):
        costs[i] = min(costs[i-2]+abs(heights[i]-heights[i-2]), costs[i-1]+abs(heights[i]-heights[i-1]))
    return costs

costs = dp(heights)


print(costs[-1])
