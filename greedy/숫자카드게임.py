# n, m = map(int, input().split())
# ls = [[0]*m for _ in range(0,n)]
# ls2 = []
# last = 0
# index = 0

# for i in range(0, n):
#     #for j in range(0, m):
#       ls[i] = list(map(int,input().split()))
# last = ls[0][0]
# for i in range(0, n):
#   print(min(ls[i]))
#   ls2.append(min(ls[i]))

# ls2.sort()

# print(ls2[-1])

n,m= map(int,input().split())
result=0

for _ in range(n):
    data=list(map(int,input().split()))
    mini=min(data)
    result = max(result,mini)
print(result)