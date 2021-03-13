n = int(input())
dp = [int(1e9)]* 5001
dp[3] = 1; dp[5] = 1
for i in range(1,n+1):
    dp[i] = min(dp[i],dp[i-3]+1,dp[i-5]+1)

if dp[n] == int(1e9):
    print(-1)
else:
    print(dp[n])