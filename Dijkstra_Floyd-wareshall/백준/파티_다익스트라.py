import heapq
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[int(1e9)]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
def djikstra(num):
    
    distance[num][0] = 0
    q =[]
    heapq.heappush(q,[0,num])
    while q:
        dist, now = heapq.heappop(q)
        if distance[num][now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if distance[num][i[0]] > cost:
                distance[num][i[0]] = cost
                heapq.heappush(q,[cost,i[0]])
for i in range(1,n+1):
    djikstra(i)
#print(distance[1][1])
ans = 0
for i in range(1,n+1):
    if x==i: continue
    # print(distance[i] , distance[x])
    # print(distance[i][x] , distance[x][i])
    ans = max(distance[i][x] + distance[x][i],ans)


print(ans)

# graph = [[int(1e9)]*(m+1) for _ in range(n+1)]

# for i in range(m):
#     a,b,c = map(int, input().split())
#     graph[a][b] = c
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j : graph[i][j] = 0
# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
# ans = 0
# for i in range(1,n+1):
#     if x==i: continue
#     ans = max(graph[i][x]+graph[x][i],ans)

# print(ans)
