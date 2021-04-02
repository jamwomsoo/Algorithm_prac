def solution(str1, str2):
    answer = 0
    dic1 ={}
    dic2 ={}
    tmp = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            sliceLowerStr = (str1[i]+str1[i+1]).lower()
            tmp.append(sliceLowerStr)
            if sliceLowerStr not in dic1.keys():
                dic1[sliceLowerStr] = 1
            else:
                dic1[sliceLowerStr] += 1
        
    str1,tmp = tmp,[]
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            sliceLowerStr = (str2[i]+str2[i+1]).lower()
            tmp.append(sliceLowerStr)
            if sliceLowerStr not in dic2.keys():
                dic2[sliceLowerStr] = 1
            else:
                dic2[sliceLowerStr] += 1
    str2 = tmp

    str1 = set(str1); str2 = set(str2)
    _union = []
    tmp = str1 | str2
    for i in tmp:
        if i in dic1.keys() and i not in dic2.keys():
            for j in range(dic1[i]):
                _union.append(i)
        if i not in dic1.keys() and i in dic2.keys():
            for j in range(dic2[i]):
                _union.append(i)
        if i in dic1.keys() and i in dic2.keys():
            _max = max(dic1[i],dic2[i])
            for j in range(_max):
                _union.append(i)

    tmp = str1 & str2
    _intersection = []
    for i in tmp:
        _min = min(dic1[i],dic2[i])
        for j in range(_min):
            _intersection.append(i)
    if len(_union)!=0 and len(_intersection)!=0:
        answer = float(len(_intersection))/float(len(_union)) *  65536
    else:
        answer = 1
    
    return int(answer)
print(solution('FRANCE','french'))
print(solution('handshake','shake hands'))
print(solution(	"aa1+aa2","AAAA12"))