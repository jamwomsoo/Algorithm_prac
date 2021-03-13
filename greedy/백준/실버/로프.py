n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
result = 0
while arr:
    tmp = arr.pop(0)*n
    result = max(tmp,result)
    n-=1
print(result)
