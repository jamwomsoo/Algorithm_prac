def binary_search(target, array, start, end):
  if start > end:
    return 0
  mid = (start+end) // 2
  if array[mid] == target:
    return 1
  elif array[mid] > target:
    return binary_search(target, array, start, mid-1)
  else:
    return binary_search(target, array, mid+1, end)
   


n = int(input())
arrayN = list(map(int,input().split()))
sorted(arrayN)
m = int(input())
arrayM = list(map(int,input().split()))
sorted(arrayM)
for item in arrayM:
  result = binary_search(item, arrayN, 0, n-1)
  if result == 0:
    print("no", end=" ")
  else:
    print("yes",end= " ")


