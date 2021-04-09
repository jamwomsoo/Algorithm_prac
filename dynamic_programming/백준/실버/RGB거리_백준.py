import sys
input = sys.stdin.readline
n = int(input())
arr = []
dp = [[0]*n for _ in range(n+1)]

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    dp[i+1][0] = arr[i][0] + min(dp[i][1], dp[i][2])
    dp[i+1][1] = arr[i][1] + min(dp[i][0], dp[i][2])
    dp[i+1][2] = arr[i][2] + min(dp[i][0], dp[i][1]) 

print(min(dp[-1][0],dp[-1][1],dp[-1][2]))
# print(min(dp[-1]))로하면 틀림 왤까???

    
        
