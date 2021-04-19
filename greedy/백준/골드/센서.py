# 행복어린이집문제와 완전 유사
from itertools import combinations
n= int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수
arr = list(map(int, input().split()))
#s = list(set(sorted(arr)))
arr.sort()
gap = []
for i in range(n-1):
    gap.append(arr[i+1]-arr[i])
gap.sort()
print(sum(gap[:n-k]))
    