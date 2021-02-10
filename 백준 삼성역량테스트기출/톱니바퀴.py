arr=[]
for i in range(4):
    arr.append(list(map(int, input())))
k = int(input())

def turn(array,how):
    if how == -1: #반시계
        tmp = array[0]
        for i in range(7):
            array[i] = array[i+1]
        array[7] = tmp
    elif how == 1:
        tmp = array[7]
        
        for i in range(7,0,-1):
            
            array[i] = array[i-1]
        array[0] = tmp
        
    return array

def check(arr):
    c = []
    
    for i in range(3):
        if arr[i][2] == arr[i+1][6]:
            c.append(True)
        else:
            c.append(False)
    
    return c

for _ in range(k):
    num,how = map(int, input().split())
    c = check(arr)
    num = num-1
    arr[num] = turn(arr[num],how) 
    tmp = how
    for i in range(num-1,-1,-1):
        if not c[i]: #극이 다를때
            
            if tmp == -1:
                tmp = 1
            else:
                tmp = -1
            arr[i] = turn(arr[i],tmp)
        else:
            break
    tmp = how
    for i in range(num,3):
        if not c[i]:
           
            if tmp == -1:
                tmp = 1
            else:
                tmp = -1
            
            arr[i+1] = turn(arr[i+1],tmp)
            
        else:
            break


result =0
for i in range(4):
    tmp = arr[i][0]
 
    if tmp == 0:
        continue
    if i == 0:
        result+=1
    if i == 1:
        result+=2
    if i ==2:
        result+=4
    if i == 3:
        result+=8
print(result)
    

