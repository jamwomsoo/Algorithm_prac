#못품.....
n = int(input()) # 꽃의 가지수
ls = []
def next_month(now):
    month = now // 100
    day = now % 100
    if month ==2 and day == 28:
        return 301
    elif (month == 4 or month == 6 or month == 9 or month == 11 ) and day == 30:
        return (month+1)*100 + 1
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day == 31 :
        return ((month+1)%12)*100 + 1


for i in range(n):
    data = list(map(int, input().split()))
    start,end = data[0]*100+data[1],data[2]*100 + data[3]
    ls.append((start,end))
ls = sorted(ls, key = lambda x : (x[0],x[1]))
start_check,end_check = False,False
small = int(1e9)
big = 0
index = 0

for i in range(len(ls)):
    start,end = ls[i]
    if start<=301:
        if big < end:
            big = end
            index = i   
        start_check = True
    if end >= 1130:
        end_check = True
if not (start_check and end_check):
    print(0)
else:
    start,end = ls[index][0], ls[index][1]
    cnt = 1
    tmp = 0
    #print(ls)
    index+=1
    while end<=1130:
        t = end//100
         
        if index>=n:
            break
        #print(start,end)
        s,e = ls[index]
        #print(index,s,e)
        if s <= end and e > end:
            pass
        if s>end or index == n-1:
            if  next_month(end) == s:
                end = e
            end = tmp
            cnt+=1
            if index >= n-1:
                break
        index+=1
    if end >= 1130:
        print(cnt)    
    else:
        print(0)





    
