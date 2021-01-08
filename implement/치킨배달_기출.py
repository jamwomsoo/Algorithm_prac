#0 빈칸,2 치킨집,1 집
import heapq
from collections import deque
from copy import deepcopy
n, m = map(int, input().split())
arr = [[] for i in range(n)]
for i in range(n):
  arr[i].extend(list(map(int,input().split())))
chicken=[]
home = []
cnt = [[0]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if arr[i][j] == 2:
      chicken.append((i,j))
    if arr[i][j] == 1:
      home.append((i,j))
      
#home =[[] for _ in range(1)] 
j = []
#print(chicken)
for x1,y1 in home:
  last = int(1e9)
  for x2,y2 in chicken:
    #print(x1,y1," ",x2,y2,end=" 거리 ")
    #print(last," ",abs(x1-x2)+abs(y1-y2))
    if last > abs(x1-x2)+abs(y1-y2):
      dx,dy = x2,y2
      last = abs(x1-x2)+abs(y1-y2)
  j.append(((dx,dy),(x1,y1),last))
#print(j)
re=0
if m < len(chicken):
  tmp =[]
  for i in range(len(j)):
    x,y = j[i][0]
    cnt[x][y]+=1
  for i in range(m):
    big = 0
    for x in range(n):
      for y in range(n):
        if big < cnt[x][y]:
          big = cnt[x][y]
          xn,yn =x,y
    tmp.append((xn,yn))
    cnt[xn][yn] = 0

  for i in tmp:
    x,y = i  
    for a in j:
      if (x,y) == a[0]:
        re+=a[2]
else:
  while j:
    re+=j.pop()[2]
print(re)
  


