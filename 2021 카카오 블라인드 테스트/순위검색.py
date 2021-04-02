
# 언어 cpp, java, python 중 택 1
# back, front 중 택 1
# 지원 경력구분 항목 junier senior 중 택 1
# chicken, pizza 중 택 1
# 코테점수
# -> info 배열에 담김
# query 순서 언어, 직군, 경력, 소울 푸드,  점수
def solution(info, query):
    n = len(query)
    answer = [0]*n
    #print(len(query))
    for index, q in enumerate(query):
        tmp = list(map(str, q.split(' ')))
        tmp = [i for i in tmp if i != 'and']
        query[index] = tmp
    
    for i_index, _info in enumerate(info):    
        tmp = list(map(str,_info.split(' '))) 
        info[i_index]=tmp
    #print("info\n",info)
    #print("query\n",query)
    for q_index,q in enumerate(query):
        #print("qqqqqqqqqqqq",q)
        for _info in info:
            #print(_info,q)
            flag = True
            for zip_index,_zip in enumerate(zip(q,_info)):
                
                if _zip[0] == '-': pass
                elif zip_index == 4 and int(_zip[0]) > int(_zip[1]):
                    flag = False
                    break
                elif zip_index < 4 and _zip[0] != _zip[1]: 
                    flag = False
                    break
            
            if flag:
                #print(_info)
                answer[q_index]+=1

    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],\
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))