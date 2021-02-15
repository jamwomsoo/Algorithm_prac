cdx = [0, 1, 0, -1]
cdy = [1, 0, -1, 0]
udx = [0, -1, 0, 1]
udy = [1, 0, -1, 0]
r,c,t = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(r)]
conditioner = []
for x in range(r):
    for y in range(c):
        if board[x][y] ==-1:
            conditioner.append((x,y))
conditioner.sort()


def move_dust():
    global c,r
    new_board = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                original = board[x][y]
                move_direct = 0
                for i in range(4):
                    nx, ny = x + cdx[i], y + cdy[i]
                    if (0<=nx<r and 0<=ny<c) and board[nx][ny] != -1:
                        new_board[nx][ny]+=original//5
                        move_direct+=1
                board[x][y] -= (original//5) * move_direct
    for x in range(r):
        for y in range(c):
            board[x][y]+=new_board[x][y]
def move_wind():
    global c,r
    for i in range(2):
        x,y = conditioner[i]
        prev = 0
        nxt = 0
        if i == 0:
            x+=udx[0]
            y+=udy[0]
            for j in range(4):
                while True:
                    if board[x][y] == -1:
                            break
                    if 0 <= x+udx[j] < r and 0 <= y+udy[j] < c:
                        nx,ny = x+udx[j], y+udy[j]                        

                        prev,board[x][y] = board[x][y],prev
                                       
                        x,y = nx,ny
                    else:
                        break
        else:
            x+=cdx[0]
            y+=cdy[0]
            for j in range(4):
                while True:
                    if board[x][y] == -1:
                            break
                    if 0 <= x+cdx[j] < r and 0 <= y+cdy[j] < c:
                        nx,ny = x+cdx[j], y+cdy[j]
                        prev,board[x][y] = board[x][y],prev
                        x,y = nx,ny
                    else:
                        break
                    
while t>0:
    t-=1
    move_dust()
    move_wind()
total = 0
for x in range(r):
    for y in range(c):
        if board[x][y] >0:
            total+=board[x][y]
print(total)



        

                    
