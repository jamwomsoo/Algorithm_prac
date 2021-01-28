import heapq
n = int(input())
arr= []
plus = []

for i in range(n):
    tmp = int(input())
    if tmp<=0:
        if 0 in arr:
            heapq.heappush(arr, tmp)
        else:
            heapq.heappush(arr, tmp)
    elif tmp>=0:
        plus.append(tmp)
            #heapq.heappush(plus, -tmp)
ans = 0


while arr:
    now = heapq.heappop(arr)
    if arr and arr[0]<=0:
        ans+=now*heapq.heappop(arr)
    else:
        ans+=now


plus = sorted(plus,reverse=True)

while plus:
    now = plus.pop(0)
    if plus and plus[0]>1:
        ans+=now*plus.pop(0)
    else:
        ans+=now

print(ans)
