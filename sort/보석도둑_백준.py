# 무게 순으로 보석을 정렬한다
# 가방도 수용량이 적은 것 부터 오름차순으로 정리한다
# 작은 것부터 해야지 최대한 담을 수 있다
# 
# 가방은 오름차순으로 정렬되어 있으므로 보석의 무게가 해당 가방이 담을 수 있는 무게라는 것은 다음 가방도 해당 보석을 담을 수 있다는 뜻
# -> 그래서 보석의 경우 무게가 작은 것부터 우선순위 큐로 빼내어 가격만 따로 담는 새로운 우선순위 큐(최대힙)에 저장
# 기존의 보석에서 가방의 무게보다 가벼운 보석을 계속 새로운 큐에 옮기고 제일 위(최대수)를 뽑아준다
# 가방은 남았지만 보석이 없거나 옮긴 곳에 보석이 없으면 탈출
import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
jew = []
bag = []
for i in range(n):
    a,b = map(int, input().split())
    heapq.heappush(jew,[a,b])

for i in range(k):
    heapq.heappush(bag,int(input()))
result = 0
q=[]

for i in range(k):
    
    capacity = heapq.heappop(bag)
    
    while jew and capacity >= jew[0][0]:
        weight, price = heapq.heappop(jew)
        heapq.heappush(q, -price)
    
    if q:
        result-=heapq.heappop(q) 

    elif not jew:
        break  
print(result)