
m,n = map(int, input().split())
store = int(input())
arr = []

for _ in range(store+1):
    a,b = map(int, input().split())
    if a == 1:
        arr.append([0,b])
    elif a == 2:
        arr.append([n,b])
    elif a == 3:
        arr.append([b,0])
    else:
        arr.append([b,m])
x = arr.pop()
#print(arr,x)
ans = 0
for arr_x,arr_y in arr:
    if abs(arr_x - x[0]) == n:
        # 시계
        clock = n + arr_y + x[1]
        un_clock = n + m-arr_y + m-x[1] 
        ans+=min(clock,un_clock) 
    elif abs(arr_y - x[1]) == m:
        clock = m + arr_x + x[0]
        un_clock = m + n - arr_x + n - x[0]
        ans+=min(clock,un_clock)
    else:
        ans += abs(arr_x - x[0]) + abs(arr_y - x[1])
    

print(ans)
