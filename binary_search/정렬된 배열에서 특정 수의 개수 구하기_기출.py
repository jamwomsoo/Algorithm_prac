import bisect
n,x = map(int, input().split())
ls = list(map(int, input().split()))
#if bisect.bisect_left(ls,n) == n:
if bisect.bisect_right(ls,x) - bisect.bisect_left(ls,x) == 0:
    print(-1)
else:
    print(bisect.bisect_right(ls,x) - bisect.bisect_left(ls,x))
