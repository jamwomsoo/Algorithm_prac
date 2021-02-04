# 못품 
# 다음기회에...

import heapq
from collections import deque
n,m,t,d = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(str,input())))
for i in range(n):
    for j in range(m):
        graph[i][j] = ord(graph[i][j]) - ord("A") 
print(graph)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
back = [[int(1e9)]*(m) for _ in range(n)]
distance = [[int(1e9)]*(m) for _ in range(n)]

def bfs():
    q = deque()
    q.append([0,0])
    distance[0][0] = 0

    while q:
        #print(q)
        x, y = q.popleft()#heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if abs(graph[x][y] - graph[nx][ny]) <= t:
                    if graph[x][y] >= graph[nx][ny]: 
                        cost = distance[x][y] + 1
                    else:
                        cost = distance[x][y] +  (graph[x][y] - graph[nx][ny])**2
                    if cost > d:
                        continue
                    if distance[nx][ny] == int(1e9) or distance[nx][ny]>cost:
                        distance[nx][ny] = cost
                        q.append([nx,ny])
        
def bfs2():
    q = deque()
    q.append([0,0])
    back[0][0] = 0

    while q:
        #print(q)
        x, y = q.popleft()#heapq.heappop(q)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if abs(graph[x][y] - graph[nx][ny]) <= t:
                    if graph[x][y] <= graph[nx][ny]: 
                        cost = back[x][y] + 1
                    else:
                        cost = back[x][y] +  (graph[x][y] - graph[nx][ny])**2
                    if cost>d:
                        continue
                    if back[nx][ny] == int(1e9) or back[nx][ny]>cost:
                        back[nx][ny] = cost
                        q.append([nx,ny])
bfs()
bfs2()
res = 0

for i in range(n):
    for j in range(m):
        print(distance[i][j],end = " ")
    print()
for i in range(n):
    for j in range(m):
        print(back[i][j],end = " ")
    print()

for i in range(n):
    for j in range(m):
        if distance[i][j] == int(1e9) or back[i][j] == int(1e9):
            continue
        if distance[i][j] + back[i][j] <= d:
            
            res = max(res, graph[i][j])
print(res)
