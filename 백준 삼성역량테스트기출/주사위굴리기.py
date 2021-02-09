n, m, x, y,k  = map(int, input().split())
arr = []
dice= [[0]*3 for _ in range(4)]
def turn_right(dic): # 동
    dic[1][0],dic[1][1],dic[1][2],dic[3][1] = dic[3][1], dic[1][0],dic[1][1],dic[1][2]
    return dic
def turn_left(dic): # 서
    dic[1][0],dic[1][1],dic[1][2],dic[3][1] = dic[1][1],dic[1][2],dic[3][1],dic[1][0]
    return dic
def turn_up(dic): # 북
    dic[0][1],dic[1][1],dic[2][1],dic[3][1] = dic[1][1],dic[2][1],dic[3][1],dic[0][1] 
    return dic
def turn_down(dic): # 남
    dic[0][1],dic[1][1],dic[2][1],dic[3][1] = dic[3][1],dic[0][1],dic[1][1],dic[2][1] 
    return dic
for i in range(n):
    arr.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
dx = [0, 0, -1,1]
dy = [1,-1,0,0]
for order in orders:
    #print(x,y)
    if 0 > x+dx[order-1] or x+dx[order-1]>=n or 0 > y+dy[order-1] or y+dy[order-1] >= m:
        continue 
    x += dx[order-1]
    y += dy[order-1]
    
    if order == 1: # 동
        dice = turn_right(dice)
    elif order == 2: # 서
        dice = turn_left(dice)
    elif order == 3: # 북
        dice = turn_up(dice)
    else: # 남
        dice = turn_down(dice)
    
    if arr[x][y] == 0:
        arr[x][y] = dice[3][1]
    elif arr[x][y] !=0:
        arr[x][y],dice[3][1] =0,arr[x][y]
    print(dice[1][1])