n , k = map(int, input().split())
ls1=list(map(int, input().split()))
ls2=list(map(int, input().split()))
#내풀이
# for _ in range(k):
#   ls1[ls1.index(min(ls1))],ls2[ls2.index(max(ls2))] = ls2[ls2.index(max(ls2))],ls1[ls1.index(min(ls1))]
# sum = 0 
# for i in ls1:
#   sum+=i
# print(sum) 

#풀이
ls1.sort()
ls2.sort(reverse=True)

for i in range(k):
    if ls1[i] < ls2[i]:
        ls1[i], ls2[i] = ls2[i], ls1[i]
    else:
        break

print(sum(ls1))
    
