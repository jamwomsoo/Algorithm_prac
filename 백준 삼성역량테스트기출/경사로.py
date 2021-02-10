#틀
n, l = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
total = 0 

def func(narr):
    global n,l
    build = [False]*n

    for i in range(n-1):
        if abs(narr[i]-narr[i+1]) > 1:
            return False
        if abs(narr[i] - narr[i+1]) == 1:
            if narr[i] > narr[i+1]:
                for j in range(i+1,i+1+l):
                    if 0<=j<n:
                        if build[j]:
                            return False
                        if narr[i+1] != narr[j]:
                            return False
                        build[j]=True 
                    else:
                        return False
            else:
                for j in range(i,i-l,-1):
                    if 0<=j<n:
                        if build[j]:
                            return False
                        if narr[i] != narr[j]:
                            return False
                        build[j]=True 
                    else:
                        return False
        if abs(narr[i] - narr[i+1]) == 0:
            continue
    return True

    
for i in range(n):
    if func(arr[i]):
        total+=1
for j in range(n):
    tmp = []
    for i in range(n):
        tmp.append(arr[i][j])
    if func(tmp):
        total+=1
print(total)
