import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,charge = map(int,input().split())
    graph[a].append((b,charge))
start, end = map(int, input().split())
distance = [int(1e9)]*(n+1)
q = []
road = [[] for i in range(n+1)]
heapq.heappush(q,(0,start))
distance[start] = 0
road[start].append(start)

while q:
    print(q)
    
    dist, now = heapq.heappop(q)
    print(dist, now)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = i[1] + dist #now에서 i[0]까지 가는 거리와 현재 now의 거리 

        if cost < distance[i[0]]:
            road[i[0]] = [i[0]]
            road[i[0]]+=road[now]
           
            distance[i[0]]= cost
            heapq.heappush(q,(cost,i[0]))
print(distance[end])
print(len(road[end]))
for i in range(len(road[end])-1,-1,-1):
    print(road[end][i], end = " ")

