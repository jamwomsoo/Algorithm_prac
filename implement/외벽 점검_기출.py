######################################
# 원형으로 나열된 데이터 처리의 경우 TIP
######################################
# 길이를 2배로 늘려서 '원형'을 일자 형태로 만드는 작업을 해주면 유리하다
from itertools import permutations
def solution(n ,weak, dist):
    answer = len(dist)+1
    length = len(weak)
    weak.extend([i+n for i in weak])
    #  
    for start in range(length):
        # 친구들이 한시간에 움직일 수 있는 거리의 배열의 순열을 구한다(완전탐색)  
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 점검에 참여하는 친구의 수 
            position = weak[start] + friends[count - 1] # 그 친구가 출발해서 1시간 동안 움직 일 수 있는 거리
            for index in range(start, start + length):
                # 1시간 동안 점검했지만 점검 못 한 부분이 남았다면
                if position <weak[index]:
                    count+=1 # 친구를 한명 더 투입
                    # 더 이상 친구를 투입 할 수 없으면 그만함
                    if count > len(dist):
                        break
                    # 점검 못한 부분부터 해당 친구가 1시간동안 점검할 수 있는 마지막 거리
                    position = weak[index] + friends[count-1]
            answer = min(answer,count)
    # 친구를 다 투입했는데 점검 못 한 부분이 있을때 -1을 리턴
    if answer > len(dist):
        return -1
    return answer

#print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))    