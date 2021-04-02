from itertools import combinations
coms = {}
def solution(orders, course):
    answer = []
    for i, order in enumerate(orders):
        for c in course:
            if len(order)<c: continue
            tmp = list((combinations(order,c)))
            for t in tmp:
                t = sorted(t)
                if tuple(t) in coms:
                    coms[tuple(t)]+=1
                else:
                    coms[tuple(t)] = 1
   # print(coms)
    for c in course:
        _max = 0
        for key,value in coms.items():
            
            #print(key,value)
            value= int(value)
            if value<2 or len(key) != c: continue
            _max = max(_max,value)
        for key,value in coms.items():
            value= int(value)
            if value<2 or len(key) != c: continue
            if value == _max:
                answer.append(''.join(key))
      

    return sorted(answer)
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))