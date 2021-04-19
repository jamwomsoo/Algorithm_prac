# https://www.acmicpc.net/problem/2133
# 모름
import sys
n = int(input())
if n%2 == 1:
    print(0)
    sys.exit()
dp = [0]*(n+1)
dp[0] = 1
dp[2] = 3
for i in range(4,n+1,2):
    #    (이전의 경우의수) * (2를 만드는 방법이 3가지임) +  ---   |--| (이런식 두가지->C타입이라 하겠음)
    #                                                    |--|   ---
    dp[i] = dp[i-2]*3  + 2
    for j in range(2,i-2,2):
        dp[i]+=dp[j]*2 # (이전의 경우)*2

print(dp[n])