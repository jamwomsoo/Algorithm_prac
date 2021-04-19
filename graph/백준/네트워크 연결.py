import heapq
n = int(input())
m = int(input())
q = []
parent = [i for i in range(n+1)]
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent, a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b 
ans = 0
for i in range(m):
    a,b,c = map(int, input().split())
    heapq.heappush(q,[c,a,b])
while q:
    cost, a,b = heapq.heappop(q)
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans+=cost
print(ans)
