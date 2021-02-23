from collections import deque
from copy import deepcopy
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,q = map(int, input().split())
arr = []

big_ice_block = 0
for i in range(2**n):
    arr.append(list(map(int, input().split())))

visited = [[0]*2**n for _ in range(2**n)]
def bfs(x,y,num):
    global big_ice_block
    q = deque()
    q.append([x,y])
    visited[x][y] = num
    size = 1
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] > 0:
                q.append([nx,ny])
                visited[nx][ny] = num
                size+=1
    big_ice_block = max(big_ice_block, size)
def find_ice_block():
    global remain_ice
    number = 1

    for i in range(n):
        for j in range(n):

            if arr[i][j] > 0 and visited[i][j] == 0:
                bfs(i,j,number) 
                number+=1

n = 2**n
step = list(map(int, input().split()))
for index in range(q):
    l = step[index]
    flag = True
    if l == 0:
        pass
    else:
        k = 2**l
        for x in range(0,n,k):
            for y in range(0,n,k):
                tmp = [arr[z][y:y+k] for z in range(x,x+k)] 
                for i in range(k):
                    for j in range(k):
                        arr[x + j][y + k - i - 1] = tmp[i][j]
    # 얼음 제거
    cnt = [[0]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            for d in range(4):
                nx,ny = x+dx[d],y+dy[d]
                if 0<=nx<n and 0<=ny<n and arr[nx][ny]:
                    cnt[x][y]+=1

    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0 and cnt[x][y] < 3:
                arr[x][y] -= 1
find_ice_block()
print(sum(sum(i) for i in arr))
print(big_ice_block)