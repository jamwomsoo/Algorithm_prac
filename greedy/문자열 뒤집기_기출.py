ls = list(map(int, input()))


count = [0]*2
#내 정답
q=list()
q.append((ls[0],ls[0],1))
for i in range(1,len(ls)):
  if ls[i-1] == ls[i]:
    a,b,cnt=q.pop()
    cnt+=1
    q.append((a,ls[i],cnt))
  else:
    q.append((ls[i],ls[i],1))
for a,b,cnt in q:
  if a == 0:
    count[0]+=1
  else:
    count[1]+=1


#해설지
# count[ls[0]]+=1
# for i in range(len(ls)-1):
#     if ls[i] != ls[i+1]:
#         if ls[i+1] == 0:
#             count[1]+=1
#         else:
#             count[0]+=1

print(min(count))