import heapq

direction = [(-1,0), (1,0), (0,1), (0,-1)]
n = int(input())
board = [list(map(int, input())) for _ in range(n)]

q=[]
heapq.heappush(q,[0,0,0])
visited = [[False]*n for _ in range(n)]
visited[0][0] = True
distance  = [[int(1e9)]*n for _ in range(n)]
distance[0][0] = 0
while q:
    _break, x, y = heapq.heappop(q)
  
    if x == n-1 and y == n-1:
        print(_break)
        break
    for dx,dy in direction:
        nx,ny = x+dx,y+dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and visited[nx][ny] == False:
            heapq.heappush(q,[_break,nx,ny])
            visited[nx][ny] = True
            
        elif 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and visited[nx][ny] == False:    
            heapq.heappush(q,[_break+1,nx,ny])
            visited[nx][ny] = True



