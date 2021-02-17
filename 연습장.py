# 밝은 색 있는 거 삭제 까지 가능한 코드
from collections import deque
from copy import deepcopy
dx = [0,1]
dy = [1,0]
ndx = [-1,1,0,0]
ndy = [0,0,-1,1]
result = 0
n = int(input())
board = [[0]*10 for _ in range(4)]
#tNum = deepcopy(board)
for _ in range(6):
    board.append([0 for _ in range(4)] )

def build_block(block,direction,t,number):
    global n,board
    x,y = block
    q = deque()
    q.append((x,y))
    re_x =re_y =x,y
    if direction == 0:
        n = len(board[0])
    else:
        n = len(board)
    while q:
        x,y =q.popleft()
        nx,ny = x+dx[direction],y+dy[direction]
        if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
            q.append((nx,ny))
            now_x,now_y = nx,ny
    
    board[now_x][now_y] = number
    if t == 2:
        board[now_x][now_y-1] = number
    elif t == 3:
        board[now_x-1][now_y] = number
# def move_all_down(i,y):
#     for x in range(4):

def check_four(i,t) :
    
    global result,board
    # 0은 파랑, 1은 초록
    # 0이면 열이 4개인게 있으면 +1
    # 1이면 행이 4개인게 있으면 +1
    # 박살 낸 후:
    # t 가 2,3일때 주위에 같은 숫자없으면 혼자 이동
    # 있으면 옆에 꺼랑 같이 이동  
    
    if i == 0:
        for y in range(len(board[0])-1,4-1,-1):
            flag = True            
            for x in range(4):
                if board[x][y] == 0:
                    flag = False
                    break
            if flag:
                for x in range(4):
                    board[x][y] = 0
                result+=1
                # 그 전것이 있는 지확인
                #move_all_down(i,y-1)
                #y+=1

    else:
        for x in range(len(board)-1,4-1,-1):
            flag = True            
            for y in range(4):
                if board[x][y] == 0:
                    flag = False
                    break
            if flag:
                for y in range(4):
                    board[x][y] = 0
                result+=1
        
def check_light(i):
    global board,number
    # 0은 파랑, 1은 초록
    # 0이면 4,5열에 있는게 있으면 각각(1개씩) 맨마지막 파괴(4에 있으면 2번, 5에 있으면 1번)
    # 1이면 4,5행에 있는게 있으면 각각(1개씩) 맨마지막 파괴
    flag4 = False
    flag5 = False
    for y in range(4,6):
        for x in range(4):
            if i == 1:
                x,y = y,x
                if x == 4 and board[x][y] !=0:
                    flag4 = True
                    break
                if x == 5 and board[x][y] !=0:
                    flag5 = True
                    break
                continue
            if y == 4 and board[x][y] !=0:
                flag4 = True
                break
            if y == 5 and board[x][y] !=0:
                flag5 = True
                break
        if flag4:
            break
    if i == 0:
        print(number,flag4,flag5)
        if flag4:
            for x in range(4):
                board[x][4:10] = board[x][2:8]
        if flag5:
            for x in range(4):
                board[x][5:10]=board[x][4:9]
    else:
                    
        if flag4:
            for x in range(9,3,-1):
                board[x] = board[x-2]
        if flag5:
            for x in range(9,4,-1):
                board[x]=board[x-1]

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
    
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end = " ")
    print()
        
        