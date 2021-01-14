import heapq
n = int(input())
ls = []
for i in range(n):
    heapq.heappush(ls, int(input()))


result =0
while len(ls) != 1:
    tmp = heapq.heappop(ls)+heapq.heappop(ls)
    heapq.heappush(ls,tmp)
    result+=tmp
    
print(result) 