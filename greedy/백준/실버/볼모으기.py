# https://www.acmicpc.net/problem/17615
# 4가지 방법으로 나누어서 풀어야 된다
# 빨간색이 모이는 방법
# 1. 빨간색을 움직여서 왼쪽에 빨간색이 모이는 방법
# 2. 빨간색을 움직여서 오른쪽에 빨산색이 모이는 방법
# 파란색이 모이는 방법
# 3. 파란색을 움직여서 왼쪽에 파란색이 모이는 방법
# 4. 파란색을 움직여서 오른쪽에 파란색이 모이는 방법
n= int(input())
arr = list(map(str, input()))
result = int(1e9)
# 빨강
# 왼쪽에서부터 시작해서
# 빨간색을 움직여서 왼쪽에 빨간색이 모이는 방법
cnt=0
check = 0
for i in range(n):
    if arr[i] == 'B': check = 1
    if check and arr[i] =='R': cnt+=1
result = min(result,cnt)
# 빨간색을 움직여서 오른쪽에 빨간색이 모이는 방법
cnt = check = 0
for i in range(n-1,-1,-1):
    if arr[i] == 'B': check=1
    if check and arr[i] =='R': cnt+=1
result = min(result,cnt)
# 파란색
# 왼쪽부터 시작
# 파란색을 움직여서 왼쪽에 파란색이 모이는 방법
cnt = check = 0
for i in range(n):
    if arr[i] == 'R': check = 1
    if check and arr[i] =='B': cnt+=1
result = min(result,cnt)
# 파란색을 움직여서 오른쪽에 파란색이 모이는 방법
cnt = check = 0
for i in range(n-1,-1,-1):
    if arr[i] == 'R': check=1
    if check and arr[i] =='B': cnt+=1
result = min(result,cnt)
print(result)