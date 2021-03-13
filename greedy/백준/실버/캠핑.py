case = 1
while True:
    l,p,v = map(int, input().split())
    if l == 0 and p == 0 and v==0:
        break
    ans = 0
    while v>p:
        v-=p
        ans+=l
    if v>=l:
        ans+=l
    else:
        ans+=v
    print(f'Case {case}: {ans}')
    case+=1