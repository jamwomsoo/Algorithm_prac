# 시간 초과
# 백준 사이트 : https://www.acmicpc.net/problem/1937
# 참고 사이트 : https://home-body.tistory.com/665

# 알고리즘
# dfs + dp
# 각 격자를 돌면서 각 격자에 도착할 수 있는 최대 거리를 저장한다.

import sys
sys.setrecursionlimit(300000)
def dfs(i,j):
    if memo[i][j]:
        return memo[i][j]
    memo[i][j] = 1

    for a in range(4):
        ni,nj = i+di[a], j+dj[a]
        if 0<=ni<n and 0 <= nj < n and forest[i][j] < forest[ni][nj]:
            memo[i][j] = max(memo[i][j],dfs(ni,nj)+1)
    return memo[i][j]

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
memo = [[0]*n for _ in range(n)]
di = [-1,1,0,0]
dj = [0,0,-1,1]

for i in range(n):
    for j in range(n):
        memo[i][j] = dfs(i,j)

#print("map",list(map(max,memo)))
# map(max,memo) -> memo 배열의 각 열에서 max만 map한 값 중 max 값
print(max(map(max,memo)))


# 내가 푼 코드
# direction = [(-1,0),(1,0),(0,-1),(0,1)]

# n = int(input())
# memory = [[1]*n for _ in range(n)]
# board = [list(map(int, input().split())) for _ in range(n)]
# ans = 1
# def dfs(x,y,origin_x,origin_y,cnt):
#     global ans
 
#     for dx,dy in direction:
#         nx,ny = x+dx, y+dy
#         if 0<=nx<n and 0<=ny<n and board[x][y] < board[nx][ny]:
#             if memory[nx][ny] > 1:
#                 memory[origin_x][origin_y] = max(memory[nx][ny]+cnt, memory[origin_x][origin_y])
#             else:
#                 dfs(nx,ny,origin_x,origin_y,cnt+1)
#         else: 
#             memory[origin_x][origin_y] = max(memory[origin_x][origin_y],cnt)

# for row in range(n):
#     for col in range(n):
#         dfs(row,col,row,col,1)

# for row in range(n):
#     ans = max(ans,max(memory[row]))
# print(ans)