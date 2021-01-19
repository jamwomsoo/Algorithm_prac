t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    arr = [0]*(n+1)
    q = []
    for i in range(m):
        q.append(list(map(int, input().split())))
    q = sorted(q,key = lambda x : (x[1],x[0]))
    #print(q,n)
    for i in q:
        a,b = i
        #print(arr,a,b+1)
        if n == 0:            
            break
        for j in range(a,b+1):
            #print(arr[j] == 0)
            if arr[j] == 0:
                arr[j] = 1
                n-=1
                break
            # if 0 in arr[a:b+1]:
        #     arr[arr[a:b+1].index(0) + a] = 1
        #     n-=1
    print(len(arr)-1 - n)   
    

