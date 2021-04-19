n = int(input())
arr = str(input())
count = arr.count('LL')
# 만약 커플석이 0개 혹은 1개일때
# 0: *s, *s*s
# 1: *s*ll*s*, *s*s*ll* 
if count<=1:
    print(n)
# 2: *s*ll*[l]l*,*s*ll*[s]*ll* 2명일때 -1
# 3: *ll*[l]l*[l]l*             3명일때 -2
else:
    print(n-count+1)
