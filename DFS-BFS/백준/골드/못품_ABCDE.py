# 

import sys

n, m = map(int, input().split())
arr = [[] for i in range(n)]
visited = [False]*n
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(index,num):
    if num>= 4:
        print(1)
        sys.exit()

    for i in arr[index]:
        if not visited[i]:
            visited[i] = True
            dfs(i, num+1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i,0)
    visited[i] =False

print(0)