# 못품
# 백준 사이트 : https://www.acmicpc.net/problem/1107
# 정답 사이트 : https://javaiyagi.tistory.com/585

# 100만 채널 순회 필요
# 최대 이용 가능 채널은 50만인데 100만을 순회하는 이유:
# => +와 -일때의 최적을 모두 고려하기때문이다.
# 예) 500000 채널에 접근하고 싶을때 [1,2,3,5]이면
#     60만에서 -를 사용해서 50만에 접근하는 경우, 
#     40만에서 +를 사용해서 50만에 접근하는 경우를 고려해야한다

n = int(input())
m = int(input())
use = {i for i in range(10)}
if m>0: use -= set(map(int,input().split()))
currnet_channel = 100
ans = abs(n - 100)
for channel in range(1000001):
    for  i in range(len(str(channel))):
        if int(str(channel)[i]) not in use:
            break
        elif len(str(channel)) - 1 == i:
            ans = min(ans, abs(channel - n) + len(str(channel)))
print(ans)

