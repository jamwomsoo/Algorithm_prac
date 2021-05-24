n,k = map(int ,input().split())
coins = [int(input()) for i in range(n)]
coins.sort()
dp = [10001]*(k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin,k+1):
        dp[i] = min(dp[i],dp[i-coin]+1)
        
dp[-1] = dp[-1] if dp[-1] != 10001 else -1
print(dp[-1])