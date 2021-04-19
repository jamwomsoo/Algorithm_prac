# https://www.acmicpc.net/problem/2812
# 틀림
# stack이용
# 스텍에 하나씩 arr의 값을 넣어줄때
# 스택의 top 값과 arr[i]값을 비교했을때
# top값이 더 작을 경우 제거해준다
# 더 클경우 뒤에 arr[i]값을 추가해준다 
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