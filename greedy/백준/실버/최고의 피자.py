# 1원당 열량이 가장 높은 피자
# n개의 토핑, 같은 토핑 2개 이상 선택 불가, 0개 선택 불가
# 도우가격 A원 토핑 가격 모두 b원, 토핑 종류 k개
n = int(input())
dow,toping = map(int, input().split())
dow_kcal = int(input())
toping_kcal = [int(input()) for _ in range(n)]
toping_kcal.sort(reverse=True)
max_value = -int(1e9)
for i in range(n+1):
    kcal = (dow_kcal+sum(toping_kcal[:i]))//(dow+toping*i)
    max_value = max(max_value,kcal)
print(max_value)
