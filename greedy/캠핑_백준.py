import sys
input = sys.stdin.readline
index = 1
while True:
    
    L,P,V = map(int, input().split())
    if L==0 and P==0 and V==0:
        break
    result = V//P*L
    if V % P <= L:
        result += V % P
    else:
        result +=L
        
    print("Case {0}: {1}".format(index,result))
    index+=1 
    