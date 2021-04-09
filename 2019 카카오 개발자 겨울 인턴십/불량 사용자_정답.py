from itertools import permutations
def isMatch(user_set, ban_set):
    for i in range(len(user_set)):
        # 만약 길이가 맞지 않으면 거짓
        if len(user_set[i]) != len(ban_set[i]):return False
        for j in range(len(ban_set[i])):
            if ban_set[i][j] =='*': continue
            # 만약 같은 순서에 있는 아이디들간 틀린 문자가 있으면 거짓
            if ban_set[i][j] != user_set[i][j]: return False
    return True
def solution(user_id,banned_id):
    answer=[]
    # 순열로하면 모든 경우의 수가 나오기 때문에 순서에 banned_ID와 user_id 각각의 아이디들의 순서를 신경쓰지 
    # 않아도 된다
    for per in permutations(user_id,len(banned_id)):
        if isMatch(per, banned_id):
            com_set = set(per)
            # 만약 answer에 com_set이 없으면 넣어준다
            if com_set not in answer:
                answer.append(com_set)

    return len(answer)