import sys
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
tmp = sys.maxsize
ans = [0]*3

for i in range(n-2):
    left = i+1
    right = n-1
    while left < right:
        now = arr[left] + arr[i] + arr[right]
        if abs(now)<tmp:
            tmp = abs(now)
            ans = [arr[i],arr[left],arr[right]]
        if now > 0:
            right-=1
        elif now <0:
            left+=1
        else:
            ans = [arr[i],arr[left],arr[right]]
            print(*sorted(ans))
            exit()
    
print(*sorted(ans))