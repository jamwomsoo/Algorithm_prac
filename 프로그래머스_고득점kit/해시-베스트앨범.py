import operator
def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}
    for i in range(len(genres)):
        if genres[i] not in dic1.keys():
            dic1[genres[i]] = []
            dic1[genres[i]].append([plays[i],i])
        else:
            dic1[genres[i]].append([plays[i],i])
        if genres[i] not in dic2.keys():
            dic2[genres[i]] = plays[i]
        else:
            dic2[genres[i]] += plays[i]
    for d in dic1:
        dic1[d].sort(key= lambda x : (-x[0],x[1]))
    dic2 = sorted(dic2.items(), key = lambda item: item[1],reverse= True)

    for key, value in dic2:
        for cnt,index in dic1[key][:2]:
            answer.append(index)
    # 위와 동일
    # dic2 = sorted(dic2.items(), key = operator.itemgetter(0),reverse= True)
  
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))