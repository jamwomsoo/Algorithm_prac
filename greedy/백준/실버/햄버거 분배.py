n,k = map(int, input().split())
arr = list(map(str,input()))
flag = True
cnt = 0
for i in range(n):
 
    if arr[i] != 'P':
        continue
    flag = False
    for j in range(k,0,-1):
        if i-j<0:
            continue
        if arr[i-j] == 'H':
            cnt+=1
            arr[i-j] = 'K'
            flag = True 
          
            break
    if not flag:
        for j in range(1,k+1):
            if i+j>=n:
                continue
            if arr[i+j] == 'H':
                cnt+=1
                arr[i+j] = 'K'
              
                break
#print(arr)
print(cnt)
    