# 최단 경로로 가기위해서는 물웅덩이를 피해 오른쪽, 아래로만 갈수 있다
# i,j 의 최단경로는 i-1,j 과 i,j-1 로의 최단경로의 합이다
def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range(n+1)]

    dp[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:continue
            if [j,i] in puddles: continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return (dp[n][m])% 1000000007
print(solution(4,3,[[2,2]]))