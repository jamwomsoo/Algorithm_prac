from collections import deque
n = int(input())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
arr = []
now_x , now_y = 0,0
now_size = 2

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 9:
            now_x = i
            now_y = j
            arr[i][j] = 0
def bfs():
    dis=[[-1]*n for _ in range(n)]
    q = deque()
    q.append((now_x,now_y))
    dis[now_x][now_y] =0 
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]<=now_size and dis[nx][ny] == -1:
                dis[nx][ny] = dis[x][y]+1
                q.append((nx, ny))
    return dis
def find(dis):
    x,y = 0,0
    min_dist = int(1e9)
    for i in range(n):
        for j in range(n):
            if dis[i][j] != -1 and 0< arr[i][j] < now_size:
                if min_dist > dis[i][j]:
                    min_dist = dis[i][j]
                    x,y=i,j
    if min_dist == int(1e9):
        return None
    return x,y,min_dist
result = 0
ate = 0
while True:
    value = find(bfs())
    if  value == None:
        print(result)
        break
    now_x = value[0]
    now_y = value[1]
    result+=value[2]
    arr[now_x][now_y] = 0
    ate +=1
    if ate >=now_size:
        now_size+=1
        ate = 0

    


    

        

