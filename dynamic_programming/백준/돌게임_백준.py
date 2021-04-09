n = int(input())
ans = n
check = 0
arr= [[0] for _ in range(2)]
i = 1
while ans > 0:
    print(i)
    i+=1
    if ans - 3 >=0:
        arr[check].append(arr[(check+1)%2][-1]+3)
        ans-=3
    elif ans - 1 >= 0:
        arr[check].append(arr[(check+1)%2][-1]+1)
        ans-=1
    check = (check+1)%2       
if n in arr[0]:
    print("SK")
else:
    print("CY")