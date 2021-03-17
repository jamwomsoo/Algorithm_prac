import bisect
n = int(input())
arr= list(map(int, input().split()))
cnt = 1
now = [arr[0]]
for i in arr:
    if i in now:
        index = now.index(i)
        now[index] -= 1
        if now[index] ==0:
            now.remove(0)
    else:
        #print(i)
        now.append(i-1)
        cnt+=1
print(cnt)

