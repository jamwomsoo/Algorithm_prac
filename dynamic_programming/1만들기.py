n = int(input())
cnt=0
arr = [0]*30001
#내 풀이
""" def dynamic(num):
  global cnt

  if num == 1:
    return cnt
  if arr[num] !=0 :
    return arr[num]  
  cnt+=1 
  if num%5==0:
    arr[num] = cnt 
    return dynamic(num//5)
  elif num>1 and num %2 == 0:
    arr[num] = cnt 
    return dynamic(num-1)  
  elif num %3 == 0:
    arr[num] = cnt 
    return dynamic(num//3)
  elif num %2 ==0:
    arr[num] = cnt 
    return dynamic(num//2)
  """


def dynamic(n):
    for i in range(2,n+1):
        arr[i] = arr[i-1] + 1
        if i%2==0:
            arr[i] = min(arr[i], arr[i//2] + 1)
        if i%3==0:
            arr[i] = min(arr[i], arr[i//3] + 1)
        if i%5==0:
            arr[i] = min(arr[i], arr[i//5] + 1)

    return arr[num]        


print(dynamic(n))  
  
