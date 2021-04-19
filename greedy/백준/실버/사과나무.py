# https://www.acmicpc.net/problem/19539
# 배열의 원소마다 2로 나누었을때 의 몫과 나머지들의 합으로 정답을 알수 있다
# 예) 3 3 3 
#    몫 3 나머지합 3 으로 알맞게 분배 가능
# 예) 1 3 1 3 1
#    몫 2, 나머지합 5로 알맞게 분배 불가능
# 예) 10000 1000 100
#    몫 != 나머지
# -> 이를 통해 알 수 있는 것: 2칸짜리 물뿌리개를 1짜리 2번으로 대체가능
# -> 몫 d,나머지 합 r,2를 1짜리로 대체한 횟수를 x로 둘때
# -> d-x = r + 2x
# -> x = (d-r)/2인것을 알수 있다
import sys
n = int(input())

want = list(map(int, input().split()))
d = 0
r = 0
for i in want:
    d+=i//2
    r+=i%2
if (d-r)%3 == 0 and d>=r:
    print("YES")
else:
    print("NO")