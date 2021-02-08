#이미 합친 블록은 또 합칠 수 없다
from copy import deepcopy 
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
def move_left(arr,index):
    new_arr =deepcopy(arr)
    if index == 1 or index == 3:
        start = n-1
        end = -1
        how = -1
    else:
        start = 0
        end = n
        how = 1
    for i in range(start,end,how):
        for j in range(start,end,how):
            if arr[i][j] > 0:
                print(i,j,new_arr)
                ny = j
                nx = i
                while True:
                    print(ny)
                    if 0 > ny + dy[index] or ny + dy[index] >= n or 0 > nx + dx[index] or nx + dx[index] >= n: # 옆에 모서리 벽일때
                        break
                    elif new_arr[nx+dx[index]][ny+dy[index]] > 0:         #옆에 숫자 칸일때
                        if new_arr[nx+dx[index]][ny + dy[index]] == arr[i][j]: # 옆칸에 동수 있을때
                            new_arr[nx+dx[index]][ny+dy[index]] +=arr[i][j]
                            new_arr[nx][ny] = 0
                        break
                    elif new_arr[nx+dx[index]][ny+dy[index]] == 0:            #옆에 비어 있을때
                        new_arr[nx+dx[index]][ny+dy[index]], new_arr[nx][ny]  = arr[i][j], 0
                        ny += dy[index]
                        nx += dx[index]  
    return new_arr



def dfs(arr,total,cnt):
    if cnt > 5 :
        result = max(result,total)
    arr = deepcopy(arr)
    #for i in range(4):
    new_arr = move_left(arr,0)
    print(new_arr)    



dfs(arr,0,0)