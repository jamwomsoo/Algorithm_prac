n = int(input())
arr = list(map(int, input().split()))

for i in range(n-2,-1,-1):
    j = i+1
    while True:
        if j ==n-1 or arr[j]!=0:
            break
        else:
            j+=1
    if arr[j]<=arr[i]:
        arr[j] = arr[i]
        arr[i] = 0
result =0
for i in range(n):
    if arr[i]!= 0:
        result+=1
print(result)
