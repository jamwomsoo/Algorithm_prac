import sys
sys.setrecursionlimit(11111111)
def dfs(x):
    global ans
    cycle.append(x)
    visited[x] = True
    number = select[x]
    if visited[number]:
        if number in cycle:
            ans += cycle[cycle.index(number):]
    else:
        dfs(number)


for _ in range(int(input())):
    n = int(input())
    select=[0]+ list(map(int,input().split()))
    ans= []
    visited = [True]+[False]*n
    for i in range(1,n+1):
        cycle = []
        dfs(i)
print(ans)   
print(n-len(ans))       
