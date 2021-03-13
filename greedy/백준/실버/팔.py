import sys
l,r= map(str, input().split())
cnt = 0
# 두 수의 길이가 다르면 무조건 8이 없이 할 수 있다
# 두 수의 길이가 같을때 높은 수부터 낮은 수로 내려갈때 만약 둘다 8이 공통으로 있다가 없으면 그 자리수 부터 8이 아닌수를 넣을 수 있다
# 8899 8999 -> 1개
# 7800 8999 -> 0개
if len(r) == len(l):
    flag= False
    for i in range(len(r)):
        if r[i] !=l[i]:
            break
            
        if r[i] == '8' and l[i]=='8':
            cnt+=1
print(cnt)
        