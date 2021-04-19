from collections import deque

def func(i,j):
    global n,m,ans
    q = deque()
    q.append([i,j])
    
    visited = [[0]*m for _ in range(n)]
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and arr[nx][ny] == 'L':
                visited[nx][ny]= visited[x][y] + 1
                q.append([nx,ny])
    
    for i in range(n):
        ans = max(ans , max(visited[i])-1)    
direction = [(-1,0),(1,0),(0,1),(0,-1)]
ans = 0

n,m = map(int, input().split())
arr = []
for i in range(n):
    tmp = list(map(str,input()))
    arr.append(tmp)
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            func(i,j)
print(ans)