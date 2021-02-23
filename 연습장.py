arr = [[] for _ in range(2)]
e = [[0,1],[2,3]]
for _ in range(2):
    for i in range(2):
        arr[i]+=e[i]
print(arr)