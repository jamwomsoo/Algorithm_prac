import math
dx = [0,1,0,-1]
dy = [-1,0,1,0]
n = int(input())
s = 0
arr = [list(map(int, input().split())) for _ in range(n)]
state = [[0]*n for _ in range(n)]
now_x = now_y = n//2
direction = 0
for i in range(n):
    s+=sum(arr[i])
zero = [[-2,0,0.02],[-1,-1,0.1],[-1,0,0.07],[-1,1,0.01],[0,-2,0.05],[1,-1,0.1],[1,0,0.07],[1,1,0.01],[2,0,0.02]]
one = [[-1,-1,0.01], [-1,1,0.01], [0,-2,0.02], [0,-1,0.07],[0,1,0.07],[0,2,0.02],[1,-1,0.1],[1,1,0.1],[2,0,0.05]]
two = [[-2,0,0.02], [-1,-1,0.01],[-1,0,0.07],[-1,1,0.1],[0,2,0.05],[1,-1,0.01], [1,0,0.07], [1,1,0.1],[2,0,0.02]]
trd = [[-2,0,0.05],[-1,-1,0.1],[-1,1,0.1],[0,-2,0.02], [0,-1,0.07],[-1,1,0.07],[0,2,0.02],[1,-1,0.01],[1,1,0.01]]
d = [[0,-1], [1,0], [0,1], [-1,0]]
total = 0
#print()
cnt= 0
def dust2(x,y,direction):
    global n
    result = 0
    t = 0
    if direction == 0:
        narr = zero           
    elif direction == 1:
        narr = one 
    elif direction == 2:
        narr = two
    elif direction == 3:
        narr = trd
    
    for d_x, d_y, p in narr:
        tmp = int(p*arr[x][y])
        
        if not (0 <= x+d_x < n and 0 <= y+d_y < n):
            result+=tmp
        else:
            arr[x+d_x][y+d_y] += tmp
        #print(tmp)
        t+=tmp
    arr[x][y] -= t
    return result   
def dust1(x,y):
    global n,total,direction
    total += dust2(x,y,direction)
    if 0<= x+dx[direction] <n and 0<= y+dy[direction]<n:
        arr[x+d[direction][0]][y+d[direction][1]] += arr[x][y]
    else:
        total+=arr[x][y] 
    arr[x][y] = 0

index = 1
flag = False


while True:
  
    if now_x == 0 and now_y == 0:
        break
    # if not(0<=now_x<n and 0<= now_y<n):
    #     break
    cnt+=1
    print(now_x,now_y,direction)
    state[now_x][now_y] = index
    index+=1
    now_x,now_y = now_x + dx[direction],now_y + dy[direction]
    #먼지계산
    if arr[now_x][now_y] == 0:
        pass
    else:
        dust1(now_x,now_y)
    nx, ny = now_x + dx[(direction+1)%4],now_y + dy[(direction+1)%4]
    if state[nx][ny] == 0 and 0<=nx<n and 0<=ny<n:
        direction=(direction + 1)%4
        
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end = "\t")
        print()
    print()
    
# for i in range(n):
#     for j in range(n):
#         print(state[i][j],end = "\t")
#     print()
kk= 0
for i in range(n):
    kk+=sum(arr[i])
print(total)
