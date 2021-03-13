n,l,k = map(int, input().split())
arr = []
for i in range(n):
    e,h = map(int, input().split())
    arr.append((e,h))
arr = sorted(arr,key = lambda x : (x[1],x[0]))

result = 0
for i in range(n):
    if k == 0:
        break
    e,h = arr[i]
    if h<=l:
        result+=140
        k-=1
    elif e<=l:
        result+=100
        k-=1
print(result)