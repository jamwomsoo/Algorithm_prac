import heapq
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
sum_value = 0
for i in arr:
    sum_value+=i
    result+=sum_value
print(result)
