# https://hoyeonkim795.github.io/posts/20061-%EB%AA%A8%EB%85%B8%EB%AF%B8%EB%85%B8%EB%8F%84%EB%AF%B8%EB%85%B82-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC/
# 참고 사이트

import sys
n = int(input())

red_blue = [[0]*10 for _ in range(4)]
red_green = [[0]*4 for _ in range(10)]
ans = 0

def green_remove(red_green, ans):
    while True:
        for i in range(10):
            if red_green[i] == [1,1,1,1]:
                ans+=1
                red_green[i] = [0,0,0,0]
                for x in range(i,0,-1):
                    red_green[x] = red_green[x-1]
                red_green[0] = [0,0,0,0]
        else:
            break
    return red_green,ans
def blue_remove(red_blue, ans):
    while True:
        for j in range(10):
            if (red_blue[0][j], red_blue[1][j],red_blue[2][j],red_blue[3][j]) == (1,1,1,1):
                ans+=1
                red_blue[0][j], red_blue[1][j],red_blue[2][j],red_blue[3][j] = 0,0,0,0
                for y in range(j,0,-1):
                    red_blue[0][y], red_blue[1][y],red_blue[2][y],red_blue[3][y] \
                        = red_blue[0][y-1], red_blue[1][y-1],red_blue[2][y-1],red_blue[3][y-1]
        else:
            break
    return red_blue,ans

def blue_special(red_blue):
    flag = False
    for i in range(4):
        if red_blue[i][4] == 1 or red_blue[i][5] == 1:
            flag = True
            break
    if flag:
        while True:
            if (red_blue[0][4], red_blue[1][4],red_blue[2][4],red_blue[3][4]) == (0,0,0,0) and\
                 (red_blue[0][5], red_blue[1][5],red_blue[2][5],red_blue[3][5]) == (0,0,0,0):
                break
            for y in range(9,4,-1):
                red_blue[0][y], red_blue[1][y],red_blue[2][y],red_blue[3][y] =\
                     red_blue[0][y-1], red_blue[1][y-1],red_blue[2][y-1],red_blue[3][y-1]
            red_blue[0][4], red_blue[1][4],red_blue[2][4],red_blue[3][4] = 0,0,0,0
    return red_blue
def green_special(red_green):
    flag= False
    for j in range(4):
        if red_green[4][j] == 1 or red_green[5][j] == 1:
            flag = True
            break
    if flag:
        while True:
            if red_green[4] == [0,0,0,0] and red_green[5] == [0,0,0,0]:
                break
            for i in range(9,4,-1):
                red_green[i] = red_green[i-1]
            red_green[4] = [0,0,0,0]
    return red_green
for _ in range(n):
    t,x,y = map(int, input().split())
    nx,ny = x,y
    if t == 1:
        # 빨 - 초        
        for i in range (1,10-x):
            if red_green[x+i][y] == 0:
                nx, ny = x+i, y
            else:
                nx,ny = x-1+i ,y
                break
        red_green[nx][ny] = 1
        # 빨 - 파
        for i in range(1,10-y):
            if red_blue[x][y+i] == 0:
                nx, ny = x,y+i
            else:
                nx,ny = x,y-1+i
                break
        red_blue[nx][ny] = 1
    elif t == 2:
        #빨 - 초
        nx, ny = x, y
        a,b = x, y+1
        for i in range(1,10-x):
            if red_green[x+i][y] == 0 and red_green[x+i][y+1] == 0:
                nx,ny = x+i,y
                a,b = x+i,y+1
            else:
                nx,ny = x+i-1,y
                a,b = x+i-1,y+1
                break
        red_green[nx][ny] = 1
        red_green[a][b] = 1
        # 빨 - 파
        nx,ny = x,y
        a, b = x, y+1
        for i in range(1,9-y):
            if red_blue[x][y+i] ==0 and red_blue[x][y+i+1] ==0:
                nx,ny =x,y+i
                a, b = x,y+1+i
            else:
                nx,ny = x, y+i-1
                a,b = x, y+i
                break
        red_blue[nx][ny] = 1
        red_blue[a][b] = 1
    elif t == 3:
        # 빨 - 초
        nx, ny = x+1,y
        for i in range(1,9-x):
            if red_green[x+i+1][y] == 0 and red_green[x+i][y] == 0:
                nx, ny = x+1+i,y
            else:
                nx,ny = x+i,y
                break
        red_green[nx][ny] = 1
        red_green[nx-1][ny] = 1

        nx, ny = x+1, y
        for i in range(1,10-y):
            if red_blue[x][y+i] ==0 and red_blue[x+1][y+i] == 0:
                nx,ny = x+1,y+i
            else:
                nx,ny = x+1,y-1+i
                break
        red_blue[nx][ny] = 1
        red_blue[nx-1][ny] = 1

    red_blue,ans = blue_remove(red_blue,ans)
    red_green,ans = green_remove(red_green,ans)
    red_blue = blue_special(red_blue)
    red_green = green_special(red_green)

print(ans)
total = 0
for i in range(6,10):
    total+=sum(red_green[i])
for i in range(4):
    total+=sum(red_blue[i])
print(total)
