# 말이 되고픈 원숭이
# https://www.acmicpc.net/problem/1600
# 어렵네... 벽부수고 가기랑 비슷한유형
# K가 남아있으면 말처럼 이동하기 + 원숭이 처럼 이동하기 둘다 큐에 쌓는다
# K가 없으면 원숭이 걸음으로만 큐에 쌓는다
# -> 큐에는 board를 이동하지만 말걸음과 원숭이 걸음이 섞여있어서 말 걸음(8케이스)를 다 포함하여 맨 오른쪽으로 최단 걸음을 구할 수 있다
# cost는 3차원이므로 
 

from collections import deque
direction = [(-1,0),(1,0),(0,-1),(0,1)]
horse_direction = [(-2,-1), (-1,-2), (-2,1), (-1,2), (2,-1), (1,-2), (2,1), (1,2)]

k = int(input())
w,h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
cost = [[[-1]*(k+1) for _ in range(w)] for _ in range(h)]

q = deque()
q.append([0,0,k])
cost[0][0][k] = 0
while q:
    x,y,c = q.popleft()
    if x == h-1 and y==w-1:
        print(cost[h-1][w-1][c])
        #print(cost)
        exit()
    for dx,dy in direction:
        nx,ny = x+dx,y+dy
        if 0<= nx < h and 0<= ny < w and board[nx][ny]==0 and cost[nx][ny][c] <0:
            q.append([nx,ny,c])
            cost[nx][ny][c] = cost[x][y][c] + 1

    if c>0:
        for dx,dy in horse_direction:
            nx,ny = x+dx,y+dy
            if 0<= nx < h and 0<= ny < w and board[nx][ny]==0 and cost[nx][ny][c-1] <0:
                q.append([nx,ny,c-1])
                cost[nx][ny][c-1] = cost[x][y][c] + 1

print(-1)