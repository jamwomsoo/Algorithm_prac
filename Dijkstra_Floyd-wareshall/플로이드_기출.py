n = int(input())# 도시 개수
m = int(input())# 버스 개수
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)

for k in range(1,n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == int(1e9):
            print(0,end=" ")
        else:
            print(graph[i][j],end = " ")
    print()

    


