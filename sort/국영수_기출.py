n = int(input())
ls =[list(input().split()) for _ in range(n)]
for i in range(0,n):
    for j in range(1,len(ls[0])):
        ls[i][j] = int(ls[i][j]) 
ls = sorted(ls,key = lambda x : (-x[1] , x[2] , -x[3],x[0]) )
for i in range(n):
    print(ls[i][0])