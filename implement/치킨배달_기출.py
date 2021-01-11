from itertools import combinations
n, m = map(int, input().split())
arr = [ [] for i in range(n)]
for i in range(n):
  arr[i] = list(map(int,input().split()))

chicken = []
house = []
for i in range(n):
  for j in range(n):
    if arr[i][j] == 2:
      chicken.append((i,j))
    elif arr[i][j] == 1:
      house.append((i,j))

coms = combinations(chicken,m)
chicken_distance_short = int(1e9)#각 집에서 조합된 치킨집들까지의 치킨거리의 합 중 최소만 찾는다
for com in coms:
  tmp = 0
  for h in house:
    short = int(1e9)
    x1,y1 = h
    for i in com:
      x2,y2 = i
      if short > abs(x1-x2)+ abs(y1-y2):
        short = abs(x1-x2)+ abs(y1-y2)
    tmp += short
  if chicken_distance_short > tmp :
    chicken_distance_short = tmp 

print(chicken_distance_short)

