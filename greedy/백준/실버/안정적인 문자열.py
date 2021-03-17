index = 1 
while True:
    cnt = 0
    #state = 0
    arr = list(map(str, input()))
    if '-' in arr:
        break
    open_val = 0
    close_val = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == '{':
            open_val+=1
            
        else:
            close_val+=1
           
        if open_val < close_val:
            cnt+=1
            open_val+=1
            close_val-=1
    if open_val != close_val:
        cnt+= (open_val-close_val)//2
    
    print(f'{index}. {cnt}')
    index+=1