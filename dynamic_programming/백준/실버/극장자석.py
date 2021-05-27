n = int(input())
m = int(input())
dp = [0]*(n+1)
dp[1] = dp[0] = 1
for i in range(2,n+1):
    dp[i] = dp[i-2] + dp[i-1]

arr = [int(input()) for _ in range(m)]
s = e = 0
ans = 1
for i in range(1,n+1):
    if i not in arr:
        e+=1
    else:
     
        ans*=dp[e-s]
        s = e = i+1
ans*=dp[e-s]
print(ans)
