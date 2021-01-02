n = int(input())
ls = [input() for i in range(n)]
# ls =[]
# for i in range(n):
#   ls.append(input())
# ls.sort(reverse=True)
ls = sorted(ls, reverse=True)
print(ls)