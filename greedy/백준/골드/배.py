import sys

n = int(input())
crane_limit = list(map(int,input().split()))
m = int(input())
box_weight = list(map(int, input().split()))
time = 0

crane_limit.sort(reverse=True)
box_weight.sort(reverse=True)
if crane_limit[0]<box_weight[0]:
    print(-1) ; sys.exit()
while box_weight:
    time+=1
    for i in range(n):
        for j in range(len(box_weight)):
            if crane_limit[i]>=box_weight[j]: 
                del box_weight[j]
                break
print(time) 


    
