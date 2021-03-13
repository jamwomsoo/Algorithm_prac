n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(m):
    a = arr[0]
    b = arr[1]
    arr[0] = arr[1] = a+b
    arr.sort()

print(sum(arr))