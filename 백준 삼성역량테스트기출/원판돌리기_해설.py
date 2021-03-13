from collections import deque
import sys
input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n,m,t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
total=0
total_cnt = n*m
for i in range(n):
    total +=sum(board[i])
def bfs(x,y,num):
    global _sum,cnt,flag
    q = deque()
    q.append((x,y))
    visited = set()
    visited.add((x,y))
    while q:
        i,j = q.popleft()
        if board[i][j] ==-1:
            continue
        for d in range(4):                
            ni = i+dx[d]
            nj = j+dy[d]
            if (nj<=-1 or nj>m-1):
                if nj<=-1:
                    nj = m-1
                else:
                    nj = 0
            if 0<=ni<n and 0<=nj<m and (ni,nj) not in visited:
                if num == board[ni][nj]:
                    q.append((ni,nj))
                    visited.add((ni,nj))
                    flag = True
    if flag and len(visited)>1:
        for x,y in visited:
            _sum+=board[x][y]
            board[x][y] =-1
            cnt+=1
    
    return _sum, cnt, flag
                        

for _ in range(t):
    _sum = cnt = 0
    flag = False
    
    x,d,k =map(int, input().split())
    for i in range(n):
        if (i+1) % x == 0:
            for _ in range(k):
                if d == 0: # 시계
                    tmp = board[i][-1]
                    for j in range(m-1,0,-1):
                        board[i][j]=board[i][j-1]
                    board[i][0] = tmp

                else: #반시계
                    tmp = board[i][0]
                    for j in range(0,m-1):
                        board[i][j] = board[i][j+1]
                    board[i][-1] = tmp
    
    for i in range(n):
        for j in range(m):
            if board[i][j]!=-1:
                _sum, cnt, flag = bfs(i,j,board[i][j])
    
    total-=_sum
    total_cnt-=cnt
    if total_cnt == 0:
        print(0)
        sys.exit() 
    
    if not flag:
        tmp = total/total_cnt
        for x in range(n):
            for y in range(m):
                if board[x][y] == -1:
                    continue
                if board[x][y] < tmp:
                    board[x][y]+=1
                    total+=1
                elif board[x][y] > tmp:
                    board[x][y]-=1
                    total-=1
print(total)