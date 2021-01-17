n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n-2,-1,-1):
    #print(i)
    for j in range(len(arr[i])):
        #왼쪽(바로 아래)
        left = arr[i+1][j]
        #오른쪽(아래 오른쪽)
        right = arr[i+1][j+1]
        #print(left,right)
        arr[i][j] = arr[i][j] + max(left,right)
        #print(arr[i][j])
print(arr[0][0])
        