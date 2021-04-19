import sys
direction = [(0,1),(0,-1),(1,0),(-1,0)]
d = ['E','W','S','N']
# 동, 서, 남, 북
n ,d_e,d_w,d_s,d_n = map(int, input().split())
if n == 0:
    print(1)
    sys.exit()
arr = [d_e/100,d_w/100,d_s/100,d_n/100]

ans = 0
def dfs(x,y,visited,cnt,value):
    global n,ans
    if cnt == n:
        #print(word)
        ans+=value
        return 
    
    for i in range(4):
        dx,dy = direction[i]
        nx,ny = x+dx,y+dy
 
        if [nx,ny] not in visited:
            visited.append([nx,ny])
            dfs(nx,ny,visited,cnt+1,value*arr[i])
            visited.pop()
dfs(0,0,[[0,0]],0,1)
print('{:.10f}'.format(ans))