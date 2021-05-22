v,e = map(int ,input().split(' '))
import heapq
k = int(input())
graph = [[] for _ in range(v)] 
for i in range(e):
    u,v1,w = map(int, input().split())
    graph[u-1].append([v1-1,w])

distance = [int(1e9)]*v
distance[k-1] = 0

q = [[0,k-1]]
while q:
    dis,now = heapq.heappop(q)
   
    if distance[now] < dis:
        continue
    for ele,d in graph[now]:
        cost = dis + d 
        if distance[ele] > cost:
           
            heapq.heappush(q,[cost, ele])
            distance[ele] = cost

for i in range(v):
    if i == k-1:
        print(0)
    else: 
        if distance[i] == int(1e9): print("INF") 
        else: print(distance[i])
     

