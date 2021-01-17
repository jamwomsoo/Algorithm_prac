from collections import deque

for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    graph = [ [False]*(n+1) for _ in range(n+1)]
    indegree = [0]*(n+1)
    for i in range(n):
        for j in range(i+1,n):
            graph[data[i]][data[j]] =True
            indegree[data[j]]+=1

    for i in range(int(input())):
        a,b = map(int, input().split())
        # 간선 반대로
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    cycle = False
    certain = True
    q=deque()
    result = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >=2:
            certain =False
            break
        now = q.popleft()
        result.append(now)
        for j in range(1,n+1):
            #graph[now][j] = False
            indegree[j]-=1
            if indegree[j] == 0:
                q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in range(n):
            print(result[i],end = " ")
        print()

        

