from collections import combinations
n = int(input())
teacher=[]
space=[]
student=[]
graph =[ ]
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] == 'X':
            space.append((i,j))
        if graph[i][j] == 'T':
            teacher.append((i,j))
        if graph[i][j] == 'S':
            student.append((i,j))
data = [['']*n for _ in range(n)]
direction_ls=[1,2,3,4]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
direction = 0


def change_direction():
    global direction
    direction+=1
    if direction > 3:
        direction = 0

def sight(data,x,y):
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0>nx or nx>=n or ny<0 or ny>=n:
        return
    if data[nx][ny] == 'O' or data[nx][ny] == 'T':
        return
    #if data[nx][ny] == 'X':
    data[nx][ny] = 'T'
    sight(data,nx,ny)
jugde = False
coms = combinations(space,3)

def solution(cnt):
    for i in range(n):
         for j in range(n):
            data[i][j] = graph[i][j]
    for com in com:
        

        
            
            
# def dfs(cnt):
#     global jugde
    
#     s_num=0    
#     if cnt==0:
#         for i in range(n):
#             for j in range(n):
#                 data[i][j] = graph[i][j]
#                 if graph[i][j] == "S":
#                     s_num+=1
#         if s_num == 0:
#             return
#         for i in range(n):
#             for j in range(n):
#                 if graph[i][j] == 'T':
#                     for d in range(4):
#                         change_direction()
#                         sight(data,i,j)
#         for i in range(n):
#             for j in range(n):
#                 if data[i][j] == "S":
#                     s_num-=1
#         if s_num == 0:
#             jugde = True
#         return 
#     else:
#         for i in range(n):
#             for j in range(n):
#                 if graph[i][j] == 'X':
#                     #print(x,y, end = " ")
#                     graph[i][j] = 'O'
#                     dfs(cnt-1)
#                     graph[i][j] = 'X'
    

dfs(3)    
if jugde == True:
    print("YES")
else:
    print("NO")
