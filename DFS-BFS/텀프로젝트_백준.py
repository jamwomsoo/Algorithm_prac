# 순열 사이클 문제와 유사
# => 마지막 지목점이 처음 시작한 시작점을 가리켜야된다
# 싸이클에 포함되지 않는 부분은 뺀다
import sys
# 충분한 재귀 깊이를 주어 오류방지
# n이 100000이므로 그것보다 살짝 크게 진행
sys.setrecursionlimit(111111) 

def dfs(x):
    global ans
    cycle.append(x)
    visited[x] = True
    number = select[x]
    if visited[number]:
        if number in cycle:
            # 싸이클이 발생한 곳 부터 결과값에 집어 넣는다 
            ans += cycle[cycle.index(number):]
        return
    else:
        dfs(number)


for _ in range(int(input())):
    n = int(input())
    select=[0]+ list(map(int,input().split()))
    ans= []
    visited = [True]+[False]*n
    for i in range(1,n+1):
        if not visited[i]:
            cycle = [] # 싸이클 확인용
            dfs(i)
    print(n-len(ans))       
