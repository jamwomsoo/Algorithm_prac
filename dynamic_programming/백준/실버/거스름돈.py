n = int(input())

dp = [int(1e9)]*(n+1)
if n>=2:
    dp[2] = 1
if n>=5: 
    dp[5] = 1

for i in range(1,n+1):
    if i-2 >0 :
        dp[i] = min(dp[i],dp[i-2]+1)
    if i-5>0:
        dp[i] = min(dp[i],dp[i-5]+1)
if dp[n] == int(1e9): print(-1)
else: print(dp[n])