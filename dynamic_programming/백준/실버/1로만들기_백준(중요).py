# dp[i] = min(i-1,i//2,i//5)+1
n = int(input())
dp = [0]*(1000001)
for i in range(2,n+1):
    # 바로 전 + 1
    dp[i] = dp[i-1] + 1
    # 바로 전꺼와 2로 나눈것에 대해 
    if i%2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])
    if i%3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i])

print(dp[n])