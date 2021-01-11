ls = list(input())
ls.sort()
sum=0
for i in range(len(ls)):
  if 'A'<= ls[i] <= 'Z':
    print(ls[i], end="")
  else:
    sum+=int(ls[i])  
print(sum)
##########
#답지 정답
##########
#isalpha()로 문자인지 숫자인지 확인가능
# data = input()
# result=[]
# value = 0

# for x in data:
#   if x.isalpha():
#     result.append(x)
#   else:
#     value+=int(x)

# result.sort()

# if value != 0:
#   result.append(str(value))
#   print(''.join(result)) 