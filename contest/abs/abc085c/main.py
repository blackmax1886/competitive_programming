def getInts():
    return map(int, input().split())

def main(total_bills, total_sum):
    max_x = min(total_bills, total_sum//10000)
    for x in range(max_x, -1, -1):
        rest_bills = total_bills - x
        for y in range(rest_bills, -1, -1):
            z = rest_bills - y
            sum = x*10000 + y*5000 + z*1000
            if sum == total_sum:
                print("{} {} {}".format(x,y,z))
                return
    print('-1 -1 -1')

n, y = getInts()
main(n, y)
