n,m =map(int, input().split())
d=[0]*(m+1)

for i in range(n):
d[int(input())] = 1

for i in range(0,m+1):
for j in range(int(i//2)+1):
    if d[j] == 0 or d[i-j]==0:
    continue
    if d[i] == 0 :
    d[i] = d[j]+d[i-j]
    else:
    d[i] = min(d[i],d[j]+d[i-j])
if d[m] == 0:
print(-1)
else:
print(d[m])

#정답풀이
#내가 작성한 코드보다 빠르고 공간 효율 좋음
""" d = [10001]*(m+1)
d[0] = 0
arr=list()
for i in range(n):
    arr.append(int(input()))
    

for i in range(n):
    for j in range(arr[i],m+1):
        if d[j-arr[i]] != 10001:
            d[j] = min(d[j],d[j-arr[i]]+1)
if d[m]!=10001:
    print(d[m])
else:
    print(-1) """

ㄴㄴㄴ
ㄴㄴ