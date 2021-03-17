def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x] 
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: parent[b] = a
    else: parent[a] = b
def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
    

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if computers[i][j] == 0: computers[i][j] = int(1e9)
                if computers[i][j] == int(1e9):
                    computers[i][j] = min(computers[i][j], computers[i][k]+computers[k][j])
    #print(computers)
    for i in range(n):
        for j in range(n):
            if computers[i][j] != int(1e9):
                if find_parent(parent,i) != find_parent(parent,j):
                    union_parent(parent,i,j)
    _s = set(parent)
    answer = len(_s)
                
    return answer
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# 다른 사람 코드
# 방문 리스트를 만들어서 방문 리스트가 0이면 dfs로 연결된 네트워크 까지 방문해봄
# 한 번 방문 리스트에 방문할때마다 다른 네트워크이므로 네트워크 하나씩 추가
# def solution(n, computers):
#     answer = 0
#     visited = [0 for i in range(n)]
#     def dfs(computers, visited, start):
#         stack = [start]
#         while stack:
#             j = stack.pop()
#             if visited[j] == 0:
#                 visited[j] = 1
#             # for i in range(len(computers)-1, -1, -1):
#             for i in range(0, len(computers)):
#                 if computers[j][i] ==1 and visited[i] == 0:
#                     stack.append(i)
#     i=0
#     while 0 in visited:
#         if visited[i] ==0:
#             dfs(computers, visited, i)
#             answer +=1
#         i+=1
#     return answer