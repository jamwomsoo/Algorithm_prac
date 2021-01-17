import heapq
n = int(input())
#distance = [i for i in range(n)]
graph=[]
parent = [i for i in range(n)]
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

for i in range(n):
    x,y,z = list(map(int, input().split()))
    graph.append((x,y,z))
#print(graph)
q=[]
for i in range(n-1):
    x1,y1,z1 = graph[i] 
    for j in range(i+1,n):
        x2,y2,z2 = graph[j]
        heapq.heappush(q,(min(abs(x1-x2),abs(y1-y2),abs(z1-z2)),i,j))
#print(q)
cnt=0
result = 0
while q:
    
    cost,a,b = heapq.heappop(q)
    if find_parent(parent,a) != find_parent(parent,b):
        #print(a,b)
        union_parent(parent,a,b)
        result+=cost
        cnt+=1
    if cnt == 4:
        break    
print(result)

        