import heapq
n = int(input())
q = []
for i in range(n):
    a,b = map(int,input().split())
    heapq.heappush(q,(a,b))
start = q[0][0]
end = q[0][1]
arr=[]
while q:
    a,b = heapq.heappop(q)
    if end<=b and end >= a:
        end = b
    elif end < a:
        arr.append((start,end))
        start = a
        end = b
arr.append((start,end))        
result = 0
for s,e in arr:
    result += (e-s)
print(result)