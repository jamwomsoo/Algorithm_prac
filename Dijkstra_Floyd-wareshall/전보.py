import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n,m,c = map(int,input().split())
#start = c
graph=[[] for _ in range(n+1)]

distance=[INF]*(n+1)

for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
def dijkstra(c):
    q=[]
    heapq.heappush(q,(0,c))
    distance[c] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q,(cost,j[0]))

dijkstra(c)
# cnt=0

# for a in range(0,n+1):
#   if distance[a] == INF:
#     distance[a] = -1
#   if distance[a] <= 0:
#     pass
#   else:
#     cnt+=1

# print(cnt, end =" ")
# print(max(distance))

#해설
cnt=0
max_value=0
for i in range(n+1):
    if distance[i] != INF:
        cnt+=1
        max_value = max(max_value,distance[i])

print(cnt-1, max_value)
