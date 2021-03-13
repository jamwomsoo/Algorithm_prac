n = int(input())
arr = list(map(int, input().split()))
max_index = arr.index(max(arr))
result=0
for i in range(max_index+1,n):
    result+=(arr[max_index]+arr[i])
for i in range(0,max_index):
    result+=(arr[max_index]+arr[i])
print(result)