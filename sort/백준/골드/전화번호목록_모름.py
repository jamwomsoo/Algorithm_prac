# https://www.acmicpc.net/problem/5052
# 정렬을 했기때문에 앞에 있는 것과 접두사를 비교하는 것만으로도 문제의 답이 나올 수 있다
import re
for _ in range(int(input())):
    n = int(input())
    arr = [str(input()) for _ in range(n)]
    arr.sort()
    flag = False
    for i in range(n-1):
        if re.match(arr[i], arr[i+1]):
            flag = True
            break
    if flag:
        print('NO')
    else:
        print('YES')
    