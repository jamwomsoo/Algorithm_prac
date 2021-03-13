n = int(input())
arr = [int(input()) for _ in range(n)]
max_value = arr[-1]
ans = 0
for i in range(n-2,-1,-1):

    if max_value <= arr[i]:
        ans += abs(max_value-arr[i]) + 1
        max_value -=1 
    else:
        max_value = arr[i] 

print(ans)