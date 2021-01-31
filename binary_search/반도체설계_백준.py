# 가장 긴 증가하는 수열 문제(LIS)
# 기존의 LIS문제는 O(N*N)문제이다
# 해당 문제의 범위는 4000이기때문에 안된다
# 그렇기 때문에 lower_bound를 이용한 LIS를 사용해야 한다
# 참고 사이트 https://seungkwan.tistory.com/8
import bisect
n = int(input())
arr = list(map(int, input().split()))
q = []
for d in arr:
    if not q or q[-1]<d:
        q.append(d)
    else:
        q[bisect.bisect_left(q,d)] = d
print(len(q))
