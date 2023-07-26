def getInts():
    return map(int, input().split())

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def main(a,b,n):
    sum = 0
    for i in range(1, n+1):
        if a <= sum_of_digits(i) <= b:
            sum += i
    print(sum)

n, a, b = getInts()
main(a,b,n)
