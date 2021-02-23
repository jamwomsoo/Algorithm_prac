import sys
sys.setrecursionlimit(10**5)
_dir = [(1,0),(0,1),(-1,0),(0,-1)]

n,q = map(int, input().split())
n = 2**n
ice = [list(map(int, input().split())) for _ in range(n)]

for L in list(map(int, input().split())):

    k = 2**L
    for x in range(0,n,k):
        for y in range(0,n,k):
            tmp = [ice[i][y:y+k] for i in range(x,x+k)]
            for i in range(k):
                for j in range(k):
                    # 기준점이 0,0 일때 기존 시계 회전
                    # new_arr[j][n-i-1] = arr[i][j]
                    # 기준점이 x,y 일때 시계 회전
                    ice[x+j][y+k-i-1] = tmp[i][j]

    cnt = [[0]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            for d in _dir:
                nx,ny = x+d[0],y+d[1]
                if 0<=nx<n and 0<=ny<n and ice[nx][ny]:
                    cnt[x][y]+=1

    for x in range(n):
        for y in range(0,n):
            if ice[x][y] > 0 and cnt[x][y] < 3:
                ice[x][y] -= 1

print((sum(sum(i) for i in ice)))

def dfs(x,y):
    ret = 1
    ice[x][y] = 0
    for d in _dir:
        nx,ny = x+d[0],y+d[1]
        if 0<=nx<n and 0<=ny<n and ice[nx][ny]:
            ret += dfs(nx,ny)
    return ret

ans = 0
for x in range(n):
    for y in range(n):
        if ice[x][y] > 0:
            ans = max(ans,dfs(x, y))
print(ans)

