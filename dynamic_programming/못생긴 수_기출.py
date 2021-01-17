# from copy import deepcopy
# from itertools import combinations
# n = int(input())
# cnt = 1
# j = [1,2,3,5]
# num = [1,2,3,5]
# i=1
# cnt =1
# while cnt != n:
#     s=set()
#     tmp=deepcopy(i)
#     while tmp>1:
#         if tmp% 2 ==0:
#             tmp//=2
#         if tmp%3 ==0:
#             tmp//=3
#         if tmp%5 ==0:
#             tmp//=5
#         if tmp%2 != 0 and tmp%3!=0 and tmp%5 !=0:
#             s.add(tmp)
#             break
#         if tmp in num:
#             pass
#         else:
#             break
#     #print(tmp ," ",num)
#     if tmp == 1 and i not in num :
#         #print(i)
#         num.append(i)
#         cnt+=1 
#     i+=1
# num.sort()
# print(num)
# print(num[cnt-1])

n = int(input())
ugly = [0]*n
ugly[0] = 1

i2=i3=i5=0
next2,next3,next5 = 2,3,5

for i in range(1,n):
    ugly[i] = min(next2,next3,next5)
    if ugly[i] == next2:
        i2+=1
        next2 = ugly[i2]*2
    if ugly[i] == next3:
        i3+=1
        next3 = ugly[i3]*3
    if ugly[i] == next5:
        i5+=1
        next5 = ugly[i5]*5

print(ugly[n-1])
