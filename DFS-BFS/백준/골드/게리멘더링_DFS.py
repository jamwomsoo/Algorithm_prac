from collections import deque
from itertools import combinations
n = int(input())
people = list(map(int, input().split(' ')))
graph = [[] for _ in range(n)]
visited = [0]*(n+1)
answer = int(1e9)
for i in range(n):
    tmp = list(map(int, input().split(' ')))
    for j in range(1,tmp[0]+1):
        graph[i].append(tmp[j]-1)


def bfs(arr):
    visited = [0]*n
   
    q = deque()
    q.append(arr[0])
    visited[arr[0]] = 1
    cnt = 1
    _sum = 0
    while q:
        x = q.popleft()
        _sum += people[x]
        for g in graph[x]:
            if g in arr and visited[g] == 0:
                q.append(g)
                visited[g] = 1
                cnt+=1
                
    if cnt == len(arr):
        return _sum
    return 0
        


for i in range(1,n//2+1):
    coms = list(combinations(range(n),i))
    for com in coms:
        diff = [i for i in range(n) if i not in com]
        v1 = bfs(com)
        if not v1:
            continue
        # s1 = 0
        # for z in com:
        #     s1+=people[z]
        v2 = bfs(diff)
        if not v2:
            continue
        # s2 = 0
        # for z in diff:
        #     s2+=people[z]
        answer = min(answer, abs(v1-v2))        

if answer != int(1e9):
    print(answer)
else:
    print(-1)