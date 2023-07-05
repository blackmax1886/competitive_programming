a, b = map(int, input().split())

def judgeOddEven(a, b):
    if (a*b%2):
        return 'Odd'
    else:
        return 'Even'

print(judgeOddEven(a,b))
