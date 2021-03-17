import sys
n = int(input())
want = list(map(int, input().split()))

origin  = [0]*n
cnt = 0
def turn_ligth(i):
    for j in range(i,i+3):
        if 0<=j<n:
            if origin[j] == 1:
                origin[j] = 0
            else:
                origin[j] = 1
    


for i in range(n):

    if want[i] != origin[i]:
        cnt+=1
        turn_ligth(i)
print(cnt)