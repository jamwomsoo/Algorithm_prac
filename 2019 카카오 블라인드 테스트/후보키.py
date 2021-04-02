from collections import deque
from itertools import combinations

def solution(relation):
    answer=[]
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    # 1개부터 n개로 되어있는 조합들을 준비한다
    for i in range(1,n_col+1):
        candidates.extend(combinations(range(n_col),i))
    #print(candidates)
    final = []
    # 유일성 확인
    for keys in candidates:
        # 속성들의 조합을 모든 튜플을 돌면서 뽑아내서 더한다

        tmp = [tuple([item[key] for key in keys]) for item in relation]
        # 중복되는 키 값들이 존재하면 set을 통해 제거되므로 길이가 줄어든다
        # 중복 되는 것들은 유일성에 위배되어 더해주지  해당 조합은 않는다
        if len(set(tmp)) == n_row:
            final.append(keys)
    #print(final)
    # 최소성확인
    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            # final[i]길이가 final[i]와 final[j]의 교집합과 길이가 같으면 final[j] 최소성 위배
            # (0,1) (0,1,2,3) -> (0,1) (0,1) 되므로 삭제 
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
    return len(answer)
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))