from collections import deque
#괴물 있 0, 없 1
n ,m =map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
steps = [0,1,2,3]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt=1
def BFS(x,y,graph):
    global cnt
    graph[x][y] = 0
    queue = deque([])
    queue.append((x,y))
    stack = 0
    while True:
        xn, yn =queue.popleft()
        if xn == n-1 and yn == m-1:
            break
        graph[xn][yn] = 0
        stack = 0
        for step in steps:
            next_x = xn + dx[step]
            next_y = yn + dy[step]
            if next_x < 0 or next_x >n-1 or next_y < 0 or next_y > m-1:
                stack+=1
                continue
            if graph[next_x][next_y] == 1:
                queue.append((next_x,next_y))
            else:
                stack+=1
        if stack == 4:
            continue
        cnt+=1
    return cnt
print(BFS(0,0,graph))