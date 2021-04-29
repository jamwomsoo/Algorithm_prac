import heapq
n,e = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    
    graph[a].append((b,c))
    graph[b].append((a,c))
pass_road = list(map(int,input().split()))


def dijkstra(start):
    q = [[0,start]]
    distance = [int(1e9)]*(n+1)
    
    
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])
    return distance

one = dijkstra(1)
p1 = dijkstra(pass_road[0])
p2 = dijkstra(pass_road[1])
ans = min(one[pass_road[0]] + p1[pass_road[1]] + p2[n], one[pass_road[1]] + p2[pass_road[0]] + p1[n])
if ans < int(1e9):
    print(ans)
else:
    print(-1)



