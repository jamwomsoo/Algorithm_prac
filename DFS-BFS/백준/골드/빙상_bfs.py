from copy import deepcopy
import sys

from collections import deque
direction = [(-1,0),(1,0),(0,1),(0,-1)]

n,m =map(int, input().split())

board = [list(map(int, input().split())) for i in range(n)]


def bfs():
    new_arr = deepcopy(board)
    
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                sea_aspect = 0
                for dx,dy in direction:
                    nx = i+dx
                    ny = j+dy
                    if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
                        sea_aspect+=1
                new_arr[i][j]-=sea_aspect
                if new_arr[i][j]<0:
                    new_arr[i][j] = 0
    return new_arr

def check_num_of_ice(visited, i ,j,index):
    q = deque()
    q.append([i,j])
    while q:
        x,y = q.popleft()

        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny] > 0 and visited[nx][ny] == -1 :
                visited[nx][ny] = index
                q.append([nx,ny])
                
        
                

time = 0
while True:
    index = 0
    visited = [[-1]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and visited[i][j] == -1:
                if index>=1: 
                    print(time)
                    sys.exit()
                visited[i][j] = index
                check_num_of_ice(visited,i,j,index)
                index+=1
    if index == 0: break
    
    time+=1
    # 얼음 크기 감소
    board = bfs()
    # 얼음덩이 check
    
print(0)