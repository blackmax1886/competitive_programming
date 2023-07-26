# N個の皿に、ボールが載ってるかどうか = 2^n
# できる限り多くの皿にボールを載せるのが最大？→条件次第な気がする

import itertools


N, M = map(int, input().split())
cond = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
choice = [tuple(map(int, input().split())) for i in range(K)]
ans = 0
for balls in itertools.product(*choice):
    balls = set(balls)
    count = 0
    # count = sum(a in balls and b in balls for a, b in cond)
    for a, b in cond:
        if a in balls and b in balls:
            count += 1
    ans = max(ans, count)
print(ans)
