import bisect
n = int(input())
arr= [int(input()) for _ in range(n)]
max_value = max(arr)
cnt = 1
start = arr.index(max_value)
for i in range(start-1,-1,-1):
    if arr[i] == max_value-1:
        max_value -=1
        cnt+=1

print(n-cnt)
    