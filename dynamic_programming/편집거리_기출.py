str1 = str(input())
str2 = str(input())

# ##############################
# 최소 편집 거리 구하기 알고리즘 #
# ##############################

def edit_distance():
    n = len(str1)
    m = len(str2)
    dp =[[0]*(m+1) for _ in range (n+1)]

    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    for i in range(1,n+1):
        for j in range(1,m+1):
            #두 문자의 글자가 같다면, 왼쪽위의 수를 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                #왼쪽(삽입), 위쪽(삭제), 왼쪽위(교체)
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[n][m]
print(edit_distance())