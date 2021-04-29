from copy import deepcopy

direction = [(-1,0), (1,0), (0,-1), (0,1)]
def nomal_dfs(x,y,character):
    global n,nomal_cnt
    for dx,dy in direction:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and nomal[nx][ny] <0:
            if character == board[nx][ny]:
                nomal[nx][ny] = nomal_cnt
                nomal_dfs(nx,ny,character)

def diff_dfs(x,y,character):
    global n,diff_cnt
    for dx,dy in direction:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and diff[nx][ny] <0:
            if character == diff_board[nx][ny]:
                diff[nx][ny] = diff_cnt
                diff_dfs(nx,ny,character)
    

n = int(input())
board= [list(map(str, input())) for _ in range(n)]
diff_board = deepcopy(board)
for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            diff_board[i][j] = 'R'
nomal = [[-1]*n for _ in range(n)]
nomal_cnt = 0
diff = [[-1]*n for _ in range(n)]
diff_cnt = 0
for i in range(n):
    for j in range(n):
        if nomal[i][j] < 0 :
            nomal[i][j] = nomal_cnt
            nomal_dfs(i,j,board[i][j])
            nomal_cnt+=1
        if diff[i][j] < 0:
            diff[i][j] = diff_cnt 
            diff_dfs(i,j,diff_board[i][j])
            diff_cnt+=1
print(nomal_cnt,diff_cnt)
