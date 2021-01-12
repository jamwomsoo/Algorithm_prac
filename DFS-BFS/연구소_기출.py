#해설지 풀이
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
tmp = [[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
result = 0
def virus(x,y):
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if nx>=0 and nx<n and ny>= 0 and ny<m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx,ny)
def get_score():
    _zero = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                _zero+=1
    return _zero
    

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]
        for x in range(n):
            for y in range(m):
                if graph[x][y] == 2:
                    virus(x,y)
        result = max(result,get_score())
        return 
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j]=1
                count+=1
                dfs(count)
                graph[i][j]=0
                count-=1
    return result
print(dfs(0))

#내 풀이_오답
# from itertools import combinations
# from collections import deque
# from copy import deepcopy
# n,m = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]
# vistied =[[False]*m for i in range(n)]
# arr = []
# birus=[]
# wall = []
# for i in range(n):
#     for j in range(m):
#         arr.append((i,j))
#         if graph[i][j] == 2:
#             birus.append((i,j))
#         if graph[i][j] == 1:
#             wall.append((i,j))

# coms = list(combinations(arr,3))

# print(len(coms))
# #coms = [((1, 0), (1, 5), (2, 0))]
# z=0
# d=[1,2,3,4]
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# q=deque()
# cx=0
# cy = 0
# cz = 0
# large=0

# for com in coms:
#     g = deepcopy(graph)
#     #조합 중 하나 선택해서 3개 빈공간에 기둥 세우기
#     check = False
#     for x,y in com:
#         if g[x][y] == 0:
#             g[x][y]=1
#     while birus:
#         q.append(birus.pop())
#         while q:
#             x,y = q.popleft()
#             if g[x][y]:
#                 continue
#             g[x][y] = 2
#             for i in range(4):  
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx<0 or ny < 0 or nx>=n or ny >=m:
#                     continue
#                 if g[nx][ny] == 0:
#                     q.append((nx,ny))         
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if g[i][j] == 0:
#                 cnt+=1   
#     if cnt > large:
#         print(cnt)
#         large = cnt
#         cx,cy,cz = com
# print(large,cx,cy,cz)
