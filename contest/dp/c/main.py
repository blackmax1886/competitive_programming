def getInt():
    return int(input())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

N = getInt()
actions = getIntsMatrix(N)

def dp(actions):
    n = len(actions)
    # i日目にA,B,Cを行ったときの最大幸福度
    max_happys = [[0,0,0] for i in range(n)]
    max_happys[0] = actions[0]
    for i in range(1,n):
        happy_a = max(max_happys[i-1][1], max_happys[i-1][2]) + actions[i][0]
        happy_b = max(max_happys[i-1][0], max_happys[i-1][2]) + actions[i][1]
        happy_c = max(max_happys[i-1][0], max_happys[i-1][1]) + actions[i][2]
        max_happys[i] = [happy_a, happy_b, happy_c]
    return max_happys

max_happys = dp(actions)
print(max(max_happys[-1]))
