from collections import deque
n, l, r=map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
total_count=0

def process(x,y,index):
    united = []
    united.append((x,y))
    people=graph[x][y]
    q = deque()
    q.append((x,y))
    visited[x][y] = index
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            xn = dx[i]+x
            yn = dy[i]+y
            if xn>=0 and yn>=0 and xn<n and yn < n and visited[xn][yn] ==-1:
                if l<= abs(graph[x][y] - graph[xn][yn]) <=r:
                    q.append((xn,yn))
                    visited[xn][yn] = index
                    people+=graph[xn][yn]
                    cnt+=1
                    united.append((xn,yn))
    for x,y in united:
        graph[x][y] = people//cnt
    return 
while True:
    visited =[[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                process(i,j,index)
                index+=1
    if index == n*n:#모든 나라가 이동이 없으면 칸 수에 맞게 한번씩 검사해서 배열의 전체 크기와 비슷해진다
        break
    total_count+=1
print(total_count)
        


        

