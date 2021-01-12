from collections import deque
n, k = map(int, input().split())
graph = [list((map(int,input().split()))) for i in range(n)]
s,final_x,final_y = map(int,input().split())
dx=[-1,0,1,0]
dy=[0,-1,0,1]

q=[]
cnt= 0
virus = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:                
            q.append((graph[i][j],0,i,j))
q.sort()
q=deque(q)        
while q:
    vi,time,x,y = q.popleft()
    if time == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny>= 0 and nx< n and ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = vi
                q.append((vi,time+1,nx,ny))
print(graph[final_x-1][final_y-1])  
                           
            



    

