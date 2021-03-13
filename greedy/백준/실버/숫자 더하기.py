while True:
    arr = list(map(int, input().split()))
    n= arr[0]
    if n == 0 and len(arr) == 1:
        break
    arr = sorted(arr[1:])
    ls1 = ''
    ls2 = ''
    #print(arr)
    for i in range(n):
        if arr[i] != 0:
            s1 = str(arr[i])
            s2 = str(arr[i+1])
            arr.remove(arr[i+1])
            arr.remove(arr[i])
            break
    cnt = 0
    flag = True
    for i in range(n):
        if not arr:
            break
        if i%2 == 0:
            ls1,ls2 = ls2,ls1
        if i%2==0:
            ls1=str(arr.pop())+ls1
        else:
            ls2 = str(arr.pop())+ls2
    if len(ls1)>len(ls2):
        ls1 = s1 + ls1
        ls2 = s2 + ls2
    elif len(ls2)>len(ls1):
        ls1 = s2 + ls1
        ls2 = s1 + ls2
    
    elif int(ls1) > int(ls2):
        ls1 = s1 + ls1
        ls2 = s2 + ls2
    elif int(ls2) <= int(ls2):
        ls1 = s2 + ls1
        ls2 = s1 + ls2  
    #print("ls",ls1,ls2)
    result = int(ls1) + int(ls2)    
    print(result)
