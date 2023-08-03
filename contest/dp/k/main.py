def getInts():
    return map(int, input().split())


def getIntsArray():
    return [int(x) for x in input().split()]


N, K = getInts()
choices = getIntsArray()

"""
何を状態として保持する？
dp[x]: x個以上石を取る最短の手数
dp[x+a_1], dp[x+a_2]..., dp[x+a_n]への遷移
最終的にdp(mod2)を答えればよい?
計算量はO(NK) <= O(10**7)

いや、dp[x]は今回のルールの取り方を表現できてない
ex) K = 4, choices = (2, 3)のとき
石の数は、4 -> 1 と遷移する
しかしdp[4] = 2で表現される取り方は 4 -> 2 -> 0である
INF = float("inf")
dp = [INF] * (K + 1)
for i in range(K):
    for choice in choices:
        if i + choice <= K:
            dp[i + choice] = min(dp[i + choice], dp[i] + 1)

turns = dp[K]
if turns % 2 == 0:
    print("Second")
else:
    print("First")
"""
"""
このルールの最適な取り方とは何か？
ex) K = 20, choices = (1,2,3)
これKが4nなら必ず後手が勝つ。相手と合わせて4になるように取り続ければいいから

相手とのchoiceの和で整理できないかな?
ex) choices = (2,3)
K = 4のとき
4 -> 1 でFirst
K = 5のとき
5 -> 2 -> 0
5 -> 3 -> 0でSecond
K = 7のとき
7 -> 4 -> 1 First
7 -> 5 こうすると自分が負けるから選ばない

どう選んでも勝ち負けが決まるゾーンがある
dp[x] := x個の石でゲームして、最初に行動するプレイヤーが勝つことができるか(0 or 1)
dp[x+a_n] = !dp[x]
"""
dp = [False] * (K + 1)
for i in range(K):
    for choice in choices:
        if i + choice <= K:
            dp[i + choice] = dp[i + choice] or not dp[i]
if dp[K]:
    print("First")
else:
    print("Second")
