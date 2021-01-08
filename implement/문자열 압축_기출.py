import heapq
def solution(s):
    s = list(s)
    q=[]
    if len(s) == 1:
        return 1
    for num in range(1,len(s)//2+1):
        cnt=1
        new_ls=[]
        for j in range(0,len(s),num):
            if s[j:j+num] == s[j+num:(j+num)+num]:
                if  j!=len(s)-1: 
                    cnt+=1
            else:
                if cnt > 1:
                    new_ls.extend(list(str(cnt)))
                    cnt=1
                new_ls.extend(s[j:j+num])
        if j+num < len(s):
            new_ls.extend(s[j+1:])
        heapq.heappush(q,(len(new_ls)))
    
    return heapq.heappop(q)