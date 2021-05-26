from bisect import bisect_left,bisect_right 
arr = [0,1,2,3,4,5,9]
i = bisect_left(arr,7)
j = bisect_right(arr,7)
print(i,j)

a = 12345
print(a[0])