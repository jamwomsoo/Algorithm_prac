# # 숫자를 입력받아서 한글로 출력하는 함수
# # 1~999
# def readNumber(n):
#   units = [''] + list('십백천')
#   nums = '일이삼사오육칠팔구'
#   result = []
#   i = 0
#   while n > 0:
#     n, r = divmod(n, 10)
#     if r > 0:
#       result.append(nums[r-1] + units[i])
#     i += 1
#   return ''.join(result[::-1])
#   def readNumber2(n):
#   """1억미만의 숫자를 읽는 함수"""
#   a, b = [readNumber(x) for x in divmod(n, 10000)]
#   if a:
#     return a + "만" +  b
#   return b
# if 10000<=n<100000000:
#     print(readNumber2(n))
# else:
#     print(readNumber(n))
n = int(input())
def readNumber(n):
    unit = ['']+list('십백천')
    num = '일이삼사오육칠팔구'
    arr = []
    while n>0:
        n,r = divmod(n,10)
        arr.append(r)
    result = ''
    for i in range(len(arr)-1,-1,-1):
        if i>=1 and arr[i] == 1:    
            result+=unit[i]
            
        else:
            if arr[i]>0:
                result+=num[arr[i]-1]+unit[i]
    return result

def readNumber2(n):
    a,b = [readNumber(x) for x in divmod(n,10000)]
    if a == '일':
        return '만'+b
    return a+'만'+b
if n ==0:
    print('영')
if 10000<=n<100000000:
    print(readNumber2(n))
else:
    print(readNumber(n))