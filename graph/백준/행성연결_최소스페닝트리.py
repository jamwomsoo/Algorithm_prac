import heapq
from typing import AnyStr
n = int(input())
board = [list(map(int ,input().split())) for _ in range(n)]
q = []
parent = [i for i in range(n+1)]
for i in range(n):
    for j in range(i+1,n):
        heapq.heappush(q,[board[i][j], i, j])
def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a
answer = 0
while q:
    cost,a,b = heapq.heappop(q)
    if find(parent, a) != find(parent, b):
        union(parent,a,b)
        answer+=cost
print(answer)