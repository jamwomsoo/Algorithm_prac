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
            #2 1 1 1
            # 먼저 인덱스가 더 클때
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
            # 나중 인덱스가 더 클때
            # 1 1 1 2
            else:
                for j in range(i,i-l,-1):
                    if 0<=j<n:
                        # 이미 블록이 있으면 x
                        if build[j]:
                            return False
                        # 경사로의 크기가 있기때문에 그 크기만큼 사이즈가 같아야됨
                        if narr[i] != narr[j]:
                            return False
                        build[j]=True 
                    else:
                        # 만약 경사로 놓기에 사이즈가 작으면 x
                        return False
        if abs(narr[i] - narr[i+1]) == 0:
            continue
    return True

# 가로확인
for i in range(n):
    if func(arr[i]):
        total+=1
# 세로확인
for j in range(n):
    tmp = []
    # 가로로 회전시킴
    for i in range(n):
        tmp.append(arr[i][j])
    
    if func(tmp):
        total+=1
print(total)
