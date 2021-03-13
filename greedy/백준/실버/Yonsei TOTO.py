n,m = map(int, input().split())
arr = []
result = 0
for i in range(n):
    p,l = map(int,input().split())
    tmp = list(map(int,input().split()))
    if p<l:
        if m>=1:
            result+=1
            m-=1
        continue
    
    tmp.sort(reverse=True)
    arr.append(tmp[l-1])
arr.sort()
#print(arr)
for i in arr:
    if i<=m:
        m-=i
        result+=1
    else:
        break
print(result)