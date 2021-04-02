# 두 선분이 교차할 경우 X -> 작은 방 하나 내부에 방 4개가 생긴다
# 이를 위해 한번의 이동이 아니라 두번의 이동으로 확대해서 도형의 크기들을 두배로 늘린다
# 1. 경로에 따라 두배로 도형을 그린다
# 2. 경로를 이동하다가 이미 존재하는 node에 만났을때 해당 vertex가 방문해 보지 않는 선분이면 새로운 방이 생기기 때문에 
# 답에 하나를 더해주고 해당 vertex는 방문 처리한다(딕셔너리는 set()를 키로 취급하지 못하므로 선분 방문시 역순도 방문처리해줘야 한다)
from collections import deque
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
def solution(arrows):
    answer= x = y = 0
    
    node = {}
    node[(0,0)] = 0
    vertex = {}
    q = deque([(0,0)])
    #print(parent)
    now_x = now_y = 0
    for direction in arrows:
        for j in range(2):
            nx = x+dx[direction]
            ny = y+dy[direction]
            node[(nx,ny)] = 0
            vertex[(x,y,nx,ny)] = 0
            vertex[(nx,ny,x,y)] = 0
            q.append((nx,ny))
            x,y = nx,ny
    #print(q)
    x,y = q.popleft()
    node[(x,y)] = 1
    while q:
        nx,ny = q.popleft()

        if node[(nx,ny)] == 1:
            if vertex[(x,y,nx,ny)] == 0:
                answer+=1
                vertex[(x,y,nx,ny)] = 1
                vertex[(nx,ny,x,y)] = 1
        else:
            node[(nx,ny)] = 1
            vertex[(x,y,nx,ny)] = 1
            vertex[(nx,ny,x,y)] = 1
        x,y = nx,ny
    #print(node)
    return answer


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([6,6,4,4,2,2,0,0,6,5,3,1,7]))