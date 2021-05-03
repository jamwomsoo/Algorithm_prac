# x축만 존재할때 x축을 각각의 n개의 행렬를 기준으로 정렬하면 n-1개의 간선이 생긴다 ex) 0-0-0-0-0
# 이렇게 n-1개의 간선만으로 최소 신장 트리를 만들 수 있다
# 결과적으로 x, y, z축에 대하여 정렬 이후 각각 n-1개의 간선만 고려해도 최적의 최소 신장 트리를 만들 수 있다
n = int(input())
graph=[]
parent = [i for i in range(n+1)]
def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
result = 0

x = []
y = []
z = []
for i in range(1,n+1):
    a,b,c = map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append(((x[i+1][0] - x[i][0]), x[i][1],x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1],y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1],z[i+1][1]))
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result+=cost
print(result)
