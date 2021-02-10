# 모든 케이스를 검사 할때는 dfs로 모든 경우의 수를 확인 가능하다! -> 이게 핵심
#틀
n,m = map(int, input().split())
arr= [list(map(int, input().split())) for _ in range(n)]
cctvs = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]

cctv_allcase = []

def watch(x,y,direction):
    return_set = set()
    for d in direction:
        now_x,now_y =x,y
        while True:
            now_x+=dx[d]
            now_y+=dy[d]
            if not (0<=now_x<n and 0<=now_y<m): break
            if arr[now_x][now_y] == 6: break
            if arr[now_x][now_y] == 0:
                return_set.add((now_x, now_y))
            
    return return_set
def dfs(n,union_set):
    global _max
    if n == len(cctv_allcase):
        if _max < len(union_set):
            _max = len(union_set)
        return
    for i in cctv_allcase[n]:
        dfs(n+1,union_set|i)


empty = 0
for i in range(n):
    
    for j in range(m):
        if arr[i][j] == 0: empty = empty + 1
        if arr[i][j] == 1:
            cctv_allcase.append([watch(i,j,[0]),watch(i,j,[1]),watch(i,j,[2]),watch(i,j,[3])])
        if arr[i][j] == 2:
            cctv_allcase.append([watch(i,j,[1,3]),watch(i,j,[0,2])])
        if arr[i][j] == 3:
            cctv_allcase.append([watch(i,j,[0,1]),watch(i,j,[1,2]),watch(i,j,[2,3]),watch(i,j,[0,3])])
        if arr[i][j] == 4:
            cctv_allcase.append([watch(i,j,[0,1,3]),watch(i,j,[0,1,2]),watch(i,j,[1,2,3]),watch(i,j,[0,2,3])])
        if arr[i][j] == 5:
            cctv_allcase.append([watch(i,j,[0,1,2,3])])
    _max = -int(1e9)
    dfs(0,set())

print(empty -_max)