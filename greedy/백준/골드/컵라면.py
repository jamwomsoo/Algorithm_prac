#그리디 문제 중 과제(골드)와 유사한 스타일의 문제이다

import heapq
N = int(input())
q = []
day = [0]*(N+1)
for i in range(N):
    dead,cup = map(int,input().split())
    heapq.heappush(q,[(-cup),dead])
ans = 0

while q:
    cup_ramun, deadline = heapq.heappop(q)
    cup_ramun =-cup_ramun
   
    for i in range(deadline,0,-1):
        if day[i] == 0:
            day[i] = cup_ramun
            ans+=cup_ramun
            break

print(ans)
