def check_proper(p):
    checker = 0
    for i in p:
        if checker < 0:
            return False
        if i == '(':
            checker+=1
        elif i ==')':
            checker-=1

    return True
def balance_index(p):
    c=0
    for i in range(len(p)):
        if p[i] == '(':
            c+=1
        elif p[i] ==')':
            c-=1
        if c == 0:
            return i
def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balance_index(p)
    u=p[:index+1]
    v=p[index+1:]
    if check_proper(u) == True :
        return u + solution(v)
    elif check_proper(u) == False:
        answer +='(' + solution(v) +')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == ')':
                u[i] = '('
            else:
                u[i]= ')'
        answer += ''.join(u)        

    return answer
    



print(solution("()))((()"))