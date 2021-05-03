import math
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: 
        parent[b] = a
    else:
     
        parent[a] = b


origin = []
n = int(input())
for i in range(n):
    a, b = map(float, input().split())

    origin.append([a,b])

parent= [i for i in range(n)]
edges = []

for i in range(n-1):
    for j in range(i+1,n):
        tmp = math.sqrt((origin[i][0]-origin[j][0])**2 + (origin[i][1]-origin[j][1])**2)
        edges.append([tmp,i,j])
edges.sort()
ans = 0
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans += cost
print('%0.2f'%ans)