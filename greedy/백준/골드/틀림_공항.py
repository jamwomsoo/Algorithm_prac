# 73프로 시간초과
# https://www.acmicpc.net/problem/10775
# 해설 :https://kkk4872.tistory.com/118
# greedy + find_union문제
# 문제팁:
# 해당 비행기를 넣을때 (1,plane)까지의 공항 게이트에 자리가 있는지 확인
# 자리가 찼다면 바로 앞에 게이트와 parent를 일치시켜서 최종적으로 0(plane에서 1까지 가득찼다면 0이 나옴)이 나온다

# 알고리즘
# 1. 해당 비행기가 들어갈 수 있는 게이트 번호를 입력받는다
# 2. 해당 게이트 번호의 parent(들어갈 수 있는 게이트를 찾는다)
#    -> 뒤에서 앞으로 숫자를 줄여가며 parent를 union했기 때문에 게이트를 찾을때마다 경로가 압축된다
# 3. 해당 게이트의 번호를 확인한다
#   3-1. 해당 게이트가 0번이라면 남는 게이트가 없는 것이다(break)
#   3-2. 해당 게이트가 0번이 아니라면 해당 번호 게이트에는 아직 비행기가 차있지 않은것이다. 

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] =find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: 
        parent[b] = a
    else:
        parent[a] = b

G = int(input())
P = int(input())
parent = [i for i in range(G+1)] 
# 해당 칸마다 채울 수 있는 게이트 번호를 표시함

ans = 0
gate_is_full_flag = False
minimum_num = 1
for i in range(P):
    plane = int(input())
    
    x = find_parent(parent,plane)
    if x==0: break
    union_parent(parent, x-1, x)
    ans+=1

print(ans)