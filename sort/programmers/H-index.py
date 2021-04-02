def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    while True:
        
        cnt = 0
        for i in range(n):
            if answer <= citations[i]:
                cnt+=1
       # print("cnt,answer",cnt,answer)
        if cnt>=answer:
            answer+=1
        else:
            answer-=1
            break            
    return answer
print(solution([3, 0, 6, 1, 5]))
print(solution([4, 0, 6, 1, 5]))
print(solution([0,0,2,3]))