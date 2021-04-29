n = int(input())
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
while True:
    a,b = map(int, input().split())
    if a == -1 and b == -1 :
        break
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i != j:
               
                graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])
ans = []
for i in range(1,n+1):
    tmp = -int(1e9)
    for j in range(1,n+1):
        if graph[i][j] != int(1e9):
            tmp=max(tmp,graph[i][j])
    if tmp != -int(1e9):
        ans.append([tmp,i])
ans.sort()

low = ans[0][0]
cnt = 0
result = []
for s,n in ans:
    if low == s:
        result.append(n)
print(low, len(result))
print(*result)
