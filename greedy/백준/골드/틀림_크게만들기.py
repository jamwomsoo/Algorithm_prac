# https://www.acmicpc.net/problem/2812
# 틀림

# stack이용
# 스텍에 하나씩 arr의 값을 넣어줄때
# 스택의 top 값과 arr[i]값을 비교했을때
# top값이 더 작을 경우 제거해준다
# 더 클경우 뒤에 arr[i]값을 추가해준다 

# 해설
# 1. stack인 result(정답)를 만들어준다
# 2. n자리 숫자를 하나씩 돌아준다
#   2-1. result에 차례가 올때마다 한 개씩 넣어준다
#   2-2. result의 가장 최에 들어온값(top)과 현재 숫자의 자리수의 수를 비교해 result가 더 작으면 result top값을 제거한다
#   2-3. 현재 숫자의 자리수에 있는 값을 result top에 넣어준다
n,k = map(int, input().split())
arr = list(map(int, input()))

result = []
delnum = 0
for i in range(n):
    while delnum<k and result:
        if result[-1] < arr[i]:
            result.pop()
            delnum+=1
        else:
            break
    result.append(arr[i])
for i in range(n-k):
    print(result[i],end = "")