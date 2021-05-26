n, m =map(int, input().split())
board = [[[int(1e9),0]]*(n+1) for _ in range(n+1)]



for i in range(m):
    a,b,cost = map(int ,input().split())
    
    board[a][b] = [cost,b]
    board[b][a] = [cost,a]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            board[i][j] = [0,0]

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i != j:
                #print(board[i][j][0] , board[i][k][0]+board[k][j][0])
                if board[i][j][0] > board[i][k][0]+board[k][j][0]:
                    board[i][j] = [board[i][k][0]+board[k][j][0], board[i][k][1]]
ans = [[int(1e9)]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('-',end = ' ')
        else:
            print(board[i][j][1],end = ' ')
    print()