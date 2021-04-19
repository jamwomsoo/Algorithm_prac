# 플로이드 와샬을 역으로 이용하는 문제
# 몰랐음 -> 틀림
import sys
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
origin = [[1]*n for _ in range(n)]
ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if j == i or i == k or j==k: continue
            if board[i][j] == board[i][k]+board[k][j]:
                origin[i][j] = 0
            elif board[i][j] > board[i][k]+board[k][j]:
                ans = -1 
if ans == -1:
    print(-1)
    sys.exit()
for i in range(n):
    for j in range(n):
        if origin[i][j] == 1:
            ans+=board[i][j]
        
print(ans//2)