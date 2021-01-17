#import numpy as np
t= int(input())


for _ in range(t):
    n,m = map(int,input().split())
    #dp = []
    result = 0
    arr = []
    tmp = list(map(int,input().split()))
    for j in range(n):
        arr.append(tmp[m*j:m*(j+1)])
    
    for i in range(1,m):
        for j in range(n):
            # 왼쪽 위에서 올때
            if j == 0:
                left_up = 0
            else:
                left_up = arr[j-1][i-1]
            # 왼쪽 아래에서 올때
            if j == n-1:
                left_down = 0
            else:
                left_down = arr[j+1][i-1]
            # 왼쪽에서 올때
            left = arr[j][i-1]
            arr[j][i] = arr[j][i]+max(left_up, left, left_down)

    for i in range(n):
        result = max(result, arr[i][m-1])
    print(result)


        



    
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2