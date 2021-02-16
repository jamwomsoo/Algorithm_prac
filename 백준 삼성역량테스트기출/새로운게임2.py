import sys
dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
horse = []
arr = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    x,y,d = map(int,input().split())
    horse.append([x-1,y-1,d-1])
    arr[x-1][y-1].append(i)

time = 0

while True:
    if time>1000:
                print(-1)
                break
    for x in range(n):
        for y in range(n):
            if len(arr[x][y])>=4:
                print(time)
                sys.exit()
    for i in range(k):
        x,y,d = horse[i]
        find_index = arr[x][y].index(i)
        nx,ny = x+dx[d],y+dy[d]
        if not (0<=nx<n and 0<=ny<n) or board[nx][ny] == 2: # 만약 모서리거나 파란색
            # 방향을 반대로
            if d==0: 
                d = 1
            elif d==1: 
                d = 0
            elif d==2: 
                d = 3
            elif d==3: 
                d = 2 
            horse[i][2] = d 
            nx,ny = x+dx[d],y+dy[d]
        if not (0<=nx<n and 0<=ny<n) or board[nx][ny] == 2:
            continue
        if board[nx][ny] == 0:
            tmp = arr[x][y][find_index:]
            for index in tmp:
                horse[index] = [nx,ny,horse[index][2]]
            arr[nx][ny].extend(tmp)
            arr[x][y] = arr[x][y][:find_index]
            
            if len(arr[nx][ny]) >=4:
                print(time+1)
                sys.exit()

        elif board[nx][ny] == 1:
            tmp = arr[x][y][find_index:]
            tmp.reverse()
            for index in tmp:
                horse[index] = [nx,ny,horse[index][2]]
            arr[nx][ny].extend(tmp)
            arr[x][y] = arr[x][y][:find_index]
            if len(arr[nx][ny]) >=4:
                print(time+1)
                sys.exit()
    time+=1