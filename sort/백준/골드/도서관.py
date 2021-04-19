# https://www.acmicpc.net/problem/1461
# 틀림
# 참고
# https://jainn.tistory.com/38
# 함수의 양수,음수를 따로 나눠서 배열로 만든다
# 배열을 m개씩 끊어줘야한다
# 배열을 m개씩 끊을때 m보다 작을 수 도 있다 -> 그만큼 담는다
# 끊어놓은것 들중에서 걸음을 최소로 하려면 맨 마지막 제일 멀리 있는 곳은 돌아올 필요가 없으므로 *2를 하지 않는다
# 제일 멀리 있는 것들 빼고 전부 왔다가 다시 가야 하므로 *2 씩해준다
n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
plus = []
minus = []
for i in arr:
    if i>0:
        plus.append(i)
    else:
        minus.append(abs(i))
plus.sort(reverse=True); minus.sort(reverse=True)
result = []


for i in range(len(plus)//m):
    result.append(plus[i*m])
if len(plus)%m > 0:
    result.append(plus[(len(plus)//m)*m])

for i in range(len(minus)//m):
    result.append(minus[i*m])
if len(minus)%m>0:
    # (len(minus)//m)*m -> m개보다 작을때 항상 맨앞을 가리킨다
    result.append(minus[(len(minus)//m)*m])
ans = 0

result.sort()

ans+=result.pop()
ans+=sum(result)*2
print(ans)

