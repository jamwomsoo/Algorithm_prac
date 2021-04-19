# 못품 -> 틀림
# https://www.acmicpc.net/problem/2156

# 점화식
# 세가지 방법에 의해 결정된다
# i 번째를 마실때
#  1. ooxo: 해당 i번과 i-2,i-3을 마신다
# 2. oxo: 해당 i번과 i-1을 마신다
# i 번째를 마시지 않는다
# 3. x
# 이 세가지중 가장 큰 값이 i번째 까지의 최대값인 dp[i]이 된다
n = int(input())

arr = [int(input()) for _ in range(n)]
arr.insert(0,0)
dp = [0]*(n+1)

for i in range(1,n+1):
    if i == 1:
        dp[i] = arr[i]
    elif i ==2 :
        dp[i] = arr[i]+arr[i-1]
    else:
        dp[i] = max(arr[i] + arr[i-1] + dp[i-3],dp[i-2] + arr[i],dp[i-1])
print(dp[n])