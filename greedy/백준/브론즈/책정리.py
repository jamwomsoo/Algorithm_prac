
n,m = map(int, input().split())
box = list((map(int,input().split())))
book = list(map(int, input().split()))
total = 0
index = 0
for b in book:
    
    for i in range(n):
        if b <= box[i]:
            box[i]-=b
            break

print(sum(box))
