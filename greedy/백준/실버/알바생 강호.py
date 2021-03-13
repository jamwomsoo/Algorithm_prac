n = int(input())
arr= [int(input()) for _ in range(n)]
arr.sort(reverse= True)
result = 0
for i,value in enumerate(arr):
    tmp = value - i
    if tmp>0:
        result+=tmp
print(result)