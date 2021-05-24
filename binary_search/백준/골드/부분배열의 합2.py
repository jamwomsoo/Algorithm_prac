# 못품
# 백준 사이트 : https://www.acmicpc.net/problem/1208
# 풀이 사이트 : https://kimkim031.medium.com/boj-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9-2-python-16a85e042816
#  1. 주어진 수열을 반으로 나누면 시간복잔도가 O(2^n/2)이 된다
#  2. 재귀를 사용해 수열을 만들고 합한 값과 개수를 딕셔너리로 저장
#  3. 아무것도 들어있지 않는 부분수열이 나올 수 있으므로 결과값에 -1
from collections import defaultdict

n,s = map(int, input().split())
arr = sorted(list(map(int ,input().split())))
a, b = arr[:n//2], arr[n//2:]
L,R = defaultdict(int),defaultdict(int)

def check(n,li,dic,_sum):
    if n == len(li):
        dic[_sum] +=1
        return
    check(n+1,li,dic,_sum + li[n]) # 해당 값을 선택해서 부분수열에 포함
    check(n+1,li,dic,_sum)         # 해당 값을 선택하지 않음

check(0,a,L,0)
check(0,b,R,0)

res = 0
if s == 0:
    res-=1 #아무 것도 선택하지 않았을 경우를 제거
for l in L:
    if s-l in R:
        res += L[l]*R[s-l]
print(res)

# 다른 풀이
# https://www.acmicpc.net/status?user_id=tjdtn4806&problem_id=1208&from_mine=1
# def dfs(index,end_index,subtotal,direction):
#     global ans 
#     if index == end_index:
#         if direction == "right":
#             ans += left[s-subtotal]
#         else:
#             left[subtotal] += 1
#         return
#     dfs(index+1,end_index,subtotal,direction)
#     dfs(index+1,end_index,subtotal+nums[index],direction)


# ans = 0
# n,s = map(int ,input().split())
# nums = list(map(int, input().split()))
# left = defaultdict(int)

# dfs(0,n//2,0,"left")
# dfs(n//2,n,0,"right")

# print(ans if s != 0 else ans - 1)
