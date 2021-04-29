
n = int(input())
prime = [2,3,5,7]

def isprime(num):
    if num<2: return False
    for i in range(2,num):
        if num%i==0: return False

    return True

def dfs(first,num):
    if num == 0: print(first)

    for i in range(1,10,2):
        tmp = first*10 + i
        if isprime(tmp): dfs(tmp,num-1)

for i in range(4):
    dfs(prime[i],n-1)
    