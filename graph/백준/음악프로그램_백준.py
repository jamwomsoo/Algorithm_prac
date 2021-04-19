from collections import deque
n, m = map(int, input().split())
indegree = [0 for _ in range(1+n)]
graph = [[] for _ in range(n+1)]
for i in range(m):
    tmp = list(map(int, input().split())) 
    for j in range(1,tmp[0]+1):
        if j != tmp[0]:
            graph[tmp[j]].append(tmp[j+1])
            indegree[tmp[j+1]]+=1
q = deque()

for i in range(1,n+1):
    if indegree[i] == 0: 
        q.append(i)


ans = []
while q:
    now = q.popleft()
    ans.append(now)
    for i in graph[now]:
        indegree[i]-=1
        if indegree[i] == 0:
            q.append(i)
if len(ans) != n:
    print(0)
else:
    for i in ans:
        print(i)
