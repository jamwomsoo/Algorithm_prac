point = list(map(int, input()))

h = len(point)//2

if sum(point[:h]) == sum(point[h:]):
  print("LUCKY")
else:
  print("READY") 