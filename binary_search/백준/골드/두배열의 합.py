# 전혀 모르겠네,,,
# 백준 사이트 https://www.acmicpc.net/problem/2143
# 참고 사이트 https://velog.io/@nyanyanyong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98python%EB%B0%B1%EC%A4%80-2143%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9
# 풀이
# a 배열의 부분 배열의 합을 key로 하고 경우의수를 Value로 하는 dictionary를 만든다
# t에서 b 배열의 부분 배열의 합을 빼준 key 값을 갖는 dict의 경우의 수를 답에 더해준다
# -> 별로 이진 탐색 문제가 아닌 것 같다
from collections import defaultdict
t = int(input())
n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int, input().split()))
dicA = defaultdict(int)
ans = 0
for i in range(n):
    for j in range(i, n, 1):
        dicA[sum(a[i:j+1])] += 1

for i in range(m):
    for j in range(i, m, 1):
        ans += dicA[t - sum(b[i:j+1])]
print(ans)