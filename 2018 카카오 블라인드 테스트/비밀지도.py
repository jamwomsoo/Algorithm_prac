def numToArr(num,n):
    arr = []
    while num>0:
        num,r = divmod(num,2)
        arr.append(r)
    
    while len(arr)<n:
        arr.append(0)
    
    arr.reverse()
    #print(arr)
    return arr
def solution(n, arr1, arr2):
    answer = []
    ls1 = [] 
    for index,value in enumerate(arr1):
        ls1.append(numToArr(value,n))
    ls2 = []
    for value in arr2:
        ls2.append(numToArr(value,n))
    for i in range(n):
        st = ""
        for j in range(n):
            if ls1[i][j]+ls2[i][j]>0:
                st+='#'
            else:
                st+=' '
        answer.append(st)
    
    return answer
print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))