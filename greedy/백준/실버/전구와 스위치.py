import sys
from copy import deepcopy
n = int(input())
ori = list(map(int, input()))
cha = list(map(int, input()))
sub_ori = deepcopy(ori)
cnt= 0
# 전구에 영향을 주는 경우를 생각해보자
# 우선 0번 전구를 킬까 말까를 고민해서 케이스를 나눈다
# 그 후 0번이 누를지 안누를지 정해지고 0번이 같다면
# 1번만이 0번에 영향을 주기때문에 1번을 누르면 안된다
# 반대 상황일때는 1번을 누른다
# 이와 같이 계속 반복한다
# -> 인덱스를 앞으로 진행하면서 이전 상태를 고정하면 현재 스위치만 고정된 전구에 영향을 준다는 뜻
def process(i):
    for j in range(i-1,i+2):
        if 0<=j<n:
            if ori[j] == 0:
                ori[j] = 1
            else:
                ori[j] = 0  
# 0을 안눌었을때
for i in range(1,n):
    if ori[i-1] != cha[i-1]:
        cnt+=1
        process(i)
        
if ori == cha: 
    print(cnt)
    sys.exit()
# 0 번을 눌렀을때
cnt = 1
ori = sub_ori
for i in range(2):
    if ori[i] == 0:
        ori[i] = 1
    else:
        ori[i] = 0
    
for i in range(1,n):
    if ori[i-1] != cha[i-1]:
        cnt+=1
        process(i)
        
if ori == cha: 
    print(cnt)
    sys.exit()
else:
    print(-1)

