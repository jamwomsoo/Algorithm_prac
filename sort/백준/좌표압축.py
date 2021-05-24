from bisect import bisect_left,bisect_right
n= int(input())
arr = list(map(int, input().split()))
b = list(sorted(set(arr)))

ans = []
for i in range(n):
    t = arr[i]
    index = bisect_left(b,t)
    ans.append(index)
print(*ans)
