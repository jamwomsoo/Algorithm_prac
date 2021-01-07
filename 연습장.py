import heapq
q=[]

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    #food_times.sort()
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    length=len(q)
    previous_value=0
    sum_value=0
    while sum_value + (q[0][0] - previous_value) * length  <= k:
        now_value = heapq.heappop(q)[0]
        sum_value+=(now_value - previous_value)*length
        length-=1
        previous_value = now_value
    
    result = sorted(q, key = lambda x : x[1])
    
    return result[(k-sum_value)%length][1]
print(solution([3,1,2],5))