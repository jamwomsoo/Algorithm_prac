import heapq
from collections import deque
from copy import deepcopy

n,m,k = map(int,input().split())
arr = []
exist = deque()
tree = [[[] for _ in range(n)] for _ in range(n)] #나무당 나이
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
for i in range(n):
    arr.append(list(map(int,input().split())))

nu = [[5]*n for _ in range(n)]
for i in range(m):
    x,y,z = map(int, input().split()) # x,y , 나이
    heapq.heappush(tree[x-1][y-1],z) 
    exist.append((x,y))
    #tree[x][y].append(z)

def spring(x,y,new_ls):
    print(x,y)
    if not tree[x][y]:
        tree[x][y] = new_ls
        if tree[x][y]: exist.append((x,y))
        return
    if tree[x][y][0] > nu[x][y]:
        summer(x,y)
        tree[x][y] = new_ls
        if tree[x][y]: exist.append((x,y))
        return
    if tree[x][y][0] <= nu[x][y]:
        age = heapq.heappop(tree[x][y])
        heapq.heappush(new_ls,age+1)
        nu[x][y]-=age
        spring(x,y,new_ls)
        
def summer(x,y):
    if not tree[x][y]:
        return
    age = heapq.heappop(tree[x][y])
    nu[x][y]+=(age//2)
    summer(x,y)
def fall(x,y):
    for i in tree[x][y]:
        if i %5 ==0:
            for j in range(8):
                nx, ny = x + dx[j], y+ dy[j]
                if not (0<=nx<n and 0<=ny<n):
                    continue
                heapq.heappush(tree[nx][ny],1)
                exist.append((nx,ny))
for i in range(k):
    # 봄
    print(i)
    length =len(exist)
    for i in range(length):
        x,y = exist.popleft()
        spring(x-1,y-1,[])
        
    # 여름
    
    # 가을
    length =len(exist)
    for i in range(length):
        fall(exist[i][0],exist[i][1])

    # 겨울
    for x in range(n):
        for y in range(n):
            nu[x][y]+=arr[x][y]
    
total=0
for i in range(n):
    for j in range(n):
        if tree[i][j]: total+=len(tree[i][j])
print(total)
    


