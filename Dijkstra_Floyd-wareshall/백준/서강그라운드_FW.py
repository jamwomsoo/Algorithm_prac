n,m,r = map(int, input().split())
item = list(map(int, input().split()))
board = [[int(1e9)]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j: 
            board[i][j] = 0
for i in range(r):
    a,b,l = map(int ,input().split())
    board[a-1][b-1] = l
    board[b-1][a-1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                board[i][j] = min(board[i][j],board[i][k]+board[k][j])

answer = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        if board[i][j] <=m:
            
            tmp+=item[j]
    answer = max(answer,tmp)
print(answer)