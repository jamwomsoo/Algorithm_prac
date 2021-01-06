#n 집의 개수, m 길의 개수
n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
edges = []
for i in range(m):
    a, b, fee = map(int, input().split())
    edges.append((fee,a,b))

edges.sort()
print(edges)
result_cost=[]
cost = 0
for edge in edges:
    fee, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost += fee
        result_cost.append(fee)

print(cost - max(result_cost))


#해답 풀이
# last = 0
# result = 0
# for  edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#         last = cost 
# print(result - cost)