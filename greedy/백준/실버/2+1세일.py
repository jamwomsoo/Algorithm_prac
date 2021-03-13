n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse = True)
result=0
for i in range(0,n):
    if (i+1)%3 == 0:
        continue

    result+=arr[i]
print(result)