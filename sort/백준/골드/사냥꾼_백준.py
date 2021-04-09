import bisect
import heapq
from copy import deepcopy
m,n,l = map(int, input().split())
hunters = sorted(list(map(int, input().split())))
ans = 0
# 이 문제는 동물을 기준으로 구하게 되면 선형 탐색으로 시간 초과가 뜨기 때문에
# 사냥꾼을 기준으로 이진탐색을 해준다.
# 
# 이진 탐색 시 lower_bound를 찾는다
#      (lower_bound-1)  (*)          (lower_bound)
# 위와 같이 lower_bound가 그 전에 있던 것 보다 *에 멀리 있을 수 있다
# 그래서 lower_bound와 그 전 것 중 더 길이가 짧은 것을 선택해서 사냥한다

def func(animal):
    l ,r = 0,len(hunters)-1
    while l<r:
        mid = (l+r) //2
        if hunters[mid]<animal:
            l = mid+1
        else:
            r = mid
    if l>0:
        if abs(animal - hunters[l - 1]) < abs(animal - hunters[l]):
            return hunters[l-1]
        else:
            return hunters[l]
    return hunters[l]
for i in range(n):
    a,b = map(int, input().split())

    p = func(a)

    if abs(p-a)+b<=l:
        ans+=1

print(ans)
