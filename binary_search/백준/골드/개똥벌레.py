# 못품
# prefix sum 문제
# prefix sum 관련 설명 페에지 https://www.crocus.co.kr/843

# 특정 높이 i에서 지나는 종유석의 개수는 높이 (i+1에서 통과하는 종류석의 개수)+(높이 i에서 새롭게 통과하는 종유석의 개수)
# 높이 1~h 


n,h = map(int, input().split())
top = [0]*(h+1)
bottom = [0]*(h+1)

for i in range(n):
    t = int(input())
    if i%2:
        top[t]+=1
    else:
        # h-t+1 하는 이유는 위에가 1이기 때문에 종류석에 맞추려고
        # 석순 키가 4면-> 위에서는 2까지 자란것   
        bottom[h-t+1]+=1
# 종유석
# 종류석은 위에서 아래로 자라기때문에
# 위로 갈 수록 많이 있다
for i in range(h-1,0,-1):
    top[i] += top[i+1]
# 석순
# 석순은 아래에서 위로 쏟기 때문에
# 아래로 갈 수 록 많이 있다

for i in range(1,h+1):
    bottom[i] += bottom[i-1]
total = [0]*(h+1)
for i in range(1,h+1):
    total[i] = top[i]+bottom[i]
total = total[1:]
ans = min(total)
print(ans, total.count(ans))