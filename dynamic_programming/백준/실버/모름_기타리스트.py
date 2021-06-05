# 백준 사이트 : https://www.acmicpc.net/problem/1495
# 해설 사이트 : https://kils-log-of-develop.tistory.com/261

# 해설
# N번의 노래를 바꿀때 마다 해당 노래의 순번이 0 ~ M 음량까지 가능한게 있는지 확인한다

# 알고리즘
# 1. 0번 노래를 시작했을때부터 N번째까지 0~M 음량의 정보가 있는 배열을 만든다
# 2. 노래를 하나씩 실행하면서 이전의 음량으로 부터 현재 가능한 음량에 True 표시를 한다
# 3. 마지막 노래까지 도착했을때 가능한 음량 중 가장 큰 음량을 답으로 출력한다
N,S,M = map(int, input().split())
V = list(map(int, input().split()))
dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][S] = True

for i in range(1,N+1):
    for j in range(M+1):
        if dp[i-1][j] == False: continue

        if j - V[i-1] >= 0:
            dp[i][j - V[i-1]] = True 
        if j + V[i-1] <= M:
            dp[i][j + V[i-1]] = True
    
answer = -1

for i in range(M,-1,-1):
    if dp[N][i]:
        answer = i
        break

print(answer)


