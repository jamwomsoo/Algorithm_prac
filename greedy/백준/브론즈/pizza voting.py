# 못품 #
import sys
n,p = map(int, input().split())
arr = []
name= []

for i in range(n):
    kcal,_name = map(str,input().split())
    arr.append(int(kcal))
    name.append(_name)
goal = name[p-1]
index = 0

while len(arr) != 1:
    if goal not in name:
        print("NO")
        sys.exit()
    if index %3 ==0:
        tmp = max(arr)
        i= arr.index(tmp)
        #print(arr[i],name[i])
        del arr[i]; del name[i]
    elif index%3 ==1 :
        tmp = min(arr)
        i= arr.index(tmp)
        #print(arr[i],name[i])
        del arr[i]; del name[i]
    else:
        if p <= n//2:
            tmp = max(arr)
            i = arr.index(tmp)
            #print(arr[i],name[i])
            del arr[i]; del name[i]
        elif p> n//2:
            tmp = min(arr)
            i = arr.index(tmp)
            #print(arr[i],name[i])
            del arr[i]; del name[i]

    index+=1
#print(arr,name)
if name[0] == goal:
    print("YES")
else:
    print("NO")
