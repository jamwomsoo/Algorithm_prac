from collections import deque
import sys
#(x,y,z)
direction = [(-1,0,0),(1,0,0),(0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
while True:
    L,R,C = map(int, input().split())
    if L == 0 and R == 0 and C==0: break
    
    building = [[list(map(str, input())) if i!=R else input() for i in range(R+1)] for _ in range(L)] 
    
    q = deque()
    visited = [[[-1]*C for _ in range(R)] for _ in range(L)]
    flag = False
    for floor in range(L):
        for i in range(R):
            for j in range(C):
                if building[floor][i][j] == 'S':
                    q.append([floor,i,j])
                    visited[floor][i][j] = 0
                    flag = True
                    break
            if flag:
                break
        if flag:
                break

    
    while q:
        f, x, y = q.popleft()
        
        if building[f][x][y] == 'E':
            print("Escaped in {0} minute(s).".format(visited[f][x][y]))
            flag = False
            break
        for df,dx,dy in direction:
            nf = f+df ; nx = x+dx ; ny = y + dy
            if 0<=nf<L and 0<=nx<R and 0<=ny<C and building[nf][nx][ny] != '#' and visited[nf][nx][ny] == -1:
                q.append([nf,nx,ny])
                visited[nf][nx][ny] = visited[f][x][y]+1
    if not flag: continue
    print("Trapped!")
