n = int(input())
arr= list(map(int, input().split()))
arr.sort()
print(arr)
target = 1
for i in arr:
    print(i, target)
    if target < i:
        break
    target+=i 
print(target)