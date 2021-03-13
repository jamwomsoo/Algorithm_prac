n, l = map(int,input().split())
leak = list(map(int, input().split()))
leak.sort()
position = leak[0]+l-1
cnt = 1
for i in leak:
    if i > position:
        #print("i",i)
        cnt+=1
        position=i+l-1
print(cnt)