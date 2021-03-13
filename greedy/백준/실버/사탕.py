for _ in range(int(input())):
    j,n = map(int, input().split())
    arr = []
    for i in range(n):
        r,c = map(int, input().split())
        arr.append(r*c)
    arr.sort(reverse= True)
    cnt = 0
    for i in arr:
        if j<=0:
            break
        j-=i
        cnt+=1
    print(cnt)