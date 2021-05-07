# 문제 https://kdgt-programmer.tistory.com/65
# 참고 사이트 https://kdgt-programmer.tistory.com/65
# 투포인트 binary_search 방식
# left, right 포인터를 시작점에 두고 시작한다
# 현재까지의 범위 중에 gems의 종류가 다 한개 이상씩 있으면 현재 범위와 목표를 비교
# left를 한칸 옆으로 이동한다
# 만약 gems의 종류가 한개 미만인게 있으면 right를 옮긴다

def solution(gems):
    answer = []
    size = len(set(gems))
    dic = {gems[0]:1}
    tmp = [0,len(gems)-1]
    left,right = 0,0

    while left<len(gems) and right < len(gems):
        if len(dic) == size:
            if right - left < tmp[1] - tmp[0]:
                tmp = [left,right] 
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else: 
                dic[gems[left]] -=1
            left+=1
        else:
            right +=1
            if right == len(gems): break
            if gems[right] in dic.keys():
                dic[gems[right]]+=1
            else:
                dic[gems[right]] = 1
    return [tmp[0]+1,tmp[1]+1]

print(solution(["AA", "AB", "AC", "AA", "AC"]))