n, m = map(int,input().split())
#graph=[[] for _ in range(n)]
ls = []

parent=[i for i in range(n)]

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]= a
    else:
        parent[a] = b


for i in range(m):
    a,b,c = map(int,input().split())
    #graph[a].append((b,c))
    ls.append((c,a,b))
ls.sort()
print(ls)
result= 0
holl=0
for i in ls:
    c,a,b = i
    holl += c
    if find_parent(parent,a) !=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=c
print(holl - result)
