#못품.....
n = int(input()) # 꽃의 가지수
ls = []
flower=[]

for i in range(n):
    data = list(map(int, input().split()))
    start,end = data[0]*100+data[1],data[2]*100 + data[3]
    ls.append((start,end))
ls = sorted(ls, key = lambda x : (x[0],x[1]))
date,index,tmp,changed = 301,-1,0,False
ans = 0
while date<=1130 and index < n:
    index+=1
    
    changed= False
    for i in range(index,n):
        s,e = ls[i]
        if s > date:
            break
        if tmp < e:
            tmp = e
            changed =True
            index = i
    if not changed:
        print(0)
        break
    else:
        ans+=1
        date = tmp 
if changed:
    print(ans)



    
