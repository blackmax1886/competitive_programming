def getInt():
    return int(input())

def getInts():
    return map(int, input().split())

def getIntsArray():
    return [int(x) for x in input().split()]

# get vertical input of ints as array
def getIntsVArray(N):
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    return arr

# get vertical input of ints as set
def getIntsVSet(N):
    s = set()
    for _ in range(N):
        s.add(int(input()))
    return s

def getIntsMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    return mat

def getStrMatrix(N):
    mat = []
    for _ in range(N):
        mat.append(list(input().split()))
    return mat
