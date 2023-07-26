def getInt():
    return int(input())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat
    
class State():
    def __init__(self, input) -> None:
        self.time = input[0]
        self.x = input[1]
        self.y = input[2]


def isReachable(start, destination):
    time = destination.time - start.time
    dist = abs(start.x - destination.x) + abs(start.y - destination.y)
    if dist > time:
        return False
    else:
        return (dist % 2 == time % 2)

def main(plan):
    flag = False
    for i in range(len(plan)-1):
        start = State(plan[i])
        destination = State(plan[i+1])
        flag = isReachable(start, destination)
    if (flag):
        print('Yes')
    else:
        print('No')



n = getInt()
mat = getIntsMatrix(n)
init = [[0,0,0]]
plan = init + mat
main(plan)
