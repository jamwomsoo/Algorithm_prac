n = int(input())
m = int(input())
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!= j:
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        if graph[i][j] != int(1e9) or graph[j][i] != int(1e9):
            tmp+=1
    print(n-tmp)
