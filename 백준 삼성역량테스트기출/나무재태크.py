#틀
from collections import deque
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

n,m,k = map(int,input().split())
tree_ls = [[[] for _ in range(n)] for _ in range(n)] #나무당 나이
nutri = [list(map(int,input().split())) for _ in range(n)] # 매년 공급되는 영양분
board = [[5]*n for _ in range(n)] # 현재 땅에 존재하는 영양분

for i in range(m):
    x,y,z = map(int, input().split())
    tree_ls[x-1][y-1].append(z)



for _ in range(k):

    
    # 봄
    for x in range(n):
        for y in range(n):
            live_trees = []
            death_trees = 0
            if tree_ls[x][y]:
                tree_ls[x][y].sort()
                for tree in tree_ls[x][y]:
                    if board[x][y] >= tree:
                        board[x][y]-=tree
                        live_trees.append(tree+1)
                    else:
                        death_trees+=tree//2
            tree_ls[x][y] = live_trees
            # 여름  
            board[x][y]+=death_trees
    
    if not tree_ls:
       print(0)
       sys.exit()

    # 가을
    
    for x in range(n):
        for y in range(n):
            if tree_ls[x][y]:
                for tree in tree_ls[x][y]:
                    if tree %5 ==0:
                        for i in range(8):
                            nx, ny = x + dx[i], y + dy[i]
                            if 0<=nx<n and 0<=ny<n:
                                tree_ls[nx][ny].append(1)
    
    #겨울
    for i in range(n):
        for j in range(n):
            board[i][j]+=nutri[i][j]
 

total=0
for x in range(n):
    for y in range(n):
        total+=len(tree_ls[x][y])
print(total)
    