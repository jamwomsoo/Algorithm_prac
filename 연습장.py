n,m,t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
total = 0
_sum = 0
for i in range(n):
    total+=sum(board[i])
print(total/(n*m))