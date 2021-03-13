alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')

word = str(input())
result = 0
now = 0
for w in word:
    goal = alpha.index(w)
    dif = abs(now-goal)
    now = goal
    result+=min(26-dif,dif)
print(result)
    