#틀
from copy import deepcopy
n, m, h = map(int, input().split())
arr = [[False]*(h+1) for _ in range(n+1)]
result = int(1e9)
def input_data():
    global n,m
    for i in range(m):
        a,b = map(int, input().split())
        # 0은 왼쪽에서 오른쪽 , 1은 오른쪽에서 왼쪽
        arr[b][a] = True

def ladder_game():
    global n,h
    for i in range(1, n+1):
        now = i
        for j in range(1,h+1):
            if arr[now][j]:
                now+=1
            elif arr[now-1][j]:
                now-=1
        if now != i:
            return False
    return True
        

def dfs(hori,cnt):
    global result,n,h
    if cnt>=4:
        return
    if ladder_game():
        result = min(result, cnt)
        return
    for i in range(hori,h+1):
        for j in range(1,n):
            if arr[j][i] or arr[j-1][i] or arr[j+1][i]: continue
            arr[j][i] = True
            dfs(i,cnt+1)
            arr[j][i] = False
    
def main():
    input_data()

    dfs(1,0)
    if result == int(1e9):
        print(-1)
    else:
        print(result)
main()