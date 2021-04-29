import heapq
index = 1
direction = [(-1,0),(1,0),(0,1),(0,-1)]
while True:
    
    n = int(input())
    if n == 0: break
    board = [list(map(int, input().split())) for _ in range(n)]
    q = []
    distance = [[int(1e9)]*n for _ in range(n)]
    distance[0][0] = board[0][0]
    heapq.heappush(q,[board[0][0],0,0])
    while q:
        dist , x, y = heapq.heappop(q)
        if dist>distance[x][y]: continue
        if x == n-1 and y == n-1 :
            print(f'Problem {index}: {dist}')
        for dx,dy in direction:
            nx, ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                cost = dist + board[nx][ny]
                if cost< distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,[cost, nx, ny])

    index+=1
