from collections import deque
import heapq
import sys
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,gas = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
now_x,now_y = map(int, input().split())
now_x-=1
now_y-=1
passenger = []

for _ in range(m):
    start_x, start_y, end_x, end_y = map(int, input().split())
    passenger.append([start_x-1, start_y-1,end_x-1,end_y-1])

def min_distance(array):
    start_x,start_y = array[0],array[1]
    end_x,end_y = array[2],array[3]
    q= []
    visited = [[False]*n for _ in range(n)]
    heapq.heappush(q,[start_x,start_y,0])
    #q.append([start_x,start_y,0])
    visited[start_x][start_y] = True
    while q:
        #x,y,cost = q.popleft()
        x,y,cost = heapq.heappop(q)
        if x == end_x and y == end_y:
            return cost,True
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if (0 <= nx < n and 0 <= ny < n) and visited[nx][ny] == False and board[nx][ny] == 0:
                q.append([nx,ny,cost+1])
                visited[nx][ny] = True
               
    return 0,False
        

for time in range(m):
  
    if gas<=0:
        print(-1)
        sys.exit()
    _min = int(1e9)
    _min_index = 0
    _flag = False
    for i in range(m):
        if not passenger[i]:
            continue
        cost,Flag = min_distance([now_x, now_y,passenger[i][0], passenger[i][1]])
        #distance[i] = cost
        if _min > cost:
            _min = cost
            _min_index = i
            _flag = True
    gas -= _min
    #print(_min_index)
    if gas < 0 or _flag == False:
        print(-1)
        sys.exit()
    to_end_cost,_flag = min_distance(passenger[_min_index])
    gas-=to_end_cost
    if _flag == False:
        print(-1)
        sys.exit()
    if gas<0:
        print(-1)
        sys.exit()
    gas+=to_end_cost*2
    now_x, now_y = passenger[_min_index][2],passenger[_min_index][3] 
    passenger[_min_index] = []
    
print(gas)