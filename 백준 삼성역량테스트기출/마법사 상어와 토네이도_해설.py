import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
def direction(x):
    if x == L: return D
    elif x == D : return R
    elif x == R : return U
    elif x == U : return L
def cal2(y,x,dir2):
    result = trash = 0
    for yi,xi,k in dir2:
        tmp = int(a[y][x]*k)
        if 0<= y + yi < n and 0<=x+xi<n:
            a[y+yi][x+xi]+=tmp
        else:
            result+=tmp
        trash +=tmp
    a[y][x]-=trash
    return result
def cal(dir,y,x):
    global result
    if dir == L : result += cal2(y,x,LL)
    elif dir == R : result += cal2(y,x,RR)
    elif dir == U : result += cal2(y,x,UU)
    elif dir == D : result += cal2(y,x,DD)
    if 0<= y+ dir[0] < n and 0 <= x+dir[1]<n:
        a[y+ dir[0]][x+dir[1]] +=a[y][x]
    else:
        result +=a[y][x]
    a[y][x] = 0
LL = [[-1,-1,0.1], [-1,0,0.07], [-1,1,0.01],[1,-1,0.1],[1,0,0.07],[1,1,0.01],[-2,0,0.02],[2,0,0.02],[0,-2,0.05]]
RR = [[-1,-1,0.01], [-1,0,0.07], [-1,1,0.1],[1,-1,0.01],[1,0,0.07],[1,1,0.1],[-2,0,0.02],[2,0,0.02],[0,2,0.05]]
UU = [[-1,1,0.1],[0,1,0.07],[1,1,0.01],[-1,-1,0.1],[0,-1,0.07],[1,-1,0.01],[0,2,0.02],[0,-2,0.02],[-2,0,0.05]]
DD = [[-1,1,0.01],[0,1,0.07],[1,1,0.1],[-1,-1,0.01],[0,-1,0.07],[1,-1,0.1],[0,2,0.02],[0,-2,0.02],[2,0,0.05]]
L,R,U,D = [0,-1],[0,1],[-1,0],[1,0]
y = x = n//2
size = 1
dir = L
cnt = result = 0
while 1:
    y,x = y+dir[0],x+dir[1]
    cal(dir,y,x)
    cnt+=1
    if cnt == size:
        if dir == U or dir == D:
            size +=1
        dir = direction(dir)
        cnt=0
    if y == 0 and x == 0: break
print(result) 