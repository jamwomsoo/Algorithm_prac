import bisect
n,m = map(int, input().split()) # 스크린, 바구니 개수
J = int(input())
start = 1
end = m
result = 0
for i in range(J):  
    apple = int(input())
   
    if start != end:
        if start<=apple<=end:
            pass
        else:
            a_s = abs(apple-start)
            a_e = abs(apple-end) 
            if a_s >a_e:
                result+=a_e
                start +=a_e
                end +=a_e
            else:
                result +=a_s
                start-=a_s
                end-=a_s
    else:
        if apple == start:
            pass
        else:
            result+=abs(start-apple)
            start = end = apple


print(result)

