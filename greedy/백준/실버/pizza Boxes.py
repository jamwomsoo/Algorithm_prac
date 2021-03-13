n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_list = set()
# 가로 체크
_max = -int(1e9)
for i in range(n):
    j = arr[i].index(max(arr[i]))
    #print(arr[i][j])
    max_list.add((i,j))

for j in range(m):
    _max = 0
    ls = ()
    for i in range(n):
        if _max < arr[i][j]:
            _max = arr[i][j]
            ls = (i,j)

    max_list.add(ls)
result = 0
for i in range(n):
    for j in range(m):
        if (i,j) not in max_list:
            result+=arr[i][j]

print(result)
    