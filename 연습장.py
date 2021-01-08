import heapq
def solution(s):
    s = list(s)
    q=[]
    
    for num in range(1,len(s)//2+1):
        cnt=1
        new_ls=[]
        for j in range(0,len(s),num):
            #print(j)
            #print(s[j:j+num],s[j+num:(j+num)+num])
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
        #print(new_ls)
        heapq.heappush(q,(len(new_ls)))
    if len(s) == 1:
        return 1
    return heapq.heappop(q)

print(solution('a'))