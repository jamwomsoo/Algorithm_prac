import heapq
v, e = map(int, input().split())
q = []
parent = [i for i in range(v+1)]
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(e):
    a, b, value = map(int, input().split())
    heapq.heappush(q,[value,a,b])
ans = 0
while q:
    v, a, b = heapq.heappop(q)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans+=v
print(ans)