# 선과 후가 있는 것들 중에서 graph에는 자신보다 뒤에 있는것들이 들어간다

from collections import deque
n, k = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(k):
    first,second = map(int, input().split())
    graph[first][second] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1#min(graph[i][j],graph[i][k]+graph[k][j])

s = int(input())
for _ in range(s):
    a,b = map(int, input().split())
    if graph[a][b] == 1:
        print(-1)
    elif graph[b][a] == 1:
        print(1)
    else:
        print(0)
