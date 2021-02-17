# 쌓는게 문제인듯
from collections import deque
dx = [0,1]
dy = [1,0]
ndx = [-1,1,0,0]
ndy = [0,0,-1,1]
result = 0
total=0
n = int(input())
board = [[0]*10 for _ in range(4)]
for _ in range(6):
    board.append([0 for _ in range(4)] )

def build_block(block,direction,t,number):
    global n,board,total
    x,y = block
    q = deque()
    if t == 1:
        q.append((x,y))
    if t ==2 :
        q.append((x,y,x,y-1))
    if t == 3:
        q.append((x,y,x-1,y))
    re_x =re_y =x,y
    if direction == 0:
        n = len(board[0])
    else:
        n = len(board)
    while q:
        if t == 1:
            x,y =q.popleft()
            nx,ny = x+dx[direction],y+dy[direction]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                q.append((nx,ny))
                now_x,now_y = nx,ny
        else:
            x,y,x2,y2 = q.popleft()
            nx1,nx2,ny1,ny2 = x+dx[direction],x2+dx[direction],y+dy[direction],y2+dy[direction]
            if 0<=nx1<n and 0<=ny1<n and board[nx1][ny1] == 0 and 0<=nx2<n and 0<=ny2<n and board[nx2][ny2] == 0:
                q.append((nx1,ny1,nx2,ny2))
                now_x,now_y = nx1,ny1
    board[now_x][now_y] = number
    total+=1
    if t == 2:
        board[now_x][now_y-1] = number
        total+=1
    elif t == 3:
        board[now_x-1][now_y] = number
        total+=1

def check_four(i,t) :
    global result,board,total
    if i == 0:
        for y in range(len(board[0])-1,4-1,-1):
            flag = True            
            for x in range(4):
                if board[x][y] == 0:
                    flag = False
                    break
            if flag:
                for x in range(4):
                    if board[x][y] !=0:
                        total-=1
                    board[x][y] = 0
                result+=1

                for k in range(4):
                    board[k][4:y+1] = board[k][4:y]
                    board[k][4] = 0
                # 그 전것이 있는 지확인
                #move_all_down(i,y-1)
                y+=1
    else:
        for x in range(len(board)-1,4-1,-1):
            flag = True            
            for y in range(4):
                if board[x][y] == 0:
                    flag = False
                    break
            if flag:
                for y in range(4):
                    if board[x][y] !=0:
                        total-=1
                    board[x][y] = 0
                result+=1
                for k in range(x,4,-1):
                    board[k] = board[k-1]
                for k in range(4):
                    board[4][k] = 0    
                
                x+=1

def check_light(i):
    global board,number,total
    if i == 0:
        flag4 = False
        flag5 = False
        for y in range(4,6):
            for x in range(4):
                if y == 4 and board[x][y] !=0:
                    flag4 = True
                    break
                if y == 5 and board[x][y] !=0:
                    flag5 = True
                    break
            if flag4:
                break
        if flag4:
            for x in range(4):
                for y in range(8,10):
                    if board[x][y] != 0:
                        total-=1
                tmp = [0,0]+board[x][:-2]
                #print(tmp)
                board[x] = tmp
                
        if flag5:
            for x in range(4):
                for y in range(9,10):
                    if board[x][y] != 0:
                        total-=1
                tmp = [0]+board[x][:-1]
       
                board[x] = tmp      
    else:
        flag4 = False
        flag5 = False
        for x in range(4,6):
            for y in range(4):
                if x == 4 and board[x][y] !=0:
                    flag4 = True
                    break
                if x == 5 and board[x][y] !=0:
                    flag5 = True
                    break
            if flag4:
                break            
        if flag4:
            for x in range(9,5,-1):
                for y in range(4):
                    if board[x][y] !=0:
                        total-=1
                board[x] = board[x-2]
            for x in range(4,6):
                board[x] =[0,0,0,0]
        if flag5:
            for x in range(9,5,-1):
                for y in range(4):
                    if board[x][y] !=0:
                        total-=1
                board[x]=board[x-1]
            for x in range(5,6):
                board[x] =[0,0,0,0]
for number in range(n):
    t,x,y = map(int, input().split())
    block=[x,y]
    if t == 2:
        block=[x,y+1]
    elif t== 3:
        block=[x+1,y]
    for i in range(2): # 0은 파랑 1은 초록
        build_block(block,i,t,number+1)    
        check_four(i,t)
        check_light(i)
print(result)    
print(total)
    
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end = " ")
    print()
        
