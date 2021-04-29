for i in range(int(input())):
    n = int(input())
    initial = list(map(str,input()))
    goal = list(map(str,input()))
    init = 0
    g = 0
    diff = 0
    for i in range(n):
        if initial[i] == 'W':
            init +=1
        if goal[i] == 'W':
            g+=1
        if goal[i] != initial[i]:
            diff+=1

    if init == g:
        print(diff//2)
    else:
        tmp = abs(g-init)
        diff = (diff-tmp)//2 + tmp
        print(diff)
