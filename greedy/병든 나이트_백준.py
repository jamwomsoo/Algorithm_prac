#못품ㅋ
from collections import deque
n , m = map(int, input().split())
now = deque([(n-1,0)])
move = 0
# n이 더 클때
dxn = [-2, 2, -1, 1]#1, 4, 2, 3
dyn = [1, 1, 2, 2] 

# m이 더 클때 #2,3,1,4
dxm = [ -1, 1,-2, 2]
dym = [2, 2,1, 1 ]
check = [False]*4
changed=False
num = -1

while now:
    x,y = now.popleft()
    
    for i in range(8):
        if m>n:
            xn = x + dxm[i%4]
            yn = y + dym[i%4]
        else:
            xn = x + dxn[i%4]
            yn = y + dyn[i%4]
        if move>3:
            if i>=4:
                break
            if (0<=xn<n and 0<=yn<m) and check[i%4] == False:
                check[i%4] =True
                move+=1
                now.append((xn,yn))
                break
        else:
            if (0<=xn<n and 0<=yn<m) and (check[i%4] == False or i>=4):
                check[i%4] =True
                move+=1
                now.append((xn,yn))
                break
        print(now)
    if False not in check:
        check = [False]*4
        
print(move+1)