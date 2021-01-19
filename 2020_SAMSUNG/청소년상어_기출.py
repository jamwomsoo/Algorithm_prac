# 청소년 상어가 먹을 수 있는 물고기 수가 여러개인 경우가 존재하므로, 완전탐색으로 수행
# 완전 탐색을 수행할 때는 DFS사용

import copy
array=[[None]*4 for _ in range(4)]
result=0
for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        array[i][j] = [data[j*2],data[j*2+1]-1] # 물고기, 방향
# 8개의 방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
def turn_left(direction):
    return (direction + 1) % 8

# 해당 번호의 물고기가 있는 위치를 반환
# 없으면 none 리턴
def find_fish(array,index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return i,j
    return None
# 물고기가 전부 움직이는 함수
def move_all_fish(array,now_x,now_y):
    for i in range(1,17):
        position = find_fish(array,i)
        if position != None:
            x, y = position[0],position[1]
            direction = array[x][y][1]
            for j in range(8):
                nx = x+dx[direction]
                ny = y+dy[direction]
                if 0<=nx<4 and 0<=ny<4:
                    if not (nx == now_x and ny == now_y): # 옮길 위치가 상어가 있는 위치가 아니면
                        array[x][y][1] = direction # 바뀐 방향성을 저장
                        array[x][y], array[nx][ny] = array[nx][ny],array[x][y]
                        break
                direction = turn_left(direction)
# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array,now_x,now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재 상어의 방향으로 이동할 수 있는 모든 경우의 수를 반환(완전 탐색을 위해)
    for i in range(3):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0<=now_x<4 and 0<=now_y<4:
            if array[now_x][now_y][0] != -1: # 물고기가 있으면
                positions.append((now_x, now_y))
    return positions
def dfs(array, now_x,now_y,total):
    global result
    array = copy.deepcopy(array)

    total +=array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    move_all_fish(array,now_x,now_y)

    positions = get_possible_positions(array,now_x,now_y)
    
    if len(positions) == 0:
        result = max(result,total) # 완전 탐색으로 생긴 여러개의 케이스중 가장 큰 값을 갖기 위해서
        return
    for next_x,next_y in positions:
        dfs(array,next_x,next_y,total)

dfs(array,0,0,0)
print(result)


