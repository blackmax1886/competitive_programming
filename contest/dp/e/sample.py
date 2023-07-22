INF = float('inf')
vmax = 7  # vi_max * N_max

N, W = map(int, input().split())
WV = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[INF] * (vmax + 1) for _ in range(N + 1)]
dp[0][0] = 0
for n in range(N):
  for v in range(vmax + 1):
    wn, vn = WV[n]
    dp[n + 1][v] = dp[n][v]
    if v - vn >= 0:
      dp[n + 1][v] = min(dp[n + 1][v], dp[n][v - vn] + wn)

for v in range(vmax + 1):
  if dp[N][v] <= W:
    ans = v
print(ans)
