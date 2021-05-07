from collections import deque
direction = [(-1,0),(1,0),(0,-1),(0,1)]
def find_xy(board,num):
    n = 4; m = 3
    for i in range(n):
        for j in range(m):
            if board[i][j] == num:
                return [i,j]
    return None
def find_direction(board,now,goal):
    visited =[[-1]*3 for _ in range(4)]
    q = deque()
    q.append(now)
    visited[now[0]][now[1]] = 0
    while q:
        x,y = q.popleft()
        if board[x][y] == goal:
            return visited[x][y]
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0<=nx<4 and 0<=ny<3 and visited[nx][ny] == -1:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y]+1
        
def solution(numbers, hand):
    answer = ''
    board = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left_now = [3,0]
    right_now = [3,2]

    for num in numbers:
       
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left_now = find_xy(board,num)
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right_now = find_xy(board,num)
        else:
            l = find_direction(board,left_now,num)
            r = find_direction(board,right_now,num)
            
            if l<r:
                answer+='L'
                left_now = find_xy(board,num)
            elif l>r:
                answer+='R'
                right_now = find_xy(board,num)
            else:
                if hand == 'right':
                    answer+='R'
                    right_now = find_xy(board,num)
                else:
                    answer+='L'
                    left_now = find_xy(board,num)
      
    return answer
#print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
#print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))