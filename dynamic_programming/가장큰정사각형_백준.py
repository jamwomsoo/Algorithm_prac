# 백준 DP 난이도 골드 5
# 전형적인 dp문제
# dp[i][j]는 위, 왼쪽, 대각선 위 중 작은 것중에 하나를 자신과 더한 값
# -> 정사각형이라면 변의 길이가 모두 같아야하므로
# 1 1 1    1 1 1
# 1 1 1 -> 1 2 2 
# 1 1 1    1 2 3

n, m = map(int, input().split())
arr = []
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    arr.append(list(map(int, input())))
    for j in range(m):
        dp[i+1][j+1] = arr[i][j]

for i in range(n+1):
    for j in range(m+1):
        if dp[i][j] != 0:
            dp[i][j] += min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
res = 0
for row in dp:
    res = max(res, max(row))
print(res**2)
