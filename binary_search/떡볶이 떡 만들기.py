n ,m = map(int, input().split())
arr = list(map(int, input().split()))

n ,m = map(int, input().split())
arr = list(map(int, input().split()))
#내풀이
""" def rice_cake(target,arr, start, end):  
  remain=0
  if start > end:
    return arr[end]
  mid = (start+end) // 2
  for i in arr:
    if arr[mid] - i > 0:
      remain+=arr[mid]
  if remain ==target:
    return arr[mid]
  if remain < target:
    return rice_cake(target,arr, start, mid-1)
  elif remain > target:
    return rice_cake(target, arr ,mid+1,end)


print(rice_cake(m,arr, 0, n-1)) 
 """

#해설 풀이
def binary_search(target, arr, start, end):
    if start > end:
        return end 
    remain = 0
    mid = (start+end) // 2
    for i in arr:
        if i > mid:
            remain+=(i-mid)
    if remain == target:
        return mid
    elif remain < target:
        return binary_search(target,arr, start, mid-1)
    else:
        return binary_search(target,arr, mid+1,end)
print(binary_search(m, arr, 0, max(arr)))
