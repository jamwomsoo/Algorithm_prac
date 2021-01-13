#set{(1,2),(2,1)} 은 {(2,1)(1,2)}와 같다
#이동, 회전을 고려
#이동시 상,하,조ㅏ,우에서 갈 수 있는 곳을 생각
#회전시 가로 일때 좌표 두부분 중 하나를 기준으로 위가 모두 빌때 아래가 모두 빌때를 각각 고려
#세로일때 좌표 두 부분중 하나를 기준으로 오른쪽이 모두 빌때 왼쪽이 모두 빌때를 고려
# BFS이므로 결국 n,n까지 최단경로가 나옴 
from collections import deque
def get_next_pos(pos,new_board):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x,pos2_y = pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i],pos2_y + dy[i]

        if new_board[pos1_next_x][pos1_next_y] == 0 and new_board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x,pos1_next_y), (pos2_next_x,pos2_next_y)})
    if pos1_x == pos2_x:
        for i in [-1,1]:
            if new_board[pos1_x+i][pos1_y] == 0 and new_board[pos2_x+i][pos2_y] == 0:
                next_pos.append({(pos1_x+i, pos1_y), (pos1_x, pos1_y)})
                next_pos.append({(pos2_x+i, pos2_y), (pos2_x, pos2_y)})
    if pos1_y == pos2_y:
        for i in [-1,1]:
            if new_board[pos1_x][pos1_y+i] == 0 and new_board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y + i), (pos1_x, pos1_y)})
                next_pos.append({(pos2_x, pos2_y + i), (pos2_x, pos2_y)})
    return next_pos
def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(len(board[0])):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    pos = {(1,1),(1,2)}
    q=deque()
    visitied=[]
    q.append((pos,0))
    visitied.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n,n) in pos:
            return cost
        for next_pos in get_next_pos(pos,new_board):
            if next_pos not in visitied:
                q.append((next_pos,cost+1))
                visitied.append(next_pos)

    return 0

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))