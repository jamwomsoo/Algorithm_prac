from itertools import permutations
from collections import deque
size = 4
myboard = [[] for i in range(4)] # 새로운 board
card_pos = {} # 캐릭터 : 위치,위치
d = [[0,1],[1,0],[0,-1],[-1,0]]
INF = int(1e4)
answer = INF
orders = [] # 캐릭터 사라지는 순열

# 1. 새로운 board 만듦
# 2. 캐릭터 넘버가 키값이고 board에서 해당 숫자를 갖고 있는 위치를 value로 집어넣는다
# 3. 모든 캐릭터들이 없어지는 순서들이 최대 6!이다. 이 모든 경우의 순열을 구해준다
def init(board):
    global myboard, card_pos, orders
    for i in range(size):
        for j in range(size):
            if board[i][j]>0 :
                card = board[i][j]
                if card not in card_pos.keys(): card_pos[card] = [[i,j]]
                else : card_pos[card].append([i,j])

            myboard[i].append(board[i][j])
    orders = [key for key in card_pos.keys()]
    orders = list(permutations(orders))
# board 내부에 있는 지 확인하는 함수
def isin(x,y):
    if -1<x<size and -1<y<size:return True
    return False
# crtl이동
def move(x,y,d):
    global myboard
    nx,ny = x,y
    while True:
        _nx = nx+d[0]
        _ny = ny+d[1]
        if not isin(_nx,_ny): return nx,ny
        if myboard[_nx][_ny] != 0: return _nx,_ny
        nx,ny = _nx,_ny
# 현재 위치에서 목적지 까지 가는 값과 목적지 좌표를 반환해주는 함수
# 이동 함수(일반이동, Ctrl 이동)
def bfs(sx,sy,ex,ey):
    if [sx,sy] == [ex,ey]: return sx,sy,1
    global myboard
    q = []
    q = deque(q)
    table = [[0 for _ in range(size)] for _ in range(size)]
    visit = [[False for _ in range(size)] for _ in range(size)]
    q.append([sx,sy])
    visit[sx][sy] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            # 일반이동
            if isin(nx,ny):
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    table[nx][ny] = table[x][y]+1
                    if [nx,ny] == [ex,ey]:
                        return nx, ny, table[nx][ny] + 1
                    q.append([nx,ny])
            # Ctrl 이동
            nx,ny = move(x,y,d[i])
            
            if not visit[nx][ny]:
                visit[nx][ny] = True
                table[nx][ny] = table[x][y]+1
                if [nx,ny] == [ex,ey]:
                    return nx, ny, table[nx][ny] + 1

                q.append([nx,ny])

    return sx, sy, INF

# 백트레킹에 사용될 함수
# Board에서 순서가 된 캐릭터가 들어있는 곳을 0으로 채운다(비운다)
def remove(card):
    global myboard, card_pos
    for x,y in card_pos[card]: myboard[x][y] = 0
# 백트레킹에 사용될 함수
# Board에서 순서가 된 캐릭터가 들어있는 곳을 원래 캐릭터 숫자로으로 채운다
def restore(card):
    global myboard, card_pos
    for x,y in card_pos[card]: myboard[x][y] = card
# 캐릭터간 순열의 경우의 수 중 하나
# 그것 중에서 캐릭터 1번 혹은 2번 위치가 먼저일때의 경우의 수를 파악해줘야 한다 
def backtrack(sx, sy, k ,m ,count):
    global orders, myboard, answer, card_pos

    if k == len(card_pos.keys()):
        if answer > count: answer = count
        return

    card = orders[m][k]
    left_x, left_y = card_pos[card][0][0], card_pos[card][0][1]
    right_x, right_y = card_pos[card][1][0], card_pos[card][1][1]

    rx1, ry1, res1 = bfs(sx, sy, left_x, left_y)
    rx2, ry2, res2 = bfs(rx1, ry1, right_x, right_y)

    remove(card)
    backtrack(rx2,ry2, k+1, m, count + res1 + res2)
    restore(card)

    rx1, ry1, res1 = bfs(sx, sy, right_x, right_y)
    rx2, ry2, res2 = bfs(rx1, ry1, left_x, left_y)

    remove(card)
    backtrack(rx2,ry2, k+1, m, count + res1 + res2)
    restore(card)

def solution(board,r,c):
    global answer
    init(board)
    
    for i in range(len(orders)):
        backtrack(r, c, 0, i, 0)
    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],0,1))