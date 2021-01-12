#n=도시의 개수, m= 도로의 개수, k=거리 정보, x 출발 도시의 번호
from collections import deque
n ,m ,k ,x = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

def bfs():
    check = False
    q=deque()
    q.append((x,0))
    short_dist = [int(1e9)]*(n+1)
    vistied = [False]*(n+1)
    while q:
        now, distance = q.popleft()
        if vistied[now] == True:
            continue
        vistied[now] = True
        short_dist[now] = distance
        distance+=1
        for i in graph[now]:     
            q.append((i,distance))           
    for i in range(1,len(short_dist)):
        if short_dist[i] == k:
            check = True
            print(i)
    if check == False:
        print(-1)

bfs()
