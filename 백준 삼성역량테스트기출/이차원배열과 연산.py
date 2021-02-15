r,c,k = map(int, input().split()) # R,C는 1부터 시작임 -> -1씩
arr = [list(map(int , input().split())) for _ in range(3)]
time = 0

def r_operater(array):
    ls = []
    tmp = [0]*101
    _max = 0
    for i in array:
        tmp[i]+=1
        _max = max(_max,i)
    for i in range(1,_max+1):
        if tmp[i] != 0:
            ls.append((i,tmp[i]))
    ls = sorted(ls, key = lambda x : (x[1],x[0]))
    re = []
    for i in ls:
        re.append(i[0])
        re.append(i[1])

    return  re
def change_hori_vert(array):
    nr,nc = len(array),len(array[0])
    #print(array)
    new_arr = [[0]*nr for _ in range(nc)]
    for x in range(nr):
        for y in range(nc):
            new_arr[y][x] = array[x][y]
    return new_arr



while True:
    nr, nc = len(arr),len(arr[0])

    # for x in range(nr):
    #     for y in range(nc):
    #         print(arr[x][y] , end = " ")
    #     print()
    # print()  
    if nr >=r and nc>= c:  
        if arr[r-1][c-1] == k:
            print(time)
            break
    if time > 100:
        print(-1)
        break
    if nr >100 or nc > 100:
        if nr > 100:
            arr = arr[:100]
        if nc > 100:
            for i in range(nr):
                arr[i] = arr[i][:nc]
    
    
    new_arr=[]
    _max = 0
    index = 0
    if nr>=nc:
        #print(time)
        for i in range(nr):
            ls = r_operater(arr[i])
            _max = max(_max,len(ls))
            new_arr.append(ls)
        for i in range(nr):
            tmp = new_arr[i]
            for j in range(_max-len(new_arr[i])):
                tmp.append(0)
            arr[i] = tmp
                
    else:    
        for i in range(nc):
            tmp = []
            for x in range(nr):
                tmp.append(arr[x][i])
                #print("tmp",tmp)
            ls = r_operater(tmp)
            _max = max(_max,len(ls))
            new_arr.append(ls)
        
        

        for i in range(nc):
            tmp = new_arr[i]
            for j in range(_max-len(new_arr[i])):
                tmp.append(0)
            new_arr[i] = tmp
            #print(new_arr[i])
        arr = change_hori_vert(new_arr)
    time+=1
    

