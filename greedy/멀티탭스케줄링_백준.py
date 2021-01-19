n ,k = map(int, input().split())
use_ls = list(map(int, input().split()))

multitap = [0]*n

cnt = 0

if len(multitap) < k:
    for i in range(len(multitap)):
        if use_ls[i] in multitap:
            continue
        multitap[i] = use_ls[i]
    #print(multitap)
    for now in range(n,len(use_ls)):
        
        #print("muti ",multitap)
        check = [int(1e9)]*n
        #print("now use_ls ",now, use_ls[now])
    
        if use_ls[now] not in multitap:
            if 0 in multitap:
                multitap[multitap.index(0)] = use_ls[now]
                continue
            for i in range(n):
                content = multitap[i]
                if content in use_ls[now:len(use_ls)]:
                    #check[i] = int()
                    check[i] = use_ls[now:len(use_ls)].index(content)
            index = check.index(max(check))
            multitap[index] = use_ls[now]
            cnt+=1
            #print(multitap,check)
            
print(cnt)
