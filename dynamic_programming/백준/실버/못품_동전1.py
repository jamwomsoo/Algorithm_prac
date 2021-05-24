# https://www.acmicpc.net/problem/2293
# 틀림
# 참고 https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-2293-%EB%8F%99%EC%A0%84-1
# 코인의 종류들 사이에서 하나씩 코인을 추가해보면서 i원을 만드는 방법을 구한다
# ex) 1 2 5  => 10원
#     1원  2원      3원          4원                     5원
#(1)  1   1,1      1,1,1         1,1,1,1                1,1,1,1,1
#(1,2)1   (1,1)+2 (1,1,1)+(1,2)  (1,1,1,1),(1,1,2),(2,2)

n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0]*(k+1)
dp[0] = 1
for coin in coins:
    for j in range(coin,k+1):
        #dp[j]에 dp[j-coin]에 현재 코인 종류를 추가해서 더해준다
        dp[j] += dp[j-coin]
print(dp[k])