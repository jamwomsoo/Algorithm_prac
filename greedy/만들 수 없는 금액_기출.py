from itertools import combinations 

n = int(input())
ls = list(map(int, input().split()))
# check = [False] * (sum(ls)+1)
# for  i in range(1,n+1):
#     coms = list(combinations(ls,i))
#     for com in coms:
#         #print(com)
#         if sum(com) <= max(ls) and check[sum(com)] == False:
#             #print(sum(com))
#             check[sum(com)] = True
            

# for i in range(1,max(ls)+1):
#     if check[i] == False:
#         print(i)
#         break
    
#해설지
#1부터 타겟으로 잡고 타켓을 하나씩 늘리면서 판단한다
ls.sort()
target = 1
for data in ls:
    if target < data:
        break
    target+=data
print(target)
#예시
#n=5
#ls =3 2 1 1 9
# sort ls = 1 1 2 3 9
# 1. 타겟 1부터 설정
# 2. 타겟 1: 1인 단위의 동전 존재 terget = 1 + 1로 업데이트(다음 가진 동전) //1까지는 만들 수 있음
# 3. 타겟 2: 1인 단위의 동전 존재 tartget = 2 + 1로 업데이트      //2까지는 만들 수 있음
# 4. 타겟 3: 2인 단위의 동전 존재 target  = 3 + 2으로 업데이트  //4까지는 만들 수 있음
# 5. 타겟 5: 3인 단위의 동전 존재 target = 5 + 3으로 업데이트   //7까지는 만들수 있음 
# 6. 타겟 7: 확인
# 다음 단위의 동전은 9이므로 8은 만들 수 없다


