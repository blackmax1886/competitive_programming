def getInt():
    return int(input())

def getIntsArray():
    return list(map(int, input().split()))


def main(n, arr):
    sorted_arr = sorted(arr,reverse=True)
    alice = []
    bob = []
    for i in range(n):
        if (i % 2):
            bob.append(sorted_arr[i])
        else:
            alice.append(sorted_arr[i])
    return sum(alice) - sum(bob)

n = getInt()
arr = getIntsArray()

print(main(n,arr))
