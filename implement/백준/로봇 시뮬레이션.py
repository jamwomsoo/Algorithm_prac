import sys
def find_location(num):
    global a,b
    #print(num)
    for y in range(b):
        for x in range(a):
           # print(board[y][x])
            if board[y][x]:
                if board[y][x][0] == num:
                    return y,x
    return None
direction = [(0,-1),(1,0),(0,1),(-1,0)]

a,b = map(int, input().split())
n,m = map(int, input().split())
board =[[[] for _ in range(a)] for _ in range(b)]
# for i in range(b):
#     for j in range(a):
#         print(board[i][j], end = " ")
#     print()
command = []
for i in range(n):
    x,y,d = map(str, input().split())
    
    if d == 'N': d = 0
    elif d == 'E': d = 1
    elif d == 'S': d = 2
    else: d = 3 
    #print("robot_location",b-(int(y)),int(x) - 1)
    board[b-int(y)][int(x) - 1] = [i+1,d]
# for i in range(b):
#     for j in range(a):
#         print(board[i][j], end = " ")
#     print()

for i in range(m):
    num, com, cnt = map(str, input().split())
    y,x = find_location(int(num))
    d = board[y][x][1]
    board[y][x] = []
    for i in range(int(cnt)):
        if com == 'F':
            x+=direction[d][0]
            y+=direction[d][1]
        #print(y,x)
        if not (0<=x< a and 0<= y <b): 
            print("Robot {0} crashes into the wall".format(num))
            sys.exit()
        if board[y][x]:
            print("Robot {0} crashes into robot {1}".format(num,board[y][x][0])) 
            sys.exit()
        elif com == 'L':
            d-=1
            if d<0: d = 3
        elif com == 'R':
            d+=1
            if d>3: d = 0

    board[y][x] = [int(num),d]
print("OK")