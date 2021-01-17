n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
travel = list(map(int, input().split()))#나중에 1씩 빼서 계산
parent = [i for i in range(0,n+1) ]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] =a
    else:
        parent[a] = b
for i in range(1,n):
    for j in range(i+1,n+1):
        if graph[i-1][j-1] == 1:
            union_parent(parent,i,j)
check = True
a=travel[0]
for i in travel:
    if  find_parent(parent,a) != find_parent(parent,i):
        print("NO")
        check=False
        break        
if check == True:     
    print("YES")
# if parent.count(max(parent)) == n:
#     print("YES")
# else:
#     print("NO")