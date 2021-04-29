import math
from itertools import combinations
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b : parent[a] = parent[b]
    else: parent[b] = parent[a]
def cal_distance(a,b):
    
    return math.sqrt(pow(a[0]-b[0],2) + pow(a[1]-b[1],2))    
n,m = map(int, input().split())
arr= [[0,0]]
parent = [i for i in range(n+1)]

for _ in range(n):
    x,y = map(int, input().split())
    arr.append([x,y])
ans = 0

for _ in range(m):
    a,b= map(int, input().split())
    union_parent(parent,a,b)
    
distance = []

coms = list(combinations([i for i in range(1,n+1)],2))
for com in coms:
    a,b = com
    tmp = cal_distance(arr[a],arr[b])
    distance.append([tmp,a,b])
distance.sort()
for tmp,a,b in distance:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans+=tmp
        
print("%0.2f"%ans)