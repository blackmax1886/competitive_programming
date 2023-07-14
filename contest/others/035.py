import math

def getInts():
    return map(int, input().split())

x1, y1, r1 = getInts()
x2, y2, r2 = getInts()

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

r_max = max(r1, r2)
r_min = min(r1, r2)

if r_max > d + r_min:
    relation = 1
elif r_max == d + r_min:
    relation = 2
elif r1 + r2 > d and r_max < d + r_min:
    relation = 3
elif r1 + r2 == d:
    relation = 4
else:
    relation = 5

print(relation)
