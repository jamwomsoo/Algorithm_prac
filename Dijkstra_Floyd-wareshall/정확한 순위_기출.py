# 학생수, 성적 비교 횟수
n,m = map(int, input().split())

graph=[[int(1e9)]*(n+1) for _ in range(n+1)]


for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i != j:
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            else:
                graph[i][j] = 0
result = 0
for i in range(1,n+1):
    cnt=0
    for j in range(1, n+1):
        if graph[i][j] != int(1e9) or graph[j][i] != int(1e9):
            cnt+=1
    if cnt == n:
        result+=1
print(result)



# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if graph[i][j] == int(1e9):
#             graph[i][j] = 0
#         print(graph[i][j], end=" ")
#     print()
# #print
# value = [0]*(n+1)
# for i in range(1,n+1):
#     cnt=0
#     for j in range(1,n+1):
#         if graph[i][j] != 0:
#             cnt+=1
#     value[i]+=cnt 
# for j in range(1,n+1):
#     cnt=0
#     for i in range(1,n+1):
#         if graph[i][j] != 0:
#             cnt+=1
#     value[j]+=cnt
# print(value)
# result=0
# for i in range(len(value)):
#     if value[i] == n-1:
#         result+=1

print(result)


# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
