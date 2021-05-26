from collections import deque
import heapq
direction = [(0,-1),(0,1),(1,0),(-1,0)]

N,M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
name = [[0]*M for _ in range(N)]
index = 1
distance_q = []
# 1. 네이밍
def island_naming():
    global N,M,index
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and name[i][j] == 0:
                q = deque()
                visited = []
                name[i][j] = index
                q.append([i,j])
                visited.append([i,j])
                while q:
                    x,y = q.popleft()
                    for dx,dy in direction:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<N and 0<=ny<M and [nx,ny] not in visited and \
                            board[nx][ny] == 1 and name[nx][ny] == 0:
                            q.append([nx,ny])
                            visited.append([nx,ny])
                            name[nx][ny] = index
                index+=1
    
# 2. 여러지점의 최단거리 구하기
def check(x,y,d):
    dx = d[0]
    dy = d[1]
    cnt = 0
    now_index = name[x][y]
    while True:
        x+=dx;y+=dy
        cnt +=1
        if not (0<=x<N and 0<=y<M): return 
        if board[x][y] == 1 and name[x][y] == now_index: return
        if board[x][y] == 1 and name[x][y] != now_index: 
            heapq.heappush(distance_q,[cnt-1,now_index, name[x][y]])
            return
# 각 섬을 연결하는 최단 거리 구하기 
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        tmp = parent[b]
        for i in range(index):
            if parent[i] == tmp:
                parent[i] = a
        # parent[b] = a
        
    else:
        tmp = parent[a]
        for i in range(index):
            if parent[i] == tmp:
                parent[i] = b

        #parent[a] = b 

def is_all_island_linked():
    s = set(parent[1:])
    if len(s) == 1:
        return True
    return False

island_naming()

# print()

# for i in range(N):
#     for j in range(M):
#         print(name[i][j],end =' ')
#     print()
for i in range(N):
    for j in range(M):
        if  board[i][j] == 1:
            for dx,dy in direction:
                check(i,j,(dx,dy))

parent = [i for i in range(index)]
arr = set()
ans = 0

while distance_q:
    
    cost,a,b = heapq.heappop(distance_q) 
    if cost>=2:
        if find(parent,a) != find(parent, b):
            union(parent,a,b)
            #print(a,"와",b,"의 거리",cost)
            arr.add(a)
            arr.add(b)
            ans+=cost

#print(parent)
if not is_all_island_linked():
    print(-1)

else:
    if ans == 0: print(-1)
    else: print(ans)