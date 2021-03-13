n = int(input())
arr= []
for i in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])
arr = sorted(arr, key = lambda x : (x[0],x[1]))
#print(arr)
start = arr[0][0]
end = arr[0][1]
cnt = 1

for i in range(1,len(arr)):
    if start<arr[i][0] and end>arr[i][1]:
        if end - start >= arr[i][1] - arr[i][0]:
            start = arr[i][0]
            end = arr[i][1]
            #print("s",start,end)
    elif end == arr[i][0] and arr[i][0]== arr[i][1]:
        start = arr[i][0]
        end  = arr[i][0]
        cnt+=1

    elif end <= arr[i][0]:
        cnt+=1
        start = arr[i][0]
        end = arr[i][1]
        #print("s",start,end)
print(cnt)