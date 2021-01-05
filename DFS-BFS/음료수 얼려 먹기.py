#나의 풀이 bfs방법
import time
from collections import deque
n,m = map(int, input().split())
ls = [list(map(int, input())) for _ in range(n)]
queue = deque([])
cnt=0

def Bfs(x,ls):
    global cnt
    for i in range(m):
        queue.append((x,i))
        if ls[x][i] == 1 :
            queue.popleft()
            continue
        ls[x][i]=1
        while True:
            xn,yn = queue.popleft()  
            if xn!=n-1 and ls[xn+1][yn] == 0:
                ls[xn+1][yn] =1
                queue.append((xn+1,yn))
            if xn != 0 and ls[xn-1][yn] == 0:
                ls[xn-1][yn] =1
                queue.append((xn-1,yn))
            if yn!=m-1 and ls[xn][yn+1] == 0:
                ls[xn][yn+1] =1
                queue.append((xn,yn+1))
            if yn!=0 and ls[xn][yn-1] == 0:
                ls[xn][yn-1] =1
                queue.append((xn,yn-1))
            if not queue:
                cnt+=1
                break
st = time.time()
for i in range(n):
    Bfs(i,ls)
ft = time.time()
print(ft - st)

print(cnt)

#DFS방법으로 해설
""" n,m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]
cnt=0
def Dfs(x,y,graph):
    if x > n-1 or x < 0 or y > m-1 or y<0:
        return False
    if graph[x][y] == 0:
        graph[x][y] =1
        Dfs(x-1,y,graph)
        Dfs(x+1,y,graph)
        Dfs(x,y-1,graph)
        Dfs(x,y+1,graph)
        return True
    return False

for i in range(n):
    for j in range(m):
        if Dfs(i,j,graph) == True:
            cnt+=1

print(cnt) """