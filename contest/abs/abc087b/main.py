def getInt():
    return int(input())

def count_two_coins_combination(coin1, coin2, sum):
    count = 0
    coin1_max = min(coin1, sum//100)
    for i in range(coin1_max+1):
        coin2_goal = sum - 100*i
        if (coin2_goal % 50 == 0 and coin2_goal//50 <= coin2):
            count += 1
    return count

def count_three_coins_combination(coin0,coin1,coin2, sum):
    count = 0
    coin0_max = min(coin0, sum//500)
    for i in range(coin0_max+1):
        rest = sum - 500*i
        count += count_two_coins_combination(coin1, coin2, rest)
    return count

a = getInt()
b = getInt()
c = getInt()
x = getInt()

print(count_three_coins_combination(a,b,c,x))

# count_two_coins_combination(50, 50, 1000)
