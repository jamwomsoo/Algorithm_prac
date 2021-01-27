from collections import deque
n,m = map(int,input().split())
data = []

for i in range(n):
    data.append(list(map(int,input())))
    
# visited에 0만 넣는게 아니라 0,0으로 만들어서 벽을 부수었을때의 경우를 추가한다
visited = [[[0]*2 for _ in range(m)] for _ in range(n)] 

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    q= deque()
    q.append((0,0,1))
    visited[0][0][1] = 1
    while q:
        x, y, breakPoint =  q.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][breakPoint]

        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny] == 0 and visited[nx][ny][breakPoint] == 0:
                    q.append((nx,ny,breakPoint))
                    visited[nx][ny][breakPoint] = visited[x][y][breakPoint] + 1
                # 벽이 있는 상황에서 아직 벽을 부순적이 없으면 벽을 부순다
                # BFS을 사용하게 되면 아직 벽을 부수기 전 상황에서 인접한 장소로 옮기다 벽을 만나면 각각 다른 장소에서 벽을 부순 여러 상황을 갖게 된다  
                if data[nx][ny] == 1 and breakPoint == 1:
                    q.append((nx,ny,0))
                    visited[nx][ny][0] = visited[x][y][1] + 1

    return -1
print(bfs())
