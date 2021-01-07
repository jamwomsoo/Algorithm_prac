#내가 구한문제 => 그룹의 최솟값
n = int(input())
ls = list(map(int,input().split()))
# index = len(ls) - 1
ls.sort()
#print(ls)
group=0
# while len(ls)>0:
#   tmp = ls[index]
#   #print("tmp ",tmp)
#   for i in range(tmp):
#     ls.pop()
#     #print(a)
#     index-=1
#   group+=1
#최솟값으로 다시 구한거
index=0
g=[]

# for i in range(len(ls)):
#     tmp = ls[i]
#     g.append(tmp) 
#     if tmp == len(g):
#         del g[0:]
#         group+=1

#정답
cnt=0
for i in range(len(ls)):
    cnt+=1 
    if cnt >=ls[i]:
        group+=1
        cnt=0

print(group)


