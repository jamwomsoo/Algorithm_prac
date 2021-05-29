# 못품
# 백준 사이트 : https://www.acmicpc.net/problem/2624
# 풀이 사이트 : https://www.landlordgang.xyz/33
# 해설
#동전 문제와 비슷
# 이차원배열 [사용한 동전 가지수][금액]
# 사용하는 동전의 가지수를 한개씩 늘려가며 => [동전가지수 -1][금액 - 현재 사용하려는 동전종류* 동전 개수]


# 알고리즘

# 1. 이차원배열 [사용한 동전 가지수][금액]을 만든다
# 2. 동전의 가지수를 범위로 잡는 for문을 돌린다(동전을 한종류씩 늘려가며 사용한다)
#   Case 나눈거아님
#   2-1. [현재 사용하는 동전 가지수][현재금액] = [현재 사용하는 동전 가지수 -1][현재 금액]
#      -> 이전 동전가지수껏을 그대로 가져온다
#   2-2. 동전 문제와 같이 
#           [현재 동전가지수][만들려는 금액]+= [이전 동전 가지수](만들고싶은 금액 - 현재 동전으로 만든 금액(현재 순서의 동전의 종류*동전 사용 갯수))

from copy import deepcopy
t = int(input()) # 금액
k = int(input()) # 동전 종류 
coin = [list(map(int, input().split()) for _ in range(k))]
dp = [[0]*(t+1) for _ in range(k+1)]
dp[0][0] = 1

for i in range(1,k+1): # i== 사용한 동전의 가지 수
    for tt in range(t+1): # 금액
        dp[i][tt] = dp[i-1][tt] 
    for j in range(1, coin[i-1][0] + 1): # 해당 종류의 동전의 개수
        for index in range(j*coin[i-1][0],t+1): # 금액(동전종류 * 동전개수)
            dp[i][index] += dp[i-1][index - j*coin[i-1][0]]

print(dp[k][t])