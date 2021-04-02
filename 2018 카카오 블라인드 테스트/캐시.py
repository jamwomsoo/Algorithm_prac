def increase_time(dic):
    for k in dic.keys():
        dic[k]+=1

def check_time(dic):
    _max = -int(1e9)
    key = 0
    for k,v in dic.items():
        if _max < v:
            _max = v
            key = k
    return key 

def solution(cacheSize, cities):
    answer = 0
    dic = {}
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            answer+=5
            continue
        if len(dic)<cacheSize:
            if city not in dic.keys():
                
                answer+=5
            else:
                answer+=1
            increase_time(dic)
            dic[city] = 1
        elif len(dic)>= cacheSize:
            if city not in dic.keys():
                key = check_time(dic)             
                del dic[key]
                answer+=5
            else:
                answer+=1
            increase_time(dic)
            dic[city] = 1
        #print(answer)
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))