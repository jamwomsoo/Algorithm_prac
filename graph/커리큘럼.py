from collections import deque
import copy
n = int(input())
#내 풀이
# parent = [0]*(n+1)

# def find_parent(parent, x):
#   if parent[x] != x:
#     parent[x] = find_parent(parent,parent[x])
#   return parent[x]

# def union_parent(parent, a, b):
#   a = find_parent(parent, a)
#   b = find_parent(parent, b)
#   if a < b:
#     parent[b] = a
#   else:
#     parent[a] = b
# for i in range(1,n+1):
#   parent[i] = i

# indegrees=[0] *(n+1)
# times = [0] * (n+1)
# graph=[[] for _ in range(n+1)]
# indegree_graph = [[] for _ in range(n+1)]
# for i in range(1,n+1):
#   tmp = list(map(int, input().split()))
#   times[i] = tmp[0]
#   cost = 0
#   for j in range(1,len(tmp)):
#     if tmp[j] != -1:
#       graph[tmp[j]].append(i)
#       indegree_graph[i].append(tmp[j])
#       cost+=1
#       if find_parent(parent, i) != find_parent(parent, tmp[j]):
#         union_parent(parent, i, tmp[j])
#   indegrees[i] = cost

# q=deque()
# for i in range(1,n+1):
#   if indegrees[i] == 0:
#     q.append(i)

# cost = [0]*(n+1)
# while q:
#     now = q.popleft()
#     s = set(indegree_graph[now])
#     for i in s:
#         times[now]+=times[i]
#     for i in graph[now]:
#         indegrees[i]-=1
#         if indegrees[i] == 0:
#             q.append(i)

# for i in range(1,n+1):
#     print(times[i])


#해설 
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
times=[0]*(n+1)

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    times[i] = tmp[0]
    for j in tmp[1:-1]:
        graph[j].append(i)
        indegree[i]+=1    
print(graph)
result=copy.deepcopy(times)

def topplogy_sort():
    q=deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
        
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i],result[now]+times[i])
            indegree[i]-=1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])


topplogy_sort()




