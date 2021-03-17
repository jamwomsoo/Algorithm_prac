import sys
a,b = map(int, input().split())
result = 0
flag = False


def dfs(x,cnt):
    global b,flag
    if x == b:
        print(cnt+1)
        flag = True
        return
    if x>b:
        return
    dfs(x*10+1,cnt+1)
    dfs(x*2,cnt+1)



dfs(a,0)
if not flag:
    print(-1)

