n = int(input())

arr = []
start=-int(1e9)
end = int(1e9)
for i in range(n):
    s,e = map(int, input().split())
    arr.append((s,e))
    start = max(s,start)
    end = min(e,end)

# for i in range(n):
#     s,e = arr[i]
    
if end - start>=0:
    print(0)
else:
    print(start-end)