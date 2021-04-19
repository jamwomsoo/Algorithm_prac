n = int(input())
graph = []
visited = [[False]*(n) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    graph.append(list(map(int,input())))



def dfs(num,x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                visited[nx][ny] = True
                graph[nx][ny] = num
                dfs(num,nx,ny)
    return 
num = 1
for i in range(n):
    for j in range(n):
        #print(visited[i][j], graph[i][j])
        if visited[i][j] == False and graph[i][j] == 1:
            #print(graph,"\n")
            visited[i][j] = True
            graph[i][j] = num    
            cnt = dfs(num,i,j)
            num+=1
print(num-1)
ans=[]
for i in range(1,num):
    cnt = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] == i:
                cnt+=1
    ans.append(cnt)
ans.sort()
for i in ans:
    print(i)