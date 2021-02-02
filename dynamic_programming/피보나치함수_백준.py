i# 메모리를 필요한만큼만....
def func(x):
    one = [0,1]
    zero = [1,0]
    for i in range(2,x+1):
        zero.append(zero[-1]+zero[-2])
        one.append(one[-1]+one[-2])
    print(zero[x],one[x])

for _ in range(int(input())):
    n = int(input())
    func(n)