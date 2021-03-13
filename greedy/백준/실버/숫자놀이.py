for _ in range(int(input())):
    n = int(input())
    cnt = 0
    check = True
    if 1<=n<=9:
        print(1)
        continue
    while n>0:
        
        flag = False
        for i in range(9,2,-1):
            
            if n%i == 0:
                flag = True
                n = n//i
                cnt+=1
                if 0<=n<=9:
                    cnt+=1
                    n=0
                break
        if not flag:
            check = False
            break
    if not check:
        print(-1)
        continue
    print(cnt)
