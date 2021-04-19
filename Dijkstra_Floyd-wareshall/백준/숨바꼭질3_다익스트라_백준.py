import heapq
from collections import deque
n, k = map(int, input().split())
distance = [int(1e9)]*(100001)
# q= []
q = deque()
distance[n] = 0
#heapq.heappush(q,(0,n))#dist,now
q.append((0,n))
def check(dist,value, next_x):
    cost = dist + value
    if -1< next_x < 100001 and cost < distance[next_x]:
        #heapq.heappush(q,(cost, next_x))
        distance[next_x] = cost
        q.append((cost,next_x))

while q:
    #dist, now = heapq.heappop(q)
    dist, now = q.popleft()
    #print(dist,now)
    if now == k:
        print(dist)
        break
    if distance[now]<dist:
        continue
    check(dist, 0, now*2)
    check(dist, 1, now-1)
    check(dist, 1, now+1)
    #print(q)

    


