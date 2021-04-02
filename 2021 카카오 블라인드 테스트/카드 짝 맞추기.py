# 63.3 통과 코드
import heapq
from collections import deque
from itertools import permutations

from copy import deepcopy
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def ctrl(board,x,y,direction):
    #print("ctrl",x,y)
    while True:
        x +=dx[direction]
        y +=dy[direction]
        #print(x,y)
        if not (0<=x<=3 and 0<=y<=3):
            x-=dx[direction]
            y-=dy[direction]
            return x,y
        if board[x][y] > 0:
            return x,y

def choose_first(board,x,y,goal):
    q = [[0,x,y]]
    tmp = []
    remain = 2
    while True:
        cnt,x,y = heapq.heappop(q)
       
        if board[x][y] == goal:
            #print("find_charactor",cnt,x,y)
            if (x,y) not in tmp:
                remain-=1
                tmp.append((x,y))
                if remain == 0:
                    return tmp
        for i in range(4):
            # 일반 방향 클릭
            nx,ny = x+dx[i],y+dy[i]
            if not (0<=nx<=3 and 0<=ny<=3): continue
            heapq.heappush(q,[cnt+1,nx,ny])
            # ctrl 방향 클릭
            if board[nx][ny] > 0: continue # 가장 가까운 캐릭이나 끝쪽으로 이동
            nx,ny = ctrl(board,nx,ny,i)
            heapq.heappush(q,[cnt+1,nx,ny])

def find_charactor(board,x,y,gx,gy):
    q = [[0,x,y]]
    
    while True:
        cnt,x,y = heapq.heappop(q)
       
        if x==gx and y == gy:
            #print("find_charactor",cnt,x,y)
            return cnt
        for i in range(4):
            # 일반 방향 클릭
            nx,ny = x+dx[i],y+dy[i]
            if not (0<=nx<=3 and 0<=ny<=3): continue
            heapq.heappush(q,[cnt+1,nx,ny])
            # ctrl 방향 클릭
            if board[nx][ny] > 0: continue # 가장 가까운 캐릭이나 끝쪽으로 이동
            nx,ny = ctrl(board,nx,ny,i)
            heapq.heappush(q,[cnt+1,nx,ny])


def dfs(per,index,board,total):
    if len(per) == index:
        answer = min(asnswer,total)
        return 
    for i in range()



answer = int(1e9)
def solution(board, r, c):
    
    remain = 0
    arr = set()
    n = len(board)
    m = len(board[0])
    # for i in range(n):
    #     for j in range(m):
    #         if board[i][j] > 0:
    #             remain+=1
    #             arr.add(board[i][j])
    # arr = list(arr)
    #print(arr)
   
    pers = list(permutations(arr,len(arr)))
    #print(pers)
    for per in pers:
        cnt = 0
        dfs(per,0,board,0)
               
            
        answer = min(cnt,answer)
    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],0,1))
#print(solution([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],1,0))