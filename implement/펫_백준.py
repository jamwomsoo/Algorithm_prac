flag = True
cnt = 0
while True:
    if flag == True:
        o,w = map(int,input().split()) # 적정, 현재 무게
        state = w
        cnt+=1
        flag = False
    if o == 0 and w == 0:
        break
    react, n = map(str,input().split())
    
    if react == '#' and n == '0':
        if o//2 < state < o*2:
            print(f"{cnt} :-)")
        elif state<= 0:
            print(f"{cnt} RIP")
        else:
            print(f"{cnt} :-(")
        flag = True

    if state<=0:
        continue
    
    if react =='F':
        state+=int(n)
    elif react == 'E':
        state-=int(n)