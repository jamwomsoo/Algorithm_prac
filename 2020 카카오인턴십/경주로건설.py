import sys
from collections import deque
direction = [(-1,0),(1,0),(0,-1),(0,1)]

def solution(board):
    answer = sys.maxsize
    n = len(board)
    m = len(board[0])
    q = deque()
    q.append((0,0,4,0))
    # 이 부분 때문에 틀림
    visited={(0,0,1):0,(0,0,3):0}
    while q:
        x,y,d,c = q.popleft()
        if x ==n-1 and y == m-1:
            answer = min(answer,c)
        for k in range(4):
            dx,dy = direction[k]
            nx,ny = x+dx,y+dy 
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
                nc = c
                if d == 4:
                    nc+=100
                elif d<=1 and k<=1:
                    nc+=100
                elif d>=2 and k>=2:
                    nc+=100
                else:
                    nc += 600
                if not visited.get((nx,ny,k)) or visited[(nx,ny,k)] > nc:
                    visited[(nx,ny,k)] = nc
                    q.append((nx,ny,k,nc))
    return answer
#print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
#print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
#print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))