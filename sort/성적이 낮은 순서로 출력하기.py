n = int(input())
ls=[]
for i in range(n):
  k,v = input().split()
  ls.append((k,int(v)))
  
#내 풀이
# def function(data):
#   return data[1]
# result = sorted(ls, key=function)

#lambda 이용 풀이: 해설
result = sorted(ls, key = lambda student: student[1])

for student in result:
  print(student[0], end= ' ')

