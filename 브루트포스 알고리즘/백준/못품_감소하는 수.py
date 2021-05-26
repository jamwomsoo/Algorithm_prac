# 못품 - 굉장히 어렵넹,,
# 백준 사이트  https://www.acmicpc.net/problem/1038
# 참고 사이트  https://hose0728.tistory.com/86
# 1자리수 부터 시작해서 10자리수까지 브루트포스 알고리즘을 적용한다
# 1의 자리수를 가지려면 0부터9까지 가능
# 2의 자리수를 가지려면 1부터 9까지 가능(20,21)
# 3의 자리수를 가지려면 2부터 9까지 가능(320,321,310)
# 30번째 줄부터는 뒤에 나오는 자리수의 값이 현재 자신의 자리수보다 작아야 하므로 
# 맨 마지막의 숫자가 최대인 포문을 돌려 이후의 값을 정해준다

import sys
n = int(input())
cnt = -1
ans = -1
def dfs(limit,sub):
    global cnt, ans
    if len(sub) == limit:
        cnt+=1
        if cnt == n:
            ans = int(sub)
            print(ans)
            sys.exit()
        return
    else:
        if sub == '':
            for i in range(limit-1,10):
                sub=str(i)
                dfs(limit,sub)
                #sub = ''
        else:
            for i in range(int(sub[-1])):
                #이건 뭔지 모르겠네,,,,,
                # if limit - len(sub) - 1 > i:
                #     continue
                sub += str(i)
                dfs(limit, sub)
                sub = sub[:-1]

for k in range(1,11):
    dfs(k,'')
print(-1)