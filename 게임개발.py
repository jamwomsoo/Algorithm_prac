#내가 푼거
# n,m = map(int, input().split())
# raw, column, s = map(int,input().split())
# ls =[]
# check = 0
# for i in range(m):
#   ls.append(list(map(int,input().split())))
# plans = [0,1,2,3]
# xn = [-1,0,1,0]
# yn = [0,1,0,-1]
# cnt = 0
# stack=0
# while check !=1 :
#     s+=3
#     for plan in plans:
#         if plan == (s%4):
#             x = xn[plan] + raw
#             y = yn[plan] +column
          
#             if x <0 or x >= n or y <0 or y>=m :
#                 continue
#             if ls[y][x] == 1 :
#                 stack+=1
#             if ls[y][x] == 0:# and ls2[y][x] == 0:
#                 ls[column][raw] = 1
#                 raw = x
#                 column = y
#                 cnt+=1
#                 stack=0
        
#     if stack>=4:    
#         s+=2    
#         x = xn[s%4] + raw
#         y = yn[s%4] +column
#         if  x <0 or x >= n or y <0 or y>=m:
#             continue
#         if ls[y][x] == 1:
#             cnt+=1
#             check = 1
#         raw = x
#         column = y
#         stack=0
# print(cnt)    

n,m = map(int, input().split())
raw, column, direction = map(int,input().split())
d =[[0]*m for _ in range(n)]
d[row][column]
array = []
for i in range(n):
  array.append(list(map(int,input().split())))
plans = [0,1,2,3]
xn = [-1,0,1,0]
yn = [0,1,0,-1]
cnt = 1
stack=0

def turn_left
    global direction
    direction-=1
    if direction = 3

while True:
    turn_left()
    x = column+xn[direction]
    y = row + yn[direction]
    if array[x][y] == 0 and d[x][y] == 0:
        column = x
        row = y
        cnt+=1
        stack=0
        continue
    else:
        stack+=1
    if stack >=4:
        x = column - xn[direction]
        y = row - yn[direction]
        if array[x][y] == 0:
            column = x
            row = y
        else:
            break
        stack=0
print(cnt)
