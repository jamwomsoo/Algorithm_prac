from itertools import combinations

def check_cnt(banned_id,comb):
    cnt = 0
    flag = True
    s =set()
    
    comb = sorted(list(comb))
    
    for ban in banned_id:
        
        for c in comb:
            flag = True
            #print(ban,c)
            if len(c) != len(ban):
                continue
            for j in range(len(ban)):
                #print(ban[j],c[j])
                if ban[j] == '*': pass
                elif ban[j]!=c[j]:
                    flag = False
                    break
            #print("뭐냐",)
            if flag and c not in s:
                s.add(c)
                #print('input')
                break

    #print(comb,s)   
    if len(s) == len(comb):
        return True
    return False
    # for i in range(len(comb)):
    #     for j in range(len(comb[i])):
    #         #print(banned_id[i],comb[i])
            
    #         if banned_id[i][j] == '*':continue 
    #         if banned_id[i][j] != comb[i][j]:
    #             flag =False
    #             break
    #     if not flag:
    #         break
    # if flag: return True
    # return False
def solution(user_id, banned_id):
    answer = 0
    sanctions_id =[]
    n = len(user_id)
    k = len(banned_id)
    combs = list(combinations(user_id,k))
    answer = []
    #print(combs)
    for comb in combs:
        tmp = check_cnt(banned_id,comb)   
        
        #print('comb, ',comb)
         
        #print(tmp)
        if tmp and set(comb) not in answer:
            answer.append(set(comb))
    #print(answer)
  
    return len(answer)
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
print(solution(['found'],['******','*****']))