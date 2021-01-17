################################################
# 2차원 리스트를 90도 회전한 결과를 반환 하는 함수
################################################
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
############################################################################
#정렬된 배열 1,2,2,2,2,3,4에서
# 2의 갯수 구하기
# 와일드카드를 포함한 쿼리와 비슷한 단어 찾기에 사용가능
def count_by_range(arr,a)
    left = bisect.bisect_left(arr,a)
    right = bisect.bisect_right(arr,a)
    return right-left

#############################################################################

# ##############################
# 최소 편집 거리 구하기 알고리즘 #
# ##############################
str1 = str(input())
str2 = str(input())

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

##############################################################################

  #####################################
 #LIS(가장 긴 증가하는 부분 수열 문제) #
######################################

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i],dp[j]+1)  
print(n-max(dp))

##############################################################################