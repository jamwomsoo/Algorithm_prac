import sys
sys.setrecursionlimit(111111)
n ,m = map(int, input().split())
data = []

for i in range(n):
    data.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny <m:
            if visited[nx][ny] == False:
                if data[nx][ny] == 0:
                    dfs(nx,ny)
                if data[nx][ny] == 1:
                    touch[nx][ny]-=1
    return
cnt = 0
while True:
    check = True
    touch = [[0]*m for _ in range(n)]
    visited= [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                touch[i][j] = 2
                check = False
    if check:
        break
    cnt+=1
    dfs(0,0)
    for i in range(n):
        for j in range(m):
            if touch[i][j] <= 0:
                data[i][j] = 0
print(cnt)