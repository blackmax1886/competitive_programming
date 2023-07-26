import math

N = int(input())
numbers = list(map(int, input().split()))

def shift_only(arr):
    min_count = math.inf
    for i in numbers:
        count = 0
        while not (i % 2):
            count += 1
            i //= 2
        min_count = min(count, min_count)
    return min_count

print(shift_only(numbers))
