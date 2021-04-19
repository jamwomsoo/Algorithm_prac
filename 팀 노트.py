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
# 정렬된 배열 1,2,2,2,2,3,4에서
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
# DP문제
# 최소 편집 거리 알고리즘
# 두 문자가 같을때 -> dp[i][j] = dp[i-1][j-1]
# 두 문자가 다를때 -> dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) 
# @ @ c a t
# @ 0 1 2 3
# c 1 0 1 2
# u 2 1 1 2
# t 3 2 2 1

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
            # 두 문자의 글자가 같다면, 왼쪽위의 수를 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # 왼쪽(삽입), 위쪽(삭제), 왼쪽위(교체)
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[n][m]
print(edit_distance())

##############################################################################

  ######################################
 # LIS(가장 긴 증가하는 부분 수열 문제) #
########################################
#예) {10,20,10,30,40,50}일때
# dp를 [1, 1, 1, 1, 1, 1]초기화
# i는 index 1부터 n-1까지
# j는 i-1까지
# arr내에서 i-1까지 arr[i]보다 작은 수의 갯수를 세준다
# dp[i] = max(dp[i],dp[j]+1)
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i],dp[j]+1)  
print(n-max(dp))

#############################################################
# LIS 문제 이진 탐색버전
# 가장 긴 증가하는 수열 문제(LIS)
import bisect
n = int(input())
arr = list(map(int, input().split()))
dp = []
for d in arr:
    # dp가 없거나 d이전의 값들의 최댓값이 d보다 작을때
    if not dp or dp[-1]<d:
        dp.append(d)
    # d가 dp내의 최댓값 보다 작다면 binary search로 자리를 찾아서 넣어준다
    else:
        dp[bisect.bisect_left(dp,d)] = d
print(len(dp))



##############################################################################
################################
# target 까지 만들 수 있는지 확인
################################
# 주어 진 동전 단위로 만들 수 없는 금액을 만들 때 효율적이다
# target을 만들 수 있으면, target에 배열의 원소를 더해가며 새로운 target 전까지 만들 수 있는 지 확인 
n = int(input())
ls = list(map(int,input().split()))
ls.sort()
target = 1

for penny in ls:
    if target < penny:
        break
    target+=penny
print(target)

#################################################################################################################
# 가장 큰 정사각형
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
##########################################################################################################################
################################
# 이진 트리 작성
################################
## 관련 문제 2019 카카오 코테 - 길 찾기 게임.py
class Node:
    # 노드 생성자
    def __init__(self,node):
        self.head = node
    # 트리에 추가
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break        
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
############################################################################################
##################
# n진수 구하기
##################
notation = '0123456789ABCDEF'
def turnToStr(num,base):
    q,r = divmod(num,base)
    n = notation[r]
    return turnToStr(q,base) + n if q else n 
###############################################################################
#################################
# 다익스트라 최소 사이클 거리 구하기
#################################
v,e = map(int, input().split())
graph = [[int(1e9)]*(v+1) for _ in range(v+1)]

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a][b] = c
for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
# 가장 작은 사이클을 찾는 for문
_min = int(1e9)
for i in range(1,v+1):
    _min = min(_min,graph[i][i])
if _min == int(1e9):
    print(-1)
else:
    print(_min)
######################################################################