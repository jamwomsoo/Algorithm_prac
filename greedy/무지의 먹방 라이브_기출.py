from collections import deque
#k = int(input())
#food_times = list(map(int, input().split()))
def solution(food_times, k):
    t=0
    index = 0
    q = deque()
    if all(v==0 for v in food_times):
            return -1
    for i in range(len(food_times)):
        q.append((i,food_times[i]))
    for i in range(k):
        if all(v==0 for v in food_times):
            return -1
        index, food = q.popleft()
        food-=1
        food_times[index]-=1
        if food > 0:
            q.append((index,food))
    if not q:
        return -1
    index, food = q.popleft()
    
    return index+1