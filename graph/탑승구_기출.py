def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
g = int(input())
p = int(input())

parent = [i for i in range(g+1)]

cnt= 0

for i in range(p):
    information = int(input())
    if find_parent(parent, information) == 0:
        break
    else:
        union_parent(parent,information,information-1)
        cnt+=1
print(cnt)
