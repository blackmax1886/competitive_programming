def getInt():
    return int(input())

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

n = getInt()
workdays = getIntsMatrix(n)
workdays.sort(key=lambda x: x[0])

def isConsecutive(d1, d2):
    return d1[1] + 1 >= d2[0]

def getDays(d):
    return d[1] - d[0] + 1

max_length = 0
current = workdays[0]

for i in range(1, len(workdays)):
    if isConsecutive(current, workdays[i]):
        current[1] = max(current[1],workdays[i][1])
    else:
        max_length = max(max_length, getDays(current))
        current = workdays[i]

max_length = max(max_length, getDays(current))
print(max_length)
