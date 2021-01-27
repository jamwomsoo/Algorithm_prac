from collections import deque
n = int(input())
Map = []
visited = [[False]*n for _ in range(n)]
for i in range(n):
    Map.append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ocean = set()
def separate(i,j,cnt):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    Map[i][j] = cnt
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == False and Map[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    Map[nx][ny] = cnt
                if visited[nx][ny] == False and Map[nx][ny] == 0:
                    ocean.add((x,y)) 
def check_mini(x,y):
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((x,y,0))
    index = Map[x][y]
    visited[x][y] = True

    while q:
        x,y,dist = q.popleft()
        # print("x,y ",x,y)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if Map[nx][ny] !=0 and Map[nx][ny] != index:
                    return dist 
                if visited[nx][ny] == False and Map[nx][ny] == 0:
                    q.append((nx, ny,dist+1))
                    visited[nx][ny] = True
    return int(1e9)

cnt = 1    
for i in range(n):
    for j in range(n):
        if Map[i][j] == 1 and visited[i][j] == False:
            separate(i,j,cnt)
            cnt+=1
ans = int(1e9)
for x,y in ocean:
    ans = min(check_mini(x,y),ans)
print(ans)
