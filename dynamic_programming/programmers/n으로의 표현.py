# 1. 5를 1번 사용해서 만들 수 있는 수 : 5
# 2. 5를 2번 사용해서 만들 수 있는 수
#   -1. 5를 연속으로 이어붙인 수: 55
#   -2. 1set과 1set을 사칙연산한 값들 : 10(5+5), 0(5-5), 1(5//5), 25(5*5)
# 3. 5를 3번 사용하여 만들 수 있는 수 : 
#   -1. 5를 연속으로 이어붙인 수: 555
#   -2. (1set 2set을 사칙연산한 값들)  U (2set과 1set을 사칙연산한 값들):
# .........5를 8번 사용해서 만들 수 있는 수까지
def solution(N, number):
    answer = 0
    if N == number: return 1

    s = [ set() for _ in range(8)]
    for i,x in enumerate(s,start=1):
        x.add(int(str(N)*i))
    # -> set이 8개 가 있는 s 리스트가 생성됨에 따라 1번사용은 0번 인덱스부터
    print(s)
    for i in range(1,8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i+1
            break
    else:
        answer = -1

    return answer

print(solution(5,12))
print(solution(2,11))