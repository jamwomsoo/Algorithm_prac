from collections import deque
n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
data = []
ans = 0

def cut(x):
    global m,ans
    if m<=0: return
    x-=10
    ans+=1; m-=1
    if x>10: cut(x)
    elif x == 10: ans+=1
    return


for i in arr:
    if m<=0: break
    elif i == 10:
         ans+=1
    elif i<10: continue
    elif i%10 == 0: cut(i)
    else: data.append(i)
for i in data:
    cut(i)
print(ans)