import bisect
n = int(input())
arr = list(map(int, input().split()))
dp = []
for i in arr:
    if not dp or dp[-1]<i:
        dp.append(i)
    else:
        index = bisect.bisect_left(dp,i)
        dp[index] = i
print(len(dp)) 