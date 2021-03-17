arr = [0,1]
def find_index(n):
    index = 0
    while True:
        if n>arr[index]:
            if index == len(arr)-1:
                arr.append(arr[index]+arr[index-1])
            index+=1
        elif n == arr[index]:
            break
        else:
            index-=1
            break
    return index
    
for i in range(int(input())):
    
    n = int(input())
    index = 0
    ans = []
    while n>0:
        index = find_index(n)
        n -= arr[index]
        ans.append(arr[index])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i], end = " ")
    print()