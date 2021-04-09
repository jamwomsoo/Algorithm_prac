# 조합문제
# nCm = nCm-1 + (n-1)c(m-1) 이용
table = {}
def com(m,n):
    #print(m,n)
    if (m,n) in table.keys():
        return table[(m,n)]
    if m==n or m ==0 or n == 0:
        table[(m,n)] = 1
        return table[(m,n)]
    table[(m,n)] = com(m,n-1) + com(m-1,n-1) 
    return table[(m,n)]
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(com(n,m))