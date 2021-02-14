n = int(input())

dy = [0,-1,0,1]
dx = [1,0,-1,0]
total = set()
def dragon_curve(x,y,g):

    if g == 0:
        return
    length = len(dragon)
    for k in range(length-1,-1,-1):
        i,j = dragon[k]
       
        if x == i and y == j:
            continue
    
        nx,ny = (x+y) - j, i + (y - x)
        if 0<=nx<=100 and 0<=ny<=100:
            dragon.append((nx,ny))
    #print(dragon[-1][0],dragon[-1][1])
    dragon_curve(dragon[-1][0],dragon[-1][1],g-1)
    

for i in range(n):
    x,y,d,g = map(int, input().split())
    dragon = []
    dragon.append((x,y))
    nx,ny = x + dx[d], y+ dy[d]
    dragon.append((nx,ny))

    dragon_curve(nx,ny,g)
 
    for j in range(len(dragon)):
        x,y = dragon[j]
        total.add((x,y))

result = 0
for x,y in total:
    if (x,y) in total and (x+1,y) in total and (x+1,y+1) in total and (x,y+1) in total:
        result+=1
print(result) 