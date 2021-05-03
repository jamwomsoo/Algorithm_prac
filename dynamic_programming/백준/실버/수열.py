from bisect import bisect_left,bisect_right

n = int(input())
arr = list(map(int,input().split()))
dp = []
ans = []
tmp = 0
for ele in arr:
   
    if not dp or dp[-1]<=ele:
        dp.append(ele)
        tmp = max(tmp,len(dp))
    else:
        tmp = max(tmp,len(dp))
        
        dp = [ele]
ans.append(tmp)
arr = arr[::-1]

dp = []
tmp = 0
for ele in arr:
 
    if not dp or dp[-1]<=ele:
        dp.append(ele)
        tmp = max(tmp,len(dp))
    else:
        tmp = max(tmp,len(dp))
   
        dp = [ele]

ans.append(tmp)

print(max(ans))