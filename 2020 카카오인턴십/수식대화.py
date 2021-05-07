from itertools import permutations
from copy import deepcopy
def solution(expression):
    operator = set()
    #pers = permutations(['*','-','+'],3)
    answer = 0
    start = 0
    arr = []
    for i in range(len(expression)):
        if not expression[i].isalnum():
            arr.append(expression[start:i])
            arr.append(expression[i])
            start = i+1
            operator.add(expression[i])
    arr.append(expression[start:])
    #print(operator)
    pers = permutations(operator,len(operator))
    #print(arr)
    for per in pers:
        tmp = deepcopy(arr)
        while len(tmp) >1:
            for ele in per:
                if ele in tmp:
                    index = tmp.index(ele)
                    if index == 0 :
                        tmp = [(tmp[0]+tmp[1])] +tmp[2:]
                        break
                    st = int(eval(tmp[index-1] + tmp[index] + tmp[index+1]))

                    if st < 0:
                        #print(tmp[index-2],index-2)
                        if tmp[index-2] == '-' or tmp[index-2] == '+' or tmp[index-2] == '*':
                            tt = [str(st)]
                        else:
                            tt = ['-',str(abs(st))]
                    else:
                        tt = [str(st)]
                    tmp = tmp[:index-1] + tt + tmp[index+2:]
                    #print("ing",tmp)
                    break
                    
        #print("result",tmp)
        answer = max(answer,abs(int(tmp[0])))
    return answer
print(solution("2-990-5+2"))
print(solution("50*6-3*2"))
print(solution("100-200*300-500+20"))