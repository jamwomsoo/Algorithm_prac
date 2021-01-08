ls = list(input())
ls.sort()
sum=0
for i in range(len(ls)):
  if 'A'<= ls[i] <= 'Z':
    print(ls[i], end="")
  else:
    sum+=int(ls[i])  
print(sum)