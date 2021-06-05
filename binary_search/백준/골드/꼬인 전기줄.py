# 모름
# 백준 사이트 : https://li-fo.tistory.com/50
# 해설 사이트 : https://li-fo.tistory.com/50
# LIS (가장긴 증가하는 수열 문제)
# 하지만 bisect_Left 를 사용하면 Index에러가 발생하기 때문에
# lower_bound 함수를 사용해야 한다

N = int(input())
#arr = [int(1e9)]
arr=list(map(int, input().split()))

dp = []
ans = 0
def lower_bound(s,e,v):
    while s<e:
        m = (s+e)//2
        if dp[m] < v:
            s = m+1
        else:
            e = m
    return e

for ele in arr:
    if not dp or dp[-1] < ele:
        dp.append(ele)
    else:
        index = lower_bound(0,len(dp),ele)
        dp[index] = ele

print(N-len(dp))


