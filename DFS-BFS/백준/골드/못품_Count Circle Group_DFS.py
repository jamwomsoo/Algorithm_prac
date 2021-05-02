# 못품 - 시간초과
# 백준 싸이트 https://www.acmicpc.net/problem/10216
# 참고 사이트 https://donggod.tistory.com/90
def calcDistance(a,b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return x**2 + y**2

# 해당 원에 접해져있는거 타고 타고 타서 같은 그룹으로 만든다(방문 처리)
# 초기에 방문이 있을때 마다 그룹의 숫자를 늘린다
def dfs(index):
    global n
    for i in range(n):
        rSum = r[index] + r[i]
        # 같은 원이거나 방문되었거나 두 원사이의 거리보다 크면(접해있지 않으면) pass
        if index == i or visited[i] or calcDistance(position[index],position[i]) > rSum * rSum:
            continue
        visited[i] = 1
        dfs(i) 

for _ in range(int(input())):
    n = int(input())
    visited =[0]*n 
    position = []
    r = []
    for i in range(n):
        a,b,c = map(int, input().split())
        position.append([a,b])
        r.append(c)
    group = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            group+=1
    print(group)