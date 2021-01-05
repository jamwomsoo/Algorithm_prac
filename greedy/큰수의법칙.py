import copy
N, M, K = map(int, input().split())
ls = list(map(int, input().split()))
ls2=list()
t = 0
tmp=M
sum = 0
ls2 = copy.deepcopy(ls)
print(ls2)
while True:
    if tmp<=0:
        break
    if tmp<K:
        for _ in range(0,tmp):
            sum+=max(ls)
    else:
        for _ in range(0,K):
            sum+=max(ls)
    
    ls2=[i for i in ls if i != max(ls)]
    sum+=max(ls2)
    tmp=tmp-K-1
print(sum)
  


