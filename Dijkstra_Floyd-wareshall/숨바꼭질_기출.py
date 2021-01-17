#다익스트라는 무조건 우선순위 큐로 사용
#from collections import deque
import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [int(1e9)]*(n+1)
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
q =[] #deque()
heapq.heappush(q,(0,1))
#q.append((0,1))
distance[1] = 0
while q:
    cost, now = heapq.heappop(q)
    if distance[now] < cost:
        continue
    for i in graph[now]:
        c=cost+1
        if distance[i] > c:
            distance[i] = c
            heapq.heappush(q,(c,i))
            #q.append((c,i))
distance = [0 if distance[i] == int(1e9) else distance[i] for i in range(n+1) ]

print(f"{distance.index(max(distance))} {max(distance)} {distance.count(max(distance))}")             

