from itertools import combinations
from collections import defaultdict
# 언어 cpp, java, python 중 택 1
# back, front 중 택 1
# 지원 경력구분 항목 junier senior 중 택 1
# chicken, pizza 중 택 1
# 코테점수
# -> info 배열에 담김
# query 순서 언어, 직군, 경력, 소울 푸드,  점수


 # 푸는 방법
 # info 배열의 한 원소당 0,1,2,3,4개가 '-'일때를 생각하면 한개당 16개씩 나옴
 # 딕셔너리에 모든 경우의 수를 키로 설정해두고 벨류에 코딩테스트 점수를 넣어둔다
 # query도 마찬가지로 선택가능한 부분과 점수 부분을 분리한 후 선택 가능부분에서 '-'를 제거 후 딕셔너리 키에 매칭 시켜본다
 # 해당 키에 연결되어 있는 벨류가 1개 이상이면 그 벨류들과 query의 점수를 비교해서 가능 한 것들의 숫자를 센디
 
def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for _info in info:
        _info = _info.split()
        info_key = _info[:-1]
        info_val = int(_info[-1])
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)
    for key in info_dict.keys():
        info_dict[key].sort()
    for q in query:
        # q = [i for i in q.split(' ') if i !='and']
        q = q.split(' ')
        q_score = int(q[-1])
        q = q[:-1]
        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q)
        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores)>0:
                start, end = 0, len(scores)
                while end>start:
                    mid = (start+end)//2
                    if scores[mid]>=q_score:
                        end = mid
                    else:
                        start = mid+1
                answer.append(len(scores)-start)
        else:
            answer.append(0)
                
    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],\
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))