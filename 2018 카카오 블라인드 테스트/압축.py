from string import ascii_uppercase
def solution(msg):
    answer = []
    dic ={}
    
    for i in range(len(ascii_uppercase)):
        dic[ascii_uppercase[i]] = i+1
    #print(dic.keys())
    index = 27
    while msg:
        w_len = 1
        for _len in range(1,len(msg)+1):
            print('msg[:_len]',msg[:_len])
            if msg[:_len] not in dic.keys():
                
                break
            else: w_len = _len
        #print('w_len',w_len,msg)
        # if w_len-1 == 0:
        #     if msg[:w_len] in dic.keys():
        #         answer.append(dic[msg[:w_len]])
        #         break
        #print(msg[:w_len])  
       
        answer.append(dic[msg[:w_len]])
        dic[msg[:w_len+1]] = index
        index+=1
        msg = msg[w_len:]
        
    #print(dic)

    return answer
print(solution('KAKAO'))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
#print(solution("ABABABABABABABAB"))