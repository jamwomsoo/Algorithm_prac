notation = '0123456789ABCDEF'
def turnToStr(num,base):
    q,r = divmod(num,base)
    n = notation[r]
    return turnToStr(q,base) + n if q else n 

def solution(n, t, m, p):
    answer = ''
    i = 0
    result = ''
    p -=1
    while True:
        _len = len(answer)
        if len(result) >= t:
            break
        if p > _len-1:
            pass
        elif p <= _len-1 :
            result+=answer[p]
            p+=m
        answer += turnToStr(i,n)
        i+=1
    return result
print(solution(2,4,2,1))
print(solution(16,16,2,1))