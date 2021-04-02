import heapq
def solution(n, edge):
    answer = 0
    graph =[[] for _ in range(n+1)]
    m = len(edge)
    distance = [int(1e9)]*(n+1)
    distance[1] = 0
    for i in range(m):
        a,b = edge[i]
        graph[a].append(b)
        graph[b].append(a)
    q = [(0,1)]
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now]<dist:
            continue
        for i in graph[now]:
           
            cost = dist+1
            if distance[i]>cost:
                distance[i] = cost
                heapq.heappush(q,(cost,i))
    print(distance)
    
    for i in range(n+1):
        if distance[i] == int(1e9): distance[i] = 0
    _max = max(distance)
    answer = distance.count(_max)
        

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))