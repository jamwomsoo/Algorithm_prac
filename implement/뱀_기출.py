from collections import deque
import heapq
n = int(input())
k = int(input())
apple_ls= []
for _ in range(k):
    x,y = map(int,input().split())
    apple_ls.append([x-1,y-1])
l = int(input())
move_ls  = deque()
for _ in range(l):
    t, m = input().split()
    move_ls.append((int(t),m))
    

def move(d):
  if d>4 :
    d=1
  if d<1:
    d=4
  return d

direction =2
dx = [0,-1,0,1,0]
dy = [0, 0,1,0,-1]
x = 0
y = 0
time=0
mine=deque()
t,m = move_ls.popleft() 
while True:
    if t== time:
        if m == 'D':
            direction+=1
        else:
            direction-=1
        direction= move(direction)
        if move_ls:
            t,m = move_ls.popleft()
    if [x,y] not in mine:
        mine.append([x,y])
    for i in range(1,5):
        if i == direction:
            x = x + dx[i]
            y = y + dy[i]
            break
    time+=1    
    if [x,y] in mine:
        break
    if x<0 or y<0 or x>=n or y>=n:
        break
    if [x,y] in apple_ls:
            mine.append([x,y])
            apple_ls.remove([x,y])
    else:
            mine.popleft()
     
print(time)


