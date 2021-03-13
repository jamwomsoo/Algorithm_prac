n,s,r = map(int, input().split())
demage = list(map(int,input().split()))
extra = list(map(int, input().split()))

for i in extra:
    if i in demage:
        demage.remove(i)
    elif i-1 in demage:
        demage.remove(i-1)
    elif i+1 in demage:
        demage.remove(i+1)
print(len(demage))