def getInt():
    return int(input())

def getIntsVSet(N):
    s = set()
    for _ in range(N):
        s.add(int(input()))
    return s

n = getInt()
s = getIntsVSet(n)

print(len(s))
