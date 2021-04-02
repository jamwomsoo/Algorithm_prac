def solution(records):
    answer = []
    dic = {}
    for index, record in enumerate(records):
        tmp = record.split(' ')
        if tmp[0] == 'Enter':

            dic[tmp[1]] = tmp[2]
            answer.append([tmp[1],'님이 들어왔습니다.'])
        elif tmp[0] == 'Leave':
            answer.append([tmp[1],'님이 나갔습니다.'])
        elif tmp[0] == 'Change':
             if dic[tmp[1]]:
                dic[tmp[1]] = tmp[2]

    for index, arr in enumerate(answer):
        
        answer[index] = str(dic[arr[0]])+str(arr[1])
    return answer