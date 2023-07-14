def getInt():
    return int(input())

def getInts():
    return map(int, input().split())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

def calcFare(start,goal,fares):
    return abs(fares[goal[0]-1][goal[1]-1] - fares[goal[0]-1][start[1]-1])

n, m = getInts()
fares = getIntsMatrix(n)
x = getInt()
routes = getIntsMatrix(x)
init = [[1,1]]
routes = init + routes

sum = 0
for i in range(len(routes)-1):
    sum += calcFare(routes[i], routes[i+1], fares)
