n = int(input())
m = int(input())

graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
visited = [[[] for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j :
            graph[i][j] = 0
            

for i in range(m):
    a,b,c = map(int,input().split())
    if graph[a][b] > c:
        graph[a][b] = c
        visited[a][b] = [a,b]



for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                visited[i][j] = visited[i][k][:-1] + visited[k][j]
             
                graph[i][j] = graph[i][k]+graph[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == int(1e9):
            graph[i][j] = 0
        print(graph[i][j],end = ' ')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if visited[i][j]:
            print(len(visited[i][j]),end = ' ')
            print(*visited[i][j])
        else: print(0)
    
