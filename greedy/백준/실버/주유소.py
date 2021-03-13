n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))
result = 0
# 항상 낮은 도시의 기름값에서 곱해준다
min_value = city[0]
for i in range(n-1):
    if min_value > city[i]:
        min_value = city[i]
    result+=min_value*road[i]
    
         

print(result)