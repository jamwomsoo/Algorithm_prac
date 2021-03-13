import sys
st = list(map(str, input()))
cnt = 0
answer = ''
def process(cnt):
    global answer
    while cnt>0:
    
        if cnt>=4:
            answer+='AAAA'
            cnt-=4
            
        elif cnt>=2:
            answer+='BB'
            cnt-=2
            
        elif cnt%2 !=0: break
            
        
    if cnt>0:
        print(-1)
        sys.exit()
    

for i in range(len(st)):
    if st[i] == 'X':
        cnt+=1
    else:
        process(cnt)
        cnt = 0
        answer+='.'
process(cnt)
print(answer)


