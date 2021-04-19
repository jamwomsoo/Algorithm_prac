v,e = map(int, input().split())
graph = [[int(1e9)]*(v+1) for _ in range(v+1)]

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a][b] = c
for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
# 가장 작은 사이클을 찾는 for문
_min = int(1e9)
for i in range(1,v+1):
    _min = min(_min,graph[i][i])
if _min == int(1e9):
    print(-1)
else:
    print(_min)