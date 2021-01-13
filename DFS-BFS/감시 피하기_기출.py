from itertools import combinations

n = int(input())
graph = []
space = []
teacher = []
for i in range(n):
    graph.append(list(map(str,input().split())))
    for j in range(n):
        if graph[i][j] =='T':
            teacher.append((i,j))
        if graph[i][j] == 'X':
            space.append((i,j))
    
coms = combinations(space,3)

def check(x,y,i):
    direction = i
    if direction == 0:
        while x>=0:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x -= 1
            
    if direction == 1:
         while y>=0:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            y -= 1
   
    if direction == 2:
         while x < n:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x += 1
    
    if direction == 3:
         while y < n:
            
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            y += 1
    return False

def process():
    # 발생한 조합에서 모든 선생들의 시야에 학생이 있는지 없는지 확인
    for x,y in teacher:    
        for i in range(4):
            # 한명이라도 학생을 발견한 경우
            if check(x,y,i):
                return True
    #학생을 못 발견한 경우
    return False

find = False
# 방해물의 조합중 학생들이 발견 안될 상황을 찾는다
for com in coms:
    for x,y in com:
        graph[x][y]='O'
    # 해당 조합에서 학생을 못 찾았을 경우
    if not process():
        # 원하는 상황을 찾았다고 체크후 탈출
        find = True
        break
    for x,y in com:
        graph[x][y]='X'
if find:
    print("YES")
else:
    print("NO")
        
    
    

