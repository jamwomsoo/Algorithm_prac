import sys
n,k = map(int, input().split())

start = 0
for i in range(k):
    start+=(i+1)
if n<start:
    print(-1)
else:
    n -= start
    if n%k == 0:
        print(k-1)
    else:
        print(k)