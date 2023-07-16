import itertools


def getInt():
    return int(input())

def isvalid(S):
    score = 0
    for c in S:
        if c == '(':
            score += 1
        else:
            score -= 1
        if score < 0:
            return False
    
    return (score == 0)

n = getInt()
def solve(n):
    if n % 2 != 0:
        return
    else:
        for S in itertools.product(['(', ')'], repeat=n):
            if (isvalid(S)):
                print(*S, sep='')

solve(n)
