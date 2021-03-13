n = int(input())
for i in range(n):
    now = int(input())
    total = [0,0,0,0]
    if now>=25:
        total[0]=now//25
        now %=25
   
    if now>=10:
        total[1]=now//10
        now%=10
    if now>=5:
        total[2]=now//5
        now%=5
    if now>=1:
        total[3]=now//1
    for i in total:
        print(i,end=' ')
    print()
