# dfs를 통한 중복 순열으로 계산

from itertools import permutations
from collections import deque
n= int(input())
#수식
data = list(map(int,input().split())) 
#연산자
#덧셈, 뺄겜 ,곱셈, 나눗셈
add, sub, mul, div = map(int,input().split())

big = -int(1e9)
small = int(1e9)

def dfs(index,now):
    global big,small, add, sub, mul, div
    if index == n:
        #수식이 맨 마지막일때
        big = max(big,now)
        small = min(small,now)   
    else:
        if add > 0:
            add-=1
            dfs(index+1, now + data[index])
            add+=1
        if sub > 0:
            sub-=1
            dfs(index+1, now - data[index])
            sub+=1
        if mul > 0:
            mul-=1
            dfs(index+1, now * data[index])
            mul+=1
        if div > 0:
            div-=1
            dfs(index+1, int(now / data[index]))
            div+=1
        
dfs(1,data[0])
print(big)
print(small)