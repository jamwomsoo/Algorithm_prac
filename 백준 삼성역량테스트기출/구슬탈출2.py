import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
rx, ry, bx, by = 0, 0, 0, 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n):
    arr.append(list(map(str,input().strip())))
    for j in range(m):
        if arr[i][j] == 'R':
            rx,ry = i,j
        if arr[i][j] == 'B':
            bx,by = i,j


def move(x,y,index):
    cnt = 0
    while arr[x+dx[index]][y+dy[index]] != '#' and arr[x][y] != 'O':
        x,y = x+dx[index],y+dy[index]
        cnt += 1
    return x,y,cnt
def bfs(rx,ry,bx,by,d):
    
    q.append([rx, ry, bx, by, d])
    visited.add((rx,ry,bx,by))
    while q:
        _rx, _ry, _bx, _by, _d = q.popleft()
        #print(_rx, _ry, _bx, _by, _d)
        if _d > 10:
            break
        for i in range(4):
            nrx,nry,rcnt = move(_rx, _ry, i)
            nbx,nby,bcnt = move(_bx, _by, i)
            if arr[nbx][nby] == 'O':
                continue
            if arr[nrx][nry] == 'O':
                print(_d)
                return
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append([nrx, nry, nbx, nby, _d+1])
    print(-1)
    return



q = deque()
visited = set()
bfs(rx,ry,bx,by,1)