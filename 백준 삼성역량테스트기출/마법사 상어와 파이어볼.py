from collections import deque
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
total_w = 0
n,m,k = map(int, input().split())
board = [[deque() for _ in range(n)] for _ in range(n)]
for i in range(m):
    r,c,w,s,d = map(int, input().split())
    board[r-1][c-1].append([w,s,d])
    total_w+=w

def print_arr():
    for i in range(n):
        for j in range(n):
            print(board[i][j],end = ' ')
        print()

for i in range(k):
    # 파이어볼의 이동
    if total_w <=0:
        break 
    new_board = [[deque() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                length = len(board[i][j])
                for _ in range(length):
                    weight, speed, direction = board[i][j].popleft()

                    nx,ny = i+dx[direction]*speed,j+dy[direction]*speed
                    #if (0<=nx<n and not 0<=ny<n) or (not 0<=nx<n and 0<=ny<n):
                    if nx  <= -1:
                        nx = (n - ((-nx)%n))%n
                    elif nx >= n:
                        nx = nx%n
                    if ny <= -1:
                        ny = (n - ((-ny)%n))%n
                    elif ny >= n:
                        ny = ny%n
                    #else:

                    
                    new_board[nx][ny].append([weight,speed,direction])
    board = new_board
    #print_arr()
    # 한 칸에 여러개의 파이어볼 있으면
    
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:
                weight_sum = speed_sum = 0
                length = len(board[i][j])
                flag_odd = True
                flag = True
                if board[i][j][0][2] % 2 == 0:    
                    flag_odd = False
                
                for index in range(length):
                    weight_sum+=board[i][j][index][0]
                    speed_sum+=board[i][j][index][1]
                    if flag_odd : # 처음 홀수
                        if board[i][j][index][2] % 2 == 0: # 나중 순번부터 짝수나오면  
                            flag = False   # 1357
                    elif not flag_odd:         # 처음 짝수
                        if board[i][j][index][2] % 2 == 1: # 나중 순번부터 홀수나오면
                            flag = False   # 1357
                if flag:
                    d = 0
                else:
                    d = 1
                total_w -= weight_sum
                tmp,weight,speed = deque(), weight_sum//5, speed_sum//length
                if weight <= 0:
                    board[i][j] = deque()
                    continue
                total_w+=weight*4
                for _ in range(4):
                    tmp.append([weight,speed,d])
                    d+=2
                    
                board[i][j] = tmp
    #print_arr()
print(total_w)