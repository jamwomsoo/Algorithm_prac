import sys
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
tmp = float('inf')
ans = [0]*3

for i in range(n-2):
    if i > 0 and arr[i] == arr[i -1]:
        continue
    left = i+1
    right = n-1
    while left < right:
        now = arr[left] + arr[i] + arr[right]
        if abs(now)<abs(tmp):
            tmp = now
            ans[0] = arr[i]
            ans[1] = arr[left]
            ans[2] = arr[right]
        if now > 0:
            right-=1
        elif now < 0:
            left+=1
        else:          
            print(arr[i],arr[left],arr[right])
            sys.exit(0)
for i in ans:
    print(i,end = ' ')