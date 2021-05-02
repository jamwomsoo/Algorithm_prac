from collections import deque 
import sys

direction = [(-1,0),(1,0),(0,1),(0,-1)]
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
time = 0
total = 0
for i in range(n):
    total += board[i].count(1)


def bfs():
    global n,m,total,time
    q = deque()
    q.append([0,0])
    visited = [[False]*m for _ in range(n)]
    tmp = []
    while q:
        x,y = q.popleft()
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if board[nx][ny] == 0:
                    q.append([nx,ny])
                if board[nx][ny] == 1:
                    tmp.append([nx,ny])
                visited[nx][ny] = True
    for x,y in tmp:
        board[x][y] = 0
    if total == len(tmp):
        print(time)
        print(total)
        sys.exit()
    else:
        total-=len(tmp)


while total>0:
    time +=1
    bfs()
    