n = int(input())
m = int(input())
parent = [i for i in range(1+n)]
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a
graph = [[int(1e9)]*(1+n) for _ in range(1+n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    union_parent(parent,a,b)  
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j != i:
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
max_x = [0]*101   
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == int(1e9):
            graph[i][j] = 0
    max_x[i] = max(graph[i][1:])

for i in range(1,n+1):
    find_parent(parent,i) #root가 중간에 바뀔 수 있다    

tmp = set(parent[1:]) 

ans = []
for i in tmp:
    t_ls = int(1e9)
    t = 0
    for j in range(1,n+1):
        if parent[j] == i:
            if t_ls > max_x[j]:
                t_ls = max_x[j]
                t = j
    ans.append(t)
ans.sort()
print(len(tmp))
for i in ans:
    print(i)
          