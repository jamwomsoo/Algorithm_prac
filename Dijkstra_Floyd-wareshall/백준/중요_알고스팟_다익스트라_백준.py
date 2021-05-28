import sys
import heapq
# 방인 부분으로 갈때 거리를 0 추가하고 벽있는 부분으로 갈때는 거리를 1 추가하는 방식으로 함
m, n =map(int, input().split())
graph = []
distance =[[int(1e9)]*(m) for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = []
distance[0][0] = 0 # 거리
heapq.heappush(q,[0,0,0]) # 거리, x, y

while q:
    dist, x, y = heapq.heappop(q) 
    if x == n-1 and y == m-1:
        print(dist)
        break
    if distance[x][y] < dist:
        continue
    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                cost = dist + 1
            else:
                cost = dist
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,[cost,nx,ny])





