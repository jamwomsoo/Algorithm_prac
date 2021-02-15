import sys
import heapq
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


r,c,m = map(int, input().split())
if m == 0:
    print(0)
    sys.exit()
board = [[[] for _ in range(c)] for _ in range(r)]

for _ in range(m):
    x,y,s,d,z = map(int, input().split())
    board[x-1][y-1].append([z,s,d-1])
start = 0
total = 0



def one_shark_move(x,y):
    
    size , cnt, direction = board[x][y][0]
    while cnt>0:
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        if not (0<=nx<r and 0<=ny<c):
            nx = x - dx[direction]
            ny = y - dy[direction]
            if direction ==0 or direction == 2:
                direction+=1
            else:
                direction-=1
        x,y = nx,ny
        cnt-=1
    return x,y,direction
def remain_one():
    for x in range(r):
        for y in range(c):
            if len(board[x][y])>1:
                while True:
                    heapq.heappop(board[x][y])
                    if len(board[x][y]) == 1:
                        break


def all_shark_move():
    global board
    new_board =  [[[] for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):  
            if board[x][y]:
                nx,ny,direct = one_shark_move(x,y)
                size , speed ,d = board[x][y][0]
                #print(f"({x},{y}) ({nx},{ny})")
                heapq.heappush(new_board[nx][ny],[size,speed,direct])
              
    board = new_board
    
for i in range(c):
    # for x in range(r):
    #     for y in range(c):
    #         print(board[x][y], end = " ")
    #     print()
    # print()
    for j in range(r):
        if board[j][i]:
            total+=board[j][i][0][0]
            board[j][i] = []
            break
    
    all_shark_move()
    remain_one()
    

print(total)
