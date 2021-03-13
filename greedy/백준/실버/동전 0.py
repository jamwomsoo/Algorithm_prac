n,k = map(int, input().split())
coin_num = 0
arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)

for i in arr:
    if k//i > 0:
        coin_num+=k//i
        k %=i
print(coin_num)