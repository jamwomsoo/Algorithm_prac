# def solution(N, stages):
#     answer = []
    
#     ls = [0]*(N+2)
#     stages.sort()
#     for i in stages:
#         ls[i] +=1
#     lenght = len(stages)
#     for i in range(1,N+2):
#         if ls[i] !=0:
#             answer.append((float(ls[i])/float(lenght),i))
#         else:
#             answer.append((0,i))    
#         lenght -=ls[i]
    
#     answer = sorted(answer ,key =lambda x: (-x[0],x[1]))
#     result=[]
#     for i in range(0,len(answer)):
#         if answer[i][1] != N+1:
#             result.append(answer[i][1])

#     return result
def solution(n,stages):
    cnt = 0
    length = len(stages)
    answer=[]
    for i in range(1,n+1):
        cnt = stages.count(i)
        if cnt == 0:
            fail=0
        else:
            fail = float(cnt)/float(length)
        answer.append((fail,i))
        length -= cnt
    answer = sorted(answer,key = lambda x: x[0],reverse=True)
    # result = []
    # for i in range(len(answer)):
    #     result.append(answer[i][1])
    answer = [i[1] for i in answer]
    return answer
print(solution(4,[4,4,4,4,4]))