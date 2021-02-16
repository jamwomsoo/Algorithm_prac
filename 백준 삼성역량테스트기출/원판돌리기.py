dx = [0,-1, 0, 1]
dy = [1,0, -1, 0]

n,m,t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
total=0
cnt = n*m
for i in range(n):
    total +=sum(board[i])


for _ in range(t):
    _sum = 0
    
    x,d,k =map(int, input().split())
    for i in range(n):
        if (i+1) % x == 0:
            for _ in range(k):
                if d == 0: # 시계
                    tmp = board[i][-1]
                    for j in range(m-1,0,-1):
                        board[i][j]=board[i][j-1]
                    board[i][0] = tmp

                else: #반시계
                    tmp = board[i][0]
                    for j in range(0,m-1):
                        board[i][j] = board[i][j+1]
                    board[i][-1] = tmp
 
    flag = False
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                continue
            for d in range(4):
                ni = i+dx[d]
                nj = j+dy[d]
                if (nj==-1 or nj==m) and 0<=ni<n:
                    if nj==-1:
                        nj = m-1
                    else:
                        nj = 0
                if 0<=ni<n and 0<=nj<m:
                    if board[i][j] == board[ni][nj]:
                        
                        _sum +=(board[i][j]+board[ni][nj])
                        board[i][j] = board[ni][nj] = -1
                        cnt -=2
                        flag = True
                        break
                

   
    if flag:
        total -= _sum
    else:
        tmp = total/cnt
        for x in range(n):
            for y in range(m):
                if board[x][y] == -1:
                    continue
                if board[x][y] < tmp:
                    board[x][y]+=1
                elif board[x][y] > tmp:
                    board[x][y]-=1 

    for x in range(n):
        for y in range(m):
            print(board[x][y], end = " ")
        print()
    print()

print(total)