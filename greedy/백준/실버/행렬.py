# 백준 사이트 : https://www.acmicpc.net/problem/1080

# 당장 눈에 보이는 다른 숫자를 맞게 고쳐준다
# 0,0 부터 시작해서 n-2,m-2까지 고쳤을때 결국 두 행렬이 같아 진다고 생각해 그리디라고 생각되는 문제이다
# -> 격자의 위부터 시작해서 같은 숫자로 되게 맞춰준다는 아이디어
import sys
n,m = map(int, input().split())
arr1 = [list(map(int, input())) for _ in range(n)]
arr2 = [list(map(int, input())) for _ in range(n)]
if arr1 == arr2:
    print(0)
    sys.exit()
if n<3 and m<3:
    print(-1)
    sys.exit()

cnt = 0

for i in range(n-2):
    for j in range(m-2):
       
        if arr1[i][j]!=arr2[i][j]:

            for x in range(i,i+3):
                for y in range(j,j+3):
                    if arr1[x][y] == 0:
                        arr1[x][y] = 1 
                    else:
                        arr1[x][y] = 0
            cnt+=1

if arr1 != arr2:
    print(-1)
else:
    print(cnt)
