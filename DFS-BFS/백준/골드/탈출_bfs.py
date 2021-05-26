from copy import deepcopy
from collections import deque
import sys
direction = [(-1,0),(1,0),(0,-1),(0,1)]
r,c = map(int ,input().split())
board = [list(map(str, input())) for _ in range(r)]
visited = []
dochi = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            visited.append([i,j])
            dochi.append([i,j,0])
def water_move(board):
    global r,c
    new_arr = deepcopy(board)
    for i in range(r):
        for j in range(c):
            if board[i][j] == "*":
                for dx,dy in direction:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<r and 0<=ny<c and board[nx][ny] != 'X' and board[nx][ny] != 'D':
                        new_arr[nx][ny] = '*'

    return new_arr
def dochi_move(board):
    global r,c,dochi
    new_q = deque()
    while dochi:
        x,y,cost = dochi.popleft()
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0<=nx<r and 0<=ny<c:
                if board[nx][ny] == '.':
                    if [nx,ny,cost+1] not in new_q and [nx,ny] not in visited:
                        new_q.append([nx,ny,cost+1])
                        visited.append([nx,ny])
                elif board[nx][ny] == 'D':
                    print(cost+1)
                    sys.exit()
    dochi =  new_q 

def check(board):
    global r,c
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                return True
    return False


while True:
    board = water_move(board)
    dochi_move(board)
    
    if not dochi or not check(board):
        print("KAKTUS")
        break