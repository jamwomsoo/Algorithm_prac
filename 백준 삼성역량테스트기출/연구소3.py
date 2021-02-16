from collections import deque
from itertools import combinations
import sys
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(n)]
_min = int(1e9)


def bfs(com): # 바이러스 모두 활성 시키면
    global m,n
    q = deque()
    _max = 0
    visited = [[-1]*n for _ in range(n)]
    for x,y in com:
        
        q.append((x,y))
        visited[x][y] = 0
    # for x in range(n):
    #     for y in range(n):
            
    #         print(visited[x][y],end = " ")
    #     print()
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if board[nx][ny] == 0 or board[nx][ny] == 2:
                        # if board[nx][ny] == 2:
                        #     visited[nx][ny] = 0
                        # else:
                        visited[nx][ny] = visited[x][y]+1
                        q.append((nx,ny))
                    
                    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 2 and visited[x][y] != 0:   
                continue
            if board[x][y] == 0 and visited[x][y] == -1:
                return None
            _max = max(_max,visited[x][y])
    #         print(visited[x][y],end = " ")
    #     print()
    # print()
    # print("mm",_max)
    return _max
ls = []

def solution(cnt):
    check = 0
    global _min,m,n
    for x in range(n):
        for y in range(n):
            if board[x][y] == 2:
                ls.append((x,y))
    coms = list(combinations(ls,m))
    
    for com in coms:
        
        tmp = bfs(com)
        if tmp == None:
            check+=1
        else:
            _min = min(_min,tmp )
    if len(coms) == check:
        _min =-1


solution(0)
print(_min)