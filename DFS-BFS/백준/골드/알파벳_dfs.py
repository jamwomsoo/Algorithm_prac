from copy import deepcopy
# 틀림 == 못품
direction = [(-1,0),(0,1),(1,0),(0,-1)]
n,m = map(int, input().split())
arr = [list(map(str,input())) for _ in range(n)]

alpha = [arr[0][0]]
answer = 1
def bfs(x,y):
    global n,m,answer
    q = set([(x,y,arr[x][y])])
    
    while q:
        x,y,ans = q.pop()
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            # 새로운칸이 중복되는 알파벳인지 체크
            if (0<=nx<n and 0<=ny<m) and (arr[nx][ny] not in ans):
                q.add((nx,ny,ans+arr[nx][ny]))
                answer = max(answer,len(ans)+1)
dfs(0,0)

print(answer)