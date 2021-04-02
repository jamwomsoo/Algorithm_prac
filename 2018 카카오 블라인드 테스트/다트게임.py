def solution(dartResult):
    answer = 0
    arr = [0,0,0]
    index = 0
    num = ''
    for i in dartResult:
        if i.isdecimal():
            num += i
        elif i.isalpha():
            arr[index] = int(num)
            num=''
            if i == 'S':
                arr[index]**=1
            elif i == "D":
                arr[index]**=2
            elif i == "T":
                arr[index]**=3
            index+=1
        elif not i.isalnum():
            tmp = index-1
            if i == '*':
                
                arr[tmp]*=2
                if tmp-1>=0:
                    arr[tmp-1]*=2
            else:
                arr[tmp] = -(arr[tmp])
    answer = sum(arr) 
    return answer
#print(solution('1S2D*3T'))
print(solution(	"1D2S#10S"))