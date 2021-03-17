for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    new_arr = []
    new_arr.append(arr[0])
    for i in range(1,n):
        if new_arr[-1][1] > arr[i][1]:
            new_arr.append(arr[i])
        
    #print(new_arr)
    #print(arr)
    print(len(new_arr))