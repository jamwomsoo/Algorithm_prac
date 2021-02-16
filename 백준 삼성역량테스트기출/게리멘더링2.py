n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
ans =int(1e9)
            
def func(x,y,d1,d2):
    global ans
    line = [[int(1e9),-int(1e9)] for _ in range (n+1)]
    arr = [[5]*(n+1) for _ in range(n+1)]
    _min = int(1e9)
    _max = -int(1e9)
    one=two=three=four=five = 0
    # line 5
    # .1
    for i in range(0,d1+1):
        r = x+i
        c = y-i
        if arr[r][c] == 6:
            continue
        five+=board[r-1][c-1]
        arr[r][c] = 6
        line[r][0] = min(line[r][0],c)
        line[r][1] = max(line[r][1],c)
    # .2
    for i in range(0,d2+1):
        r = x+i
        c = y+i
        if arr[r][c] == 6:
            continue
        five+=board[r-1][c-1]
        arr[r][c] = 6
        line[r][0] = min(line[r][0],c)
        line[r][1] = max(line[r][1],c)

    # .3
    for i in range(0,d2+1):
        r = x+d1+i
        c = y-d1+i
        if arr[r][c] == 6:
            continue
        five+=board[r-1][c-1]
        arr[r][c] = 6
        line[r][0] = min(line[r][0],c)
        line[r][1] = max(line[r][1],c)

    # .4
    for i in range(0,d1+1):
        r = x+d2+i
        c = y+d2-i
        if arr[r][c] == 6:
            continue
        five+=board[r-1][c-1]
        arr[r][c] = 6
        line[r][0] = min(line[r][0],c)
        line[r][1] = max(line[r][1],c)
    #1
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if line[r][0]<= c <= line[r][1]: continue   
            if arr[r][c] !=6:
                one += board[r-1][c-1]
                arr[r][c] = 1
    #2
    for r in range(1, x+d2+1):
        for c in range(y+1, n+1):
            if line[r][0]<= c <= line[r][1]: continue
            if arr[r][c] !=6:
                two+=board[r-1][c-1]
                arr[r][c] = 2
    #3
    for r in range(x+d1, n+1):
        for c in range(1, y-d1+d2):
            if line[r][0]<= c <= line[r][1]: continue
            if arr[r][c] !=6:
                three+=board[r-1][c-1]
                arr[r][c] = 3
    #4
    for r in range(x+d2+1, n+1):
        for c in range(y-d1+d2, n+1):
            if line[r][0]<= c <= line[r][1]: continue
            if arr[r][c] !=6:
                four+=board[r-1][c-1]
                arr[r][c] = 4
    #inside 5
    for r in range(1,n+1):
        for c in range(1,n+1):
            if arr[r][c] == 5:
                five+=board[r-1][c-1]

    
    _min = min(one,two,three,four,five)
    _max = max(one,two,three,four,five)
    ans = min(ans, _max - _min)

def find_d1d2(x,y):
    global n
    for d1 in range(1,n-1):
        for d2 in range(1,n-1):
            if 1<=x<x+d1+d2<=n and 1<=y-d1<y<y+d2<=n:
                func(x,y,d1,d2) 
            else:
                break
            
for x in range(1,n-1):
    for y in range(2,n):
        find_d1d2(x,y)
print(ans)