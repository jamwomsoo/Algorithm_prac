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

###########
#정답지 해설
###########
# def solution(s):

#     answer = len(s)
#     for step in range(1,len(s)//2+1):
#         compressed = ''
#         cnt = 1
#         #앞에서 step개 만큼 추출
#         prev = s[0:step]
#         for j in range(step, range(s),step):
#             if prev == s[j:j+step]:
#                 cnt+=1
#             else:
#                 compressed += str(cnt) + prev if cnt>=2 else prev
#                 prev = [j:j+step]
#                 cnt=1
#         # 남아있는 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
#         compressed += str(cnt) + prev if cnt>=2 else prev
#         # 만들어지는 압축 문자열이 가장 짧은 것이 정답
#         answer = min(answer, len(compressed))
#     return answer




