import heapq

n,m = map(int, input().split())
distance = [int(1e9)]*(n+1)
distance[1] = 0
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
q = []
heapq.heappush(q,[0,1])
index = 0
arr = [[] for _ in range(n+1)]
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: continue
    for _next,c in graph[now]:
        cost = dist+c
        if distance[_next] > cost:
            
            arr[_next] = [now,_next]
            distance[_next] = cost
            heapq.heappush(q,[cost,_next])
ans = [] 

for i in range(2,n+1):
    if len(arr[i]) > 0:
        ans.append(arr[i])
print(len(ans))
for x in ans:
    print(*x) 