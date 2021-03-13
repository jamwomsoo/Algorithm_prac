n = int(input())
arr = list(map(int, input().split()))
max_value=-int(1e9)
for i in range(n):
    stack = 0
  
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            break
        if arr[i]>arr[j]:
            stack+=1
    max_value = max(max_value,stack)
    
    

print(max_value)