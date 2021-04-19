import heapq
for _ in range(int(input())):
    n,d,c = map(int, input().split())
    distance=[int(1e9)]*(n+1)
    distance[c] = 0 
    graph = [[] for _ in range(n+1)]
    for i in range(d):
        a,b,s = map(int, input().split())
        graph[b].append([a,s])
    q = [[0,c]]
    cnt = 0
    _max = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])

  
    for i in range(1,n+1):
        if distance[i] == int(1e9):
            continue
        cnt+=1
        _max = max(_max,distance[i]) 
    print(cnt, _max)   

