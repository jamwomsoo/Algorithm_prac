from collections import deque
n, m = map(int, input().split())
arr = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x,y,direction = map(int, input().split())
for i in range(n):
    arr.append(list(map(int, input().split())))

def turn_left(direction):
    direction-=1
    if direction < 0:
        direction = 3
    return direction
q = deque()
q.append([x,y,1])
visited =set()
visited.add((x,y))
while q:
    now_x,now_y, vacuum = q.popleft()
    
    flag = False
    for i in range(4):
        direction = turn_left(direction)
        nx = now_x + dx[direction]
        ny = now_y + dy[direction]
        if 0 > nx or nx >= n or 0 > ny or ny >= m or arr[nx][ny] == 1 or (nx,ny) in visited:
            continue
        if arr[nx][ny] == 0 and (nx,ny) not in visited:
            visited.add((nx,ny))
            q.append([nx,ny,vacuum + 1])
            flag = True
            break
    if not flag:
        nx = now_x - dx[direction]
        ny = now_y - dy[direction]
        if 0 > nx or nx >= n or 0 > ny or ny >= m or arr[nx][ny] == 1:
            print(vacuum)
            break
        if arr[nx][ny] == 0:
            q.append([nx,ny,vacuum])

        


            

