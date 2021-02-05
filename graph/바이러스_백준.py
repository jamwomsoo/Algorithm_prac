n = int(input())
m = int(input())
parent = [i for i in range(101)]

def find_parent(parent, x):
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

for i in range(m):
    a,b = map(int, input().split())
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)

for i in range(1,n+1):
    find_parent(parent,i)
print(parent.count(parent[1])-1)