
n = int(input())
a_lst = list(map(int, input().split()))
b, c = map(int, input().split())

total = 0
    
for i in range(n):
    total+=1
    a_lst[i] -= b
    if a_lst[i] > 0:
        total += a_lst[i]//c
        z = a_lst[i] % c
        if z > 0:
            total+=1

print(total)