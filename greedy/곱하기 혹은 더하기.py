ls = list(map(int,input()))
#print(ls)
# 내 정답
#  now = ls[0]
# #while True:
# for i in range(1,len(ls)):
#   if now==0 or ls[i] ==0:
#     now = ls[i]+now
#   else:
#     now=now*ls[i]

#해설
now = ls[0]
for i in range(1,len(ls)):
    if now <=1 or ls[i]<= 1:
        now += ls[i]
    else:
        now *= ls[i] 
print(now)