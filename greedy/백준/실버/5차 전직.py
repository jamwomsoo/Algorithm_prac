n,k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
_open = 0
result = 0
for i in arr:
    result+=_open*i
    if _open<k:
        _open+=1
print(result)